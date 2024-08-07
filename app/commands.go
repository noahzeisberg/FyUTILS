package app

import (
	"context"
	"encoding/json"
	"fmt"
	"github.com/noahzeisberg/FyUTILS/log"
	"github.com/noahzeisberg/FyUTILS/networking"
	"github.com/noahzeisberg/FyUTILS/typing"
	"github.com/noahzeisberg/FyUTILS/utils"
	"io"
	"math"
	"net"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"slices"
	"strings"
	"sync"
	"time"

	"github.com/google/go-github/github"
	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/networking/requests"
	"golang.org/x/sync/semaphore"
)

var (
	githubClient = github.NewClient(nil)
)

func FloodCommand(args []string) {
	ip := args[0]
	port := args[1]

	conn, err := net.Dial("tcp", net.JoinHostPort(ip, port))
	if err != nil {
		log.Error("Failed to connect to target: " + err.Error())
		return
	}

	for {
		randomBytes, err := utils.RandomBytes(1024)
		if err != nil {
			log.Error("Cannot generate random bytes.")
			break
		}
		_, err = conn.Write(randomBytes)
		if err != nil {
			log.Error("Failed to send data to connection.")
			break
		}
		log.Print("Bytes successfully sent to " + color.Blue + conn.RemoteAddr().String())
	}
}

func PortscanCommand(args []string) {
	ip := args[0]
	lock := semaphore.NewWeighted(1024)

	results := make(chan int, 1024*64)

	var wg sync.WaitGroup
	commandStartTime := time.Now()

	for port := 0; port < 1024*64; port++ {
		wg.Add(1)
		err := lock.Acquire(context.TODO(), 1)
		if err != nil {
			log.Error(err.Error())
			return
		}
		go func(port int) {
			networking.ScanPort(ip, port, results)
			lock.Release(1)
			wg.Done()
		}(port)
	}
	wg.Wait()
	close(results)

	log.Print("Scan took " + fmt.Sprint(math.Trunc(time.Since(commandStartTime).Seconds())) + "!")
	log.Print()

	var openPortGroups []typing.Group
	for port := range results {
		openPortGroups = append(openPortGroups, typing.Group{
			A: fmt.Sprint(port),
			B: utils.GetPortService(port),
		})
	}

	log.Print(log.GroupContainer(openPortGroups...))
}

func WhoisCommand(args []string) {
	target := args[0]
	var data typing.AddressInformation
	body := requests.Get("https://ipwho.is/" + target)

	err := json.Unmarshal(body, &data)
	if err != nil {
		log.Error("Failed to parse JSON.")
		return
	}

	log.Print("WHOIS Report for " + color.Blue + data.IP)
	log.Print()
	log.Print(log.GroupContainer([]typing.Group{
		{A: "Target", B: data.IP},
		{A: "Address Type", B: data.Type},
		{A: "Continent", B: data.Continent + " (" + data.ContinentCode + ")"},
		{A: "Country", B: data.Country + " (" + data.CountryCode + ")"},
		{A: "Region", B: data.Country + " (" + data.RegionCode + ")"},
		{A: "City", B: data.Country},
		{A: "Latitude", B: data.Latitude},
		{A: "Longitude", B: data.Longitude},
		{A: "Location", B: "https://www.openstreetmap.org/#map=10/" + fmt.Sprint(data.Latitude) + "/" + fmt.Sprint(data.Longitude)},
		{A: "European Union", B: data.IsEU},
		{A: "Postal Code", B: data.PostalCode},
		{A: "Calling Code", B: data.CallingCode},
		{A: "Capital", B: data.Capital},
		{A: "System Number (ASN)", B: data.Connection.SystemNumber},
		{A: "Organisation (ORG)", B: data.Connection.Organisation},
		{A: "Service Provider (ISP)", B: data.Connection.ServiceProvider},
		{A: "ISP Domain", B: data.Connection.ISPDomain},
		{A: "Timezone", B: data.Timezone.ID},
		{A: "Timezone Abbreviation", B: data.Timezone.Abbreviation},
		{A: "UTC", B: data.Timezone.UTC},
	}...))
}

func RetrieveCommand(args []string) {
	item := args[0]
	switch item {
	case "interfaces":
		devices, err := pcap.FindAllDevs()
		if err != nil {
			log.Error("Failed to retrieve network interfaces!")
			return
		}
		var interfaces []typing.Group
		for _, dev := range devices {
			interfaces = append(interfaces, typing.Group{A: dev.Description, B: dev.Name})
		}
		log.Print(log.GroupContainer(interfaces...))
	case "networks":
		output, err := exec.Command("cmd.exe", "/c", "netsh", "wlan", "show", "networks").CombinedOutput()
		if err != nil {
			log.Error(err.Error())
			return
		}
		log.Print(log.Container(networking.ScanNetworks(string(output))...))
	case "user":
		log.Print(color.Blue + Username + color.Gray + "@" + color.Reset + Device + color.Gray + " (" + runtime.GOOS + "-" + runtime.GOARCH + ")")
	case "version":
		log.Print(Version)
	case "uptime":
		log.Print(int(math.Trunc(time.Since(StartTime).Seconds())))
	case "paths":
		log.Print(log.GroupContainer([]typing.Group{
			{A: "Root Path", B: MainDir},
			{A: "Temp Path", B: TempDir},
			{A: "Download Path", B: DownloadDir},
			{A: "Config Path", B: ConfigDir},
			{A: "FUEL Path", B: FuelDir},
		}...))
	default:
		log.Error("No valid item to retrieve!")
	}
}

func SniffCommand(args []string) {
	interfaceName := args[0]
	interfaces, err := pcap.FindAllDevs()
	if err != nil {
		log.Error("Failed to retrieve network interfaces!")
		return
	}
	found := false
	for _, networkInterface := range interfaces {
		if networkInterface.Name == interfaceName {
			found = true
		}
	}
	if !found {
		log.Error("Desired interface was not found!")
		return
	}
	handle, err := pcap.OpenLive(interfaceName, 1600, false, pcap.BlockForever)
	if err != nil {
		log.Error("Failed to start network sniffer!")
		return
	}
	defer handle.Close()
	source := gopacket.NewPacketSource(handle, handle.LinkType())

	for packet := range source.Packets() {
		log.Print(packet.String())
	}
}

func FetchCommand(args []string) {
	url := args[0]

	split := strings.Split(url, "/")
	filename := split[len(split)-1]

	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Error("Failed to create new request instance.")
		return
	}

	request.Close = true

	downloadStartTime := time.Now()

	response, err := HttpClient.Do(request)
	if err != nil {
		log.Error("Failed to make request.")
		return
	}

	buffer := make([]byte, 4096)
	var downloaded int64
	var downloadedData []byte

	for {
		n, err := response.Body.Read(buffer)
		if err != nil && err != io.EOF {
			log.Error("Failed to read response body.")
			return
		}
		if n == 0 {
			break
		}

		downloaded += int64(n)
		downloadedData = append(downloadedData, buffer[:n]...)

		currentTime := time.Now()
		progress := float64(downloaded) / float64(response.ContentLength) * 100

		if currentTime.Sub(StartTime).Milliseconds() >= 250 {
			StartTime = currentTime
			msg := "Downloading... " + color.Blue + fmt.Sprint(int(progress)) + "%" + color.Reset
			log.PrintR(msg)
		}
	}
	err = response.Body.Close()
	if err != nil {
		log.Error("Failed to close body!")
		return
	}

	log.Print("Downloading... " + color.Blue + "100%" + color.Reset + utils.MultiString(" ", 20))
	log.Print(fmt.Sprint(time.Since(downloadStartTime)) + " elapsed!")

	err = os.WriteFile(DownloadDir+filename, downloadedData, os.ModePerm)
	if err != nil {
		log.Error("Failed to write data to file.")
		return
	}
}

func CdCommand(args []string) {
	if len(args) == 0 {
		dir, err := os.Getwd()
		if err != nil {
			log.Error(err.Error())
			return
		}
		log.Print(log.Container(GetPathAlias(dir) + color.Gray + " - " + color.Reset + "(" + dir + ")"))
		return
	}
	dir := args[0]
	err := os.Chdir(GetAliasPath(dir))
	if err != nil {
		log.Error(err.Error())
		return
	}
}

func LsCommand(_ []string) {
	dir, err := os.Getwd()
	if err != nil {
		log.Error(err.Error())
	}
	files, err := os.ReadDir(dir)
	if err != nil {
		log.Error(err.Error())
	}
	var folderList []string
	var fileList []string
	for _, file := range files {
		if file.IsDir() {
			folderList = append(folderList, file.Name())
		} else {
			fileList = append(fileList, file.Name())
		}
	}
	slices.Sort(folderList)
	slices.Sort(fileList)

	var combinedList []string
	for _, folder := range folderList {
		if strings.HasPrefix(folder, ".") {
			combinedList = append(combinedList, color.Gray+folder)
		} else {
			combinedList = append(combinedList, color.Reset+folder)
		}
	}
	for _, file := range fileList {
		if strings.HasPrefix(file, ".") {
			combinedList = append(combinedList, color.Gray+file)
		} else if strings.HasSuffix(file, ".exe") || strings.HasSuffix(file, ".bat") || strings.HasSuffix(file, ".cmd") || strings.HasSuffix(file, ".ps1") || strings.HasSuffix(file, ".msi") {
			combinedList = append(combinedList, color.Blue+file)
		} else {
			combinedList = append(combinedList, color.Reset+file)
		}
	}

	log.Print(log.Container(combinedList...))
}

func DirCommand(_ []string) {
	err := exec.Command("cmd.exe", "/c", "start", "explorer.exe", MainDir).Run()
	if err != nil {
		log.Error("Failed to start explorer process.")
		return
	}
}

func UpdateCommand(_ []string) {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "FyUTILS")
	if err != nil {
		log.Error("Failed to get latest release! " + err.Error())
		return
	}
	description := strings.Split(release.GetBody(), "\n")[0]
	if len(description) >= 118 {
		description = description[:115] + "..."
	}

	log.Print(log.Container(
		color.Red+Version+color.Gray+" -> "+color.Green+release.GetTagName(),
		description,
		color.Gray+release.GetHTMLURL(),
	))

	log.Print(color.Reset)

	if log.Confirm("Do you want to update to this version?") {
		output, err := utils.PowerShellRun("irm https://noahonfyre.github.io/FyUTILS/get.ps1 | iex")
		if err != nil {
			log.Error(err)
			return
		}
		log.Print(output)
		log.Input("Press enter to restart... ")
		os.Exit(0)
	} else {
		log.Print("Update cancelled!")
	}
}

func HelpCommand(_ []string) {
	var commandList []typing.Group
	for _, command := range Commands {
		var usages []string
		for _, argument := range command.Args {
			if argument.Required {
				usages = append(usages, "<"+argument.Identifier+">")
			} else {
				usages = append(usages, "["+argument.Identifier+"]")
			}
		}
		usage := " " + strings.Join(usages, " ")
		commandList = append(commandList, typing.Group{A: command.Name + usage, B: command.Short})
	}
	log.Print(log.GroupContainer(commandList...))
}

func ClearCommand(_ []string) {
	log.Clear()
	log.Menu()
}

func ExitCommand(_ []string) {
	log.Print("Shutting down FyUTILS...")
	os.Exit(0)
}
