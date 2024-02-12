package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"strings"
	"sync"
	"time"

	"github.com/google/go-github/github"
	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
	"github.com/noahzeisberg/gengine/color"
	"github.com/noahzeisberg/gengine/convert"
	"github.com/noahzeisberg/gengine/networking/requests"
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
		Error("Failed to connect to target: " + err.Error())
		return
	}

	for {
		randomBytes, err := RandomBytes(1024)
		if err != nil {
			Error("Cannot generate random bytes.")
			break
		}
		_, err = conn.Write(randomBytes)
		if err != nil {
			Error("Failed to send data to connection.")
			break
		}
		Print("Bytes successfully sent to " + color.Blue + conn.RemoteAddr().String())
	}
}

func PortscanCommand(args []string) {
	ip := args[0]
	lock := semaphore.NewWeighted(1024)

	results := make(chan int, 1024*64)

	var wg sync.WaitGroup
	Print("Scanning ports... This could take some time.")
	Print()

	for port := 0; port < 1024*64; port++ {
		wg.Add(1)
		err := lock.Acquire(context.TODO(), 1)
		if err != nil {
			Error(err.Error())
			return
		}
		go func(port int) {
			defer lock.Release(1)
			defer wg.Done()
			ScanPort(ip, port, results)
		}(port)
	}

	close(results)
	wg.Wait()

	var openPortGroups []Group
	for port := range results {
		openPortGroups = append(openPortGroups, Group{
			A: fmt.Sprint(port),
			B: GetPortService(port),
		})
	}

	Print(GroupContainer(openPortGroups...))
}

func WhoisCommand(args []string) {
	target := args[0]
	var data AddressInformation
	body := requests.Get("https://ipwho.is/" + target)

	err := json.Unmarshal(body, &data)
	if err != nil {
		Error("Failed to parse JSON.")
		return
	}

	Print("WHOIS Report for " + color.Blue + data.IP)
	Print()
	Print(GroupContainer([]Group{
		{A: "Target", B: data.IP},
		{A: "Address Type", B: data.Type},
		{A: "Continent", B: data.Continent + " (" + data.ContinentCode + ")"},
		{A: "Country", B: data.Country + " (" + data.CountryCode + ")"},
		{A: "Region", B: data.Country + " (" + data.RegionCode + ")"},
		{A: "City", B: data.Country},
		{A: "Latitude", B: data.Latitude},
		{A: "Longitude", B: data.Longitude},
		{A: "Location", B: "https://www.openstreetmap.org/#map=10/" + convert.FormatFloat(data.Latitude) + "/" + convert.FormatFloat(data.Longitude)},
		{A: "European Union", B: data.IsEU},
		{A: "Postal Code", B: data.PostalCode},
		{A: "Calling Code", B: data.CallingCode},
		{A: "Capital", B: data.Capital},
		{A: "", B: ""},
		{A: "System Number (ASN)", B: data.Connection.SystemNumber},
		{A: "Organisation (ORG)", B: data.Connection.Organisation},
		{A: "Service Provider (ISP)", B: data.Connection.ServiceProvider},
		{A: "ISP Domain", B: data.Connection.ISPDomain},
		{A: "", B: ""},
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
			Error("Failed to retrieve network interfaces!")
			return
		}
		var interfaces []Group
		for _, dev := range devices {
			interfaces = append(interfaces, Group{A: dev.Description, B: dev.Name})
		}
		Print(GroupContainer(interfaces...))
	case "path":
		pathVar := os.Getenv("PATH")
		paths := strings.Split(pathVar, string(os.PathListSeparator))
		Print(Container(paths...))
	case "networks":
		output, err := exec.Command("cmd.exe", "/c", "netsh", "wlan", "show", "networks").CombinedOutput()
		if err != nil {
			Error(err.Error())
			return
		}
		Print(Container(ScanNetworks(string(output))...))
	default:
		Error("No valid item to retrieve!")
	}
}

func SniffCommand(args []string) {
	interfaceName := args[0]
	interfaces, err := pcap.FindAllDevs()
	if err != nil {
		Error("Failed to retrieve network interfaces!")
		return
	}
	found := false
	for _, networkInterface := range interfaces {
		if networkInterface.Name == interfaceName {
			found = true
		}
	}
	if !found {
		Error("Desired interface was not found!")
		return
	}
	handle, err := pcap.OpenLive(interfaceName, 1600, false, pcap.BlockForever)
	if err != nil {
		Error("Failed to start network sniffer!")
		return
	}
	defer handle.Close()
	source := gopacket.NewPacketSource(handle, handle.LinkType())

	for packet := range source.Packets() {
		Print(packet.String())
	}
}

func FetchCommand(args []string) {
	url := args[0]

	split := strings.Split(url, "/")
	filename := split[len(split)-1]

	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		Error("Failed to create new request instance.")
		return
	}

	request.Close = true

	downloadStartTime := time.Now()

	response, err := httpClient.Do(request)
	if err != nil {
		Error("Failed to make request.")
		return
	}

	buffer := make([]byte, 4096)
	var downloaded int64
	var downloadedData []byte

	for {
		n, err := response.Body.Read(buffer)
		if err != nil && err != io.EOF {
			Error("Failed to read response body.")
			return
		}
		if n == 0 {
			break
		}

		downloaded += int64(n)
		downloadedData = append(downloadedData, buffer[:n]...)

		currentTime := time.Now()
		progress := float64(downloaded) / float64(response.ContentLength) * 100

		if currentTime.Sub(startTime).Milliseconds() >= 250 {
			startTime = currentTime
			msg := "Downloading... " + color.Blue + convert.FormatInt(int(progress)) + "%" + color.Reset
			PrintR(msg + "\r")
		}
	}
	err = response.Body.Close()
	if err != nil {
		Error("Failed to close body!")
		return
	}

	Print("Downloading... " + color.Blue + "100%" + color.Reset + MultiString(" ", 20))
	Print(fmt.Sprint(time.Since(downloadStartTime)), "elapsed!")

	err = os.WriteFile(downloadDir+filename, downloadedData, os.ModePerm)
	if err != nil {
		Error("Failed to write data to file.")
		return
	}
}

func FuelCommand(args []string) {
	action := args[0]

	if len(args) == 1 {
		switch action {
		case "list":
			directoryEntries, err := os.ReadDir(fuelDir)
			if err != nil {
				return
			}

			var fuels []Group

			for _, entry := range directoryEntries {
				fileInfo, err := entry.Info()
				if err != nil {
					return
				}
				fuels = append(fuels, Group{
					A: strings.ReplaceAll(fileInfo.Name(), ".", "/"),
					B: fileInfo.Size(),
				})
			}

			Print(GroupContainer(fuels...))
		}
		return
	}
	pkg := args[1]
	switch action {
	case "get", "install", "fetch":
		FetchRepositoryContent(pkg, "", time.Now())
	case "remove", "delete", "uninstall":
		owner, repository := ParseRepository(pkg)

		if Confirm("Do you really want to remove this package?") {
			err := os.RemoveAll(fuelDir + owner + "." + repository)
			if err != nil {
				Error(err.Error())
				return
			}
			Print("Removed package " + color.Blue + owner + "/" + repository + color.Reset + "!")
		} else {
		}
	case "run":
		owner, repository := ParseRepository(pkg)
		packageDirectory := fuelDir + owner + "." + repository + "\\"

		cmd := exec.Command("cmd.exe", "/c", packageDirectory+"main")

		var stdBuffer bytes.Buffer
		mw := io.MultiWriter(os.Stdout, &stdBuffer)

		cmd.Stdout = mw
		cmd.Stderr = mw
		cmd.Stdin = os.Stdin

		err := cmd.Run()
		if err != nil {
			Error(err.Error())
			return
		}
	}
}

func CdCommand(args []string) {
	if len(args) == 0 {
		dir, err := os.Getwd()
		if err != nil {
			Error(err.Error())
			return
		}
		Print(Container(GetPathAlias(dir) + color.Gray + " - " + color.Reset + "(" + dir + ")"))
		return
	}
	dir := args[0]
	err := os.Chdir(GetAliasPath(dir))
	if err != nil {
		Error(err.Error())
		return
	}
}

func LsCommand(_ []string) {
	dir, err := os.Getwd()
	if err != nil {
		Error(err.Error())
	}
	files, err := os.ReadDir(dir)
	if err != nil {
		Error(err.Error())
	}
	var fileList []string
	for _, file := range files {
		if file.IsDir() {
			fileList = append(fileList, "/"+file.Name())
		} else if strings.HasPrefix(file.Name(), ".") {
			fileList = append(fileList, color.Gray+file.Name())
		} else {
			fileList = append(fileList, file.Name())
		}
	}
	Print(Container(fileList...))
}

func DirCommand(_ []string) {
	err := exec.Command("cmd.exe", "/c", "start", "explorer.exe", mainDir).Run()
	if err != nil {
		Error("Failed to start explorer process.")
		return
	}
}

func UpdateCommand(_ []string) {
	Print(GroupContainer([]Group{
		{A: "Version Diff:", B: color.Red + version + color.Gray + " -> " + color.Green + newestRelease.GetTagName()},
		{A: "Short:", B: color.Reset + strings.Split(newestRelease.GetBody(), "\n")[0]},
		{A: "GitHub Release:", B: newestRelease.GetHTMLURL()},
	}...))

	Print(color.Reset)

	if Confirm("Do you want to update to this version?") {
		PowerShellRun("irm https://noahonfyre.github.io/FyUTILS/get.ps1 | iex")
		time.Sleep(time.Second)
		os.Exit(0)
	} else {
		Print("Update cancelled!")
	}
}

func HelpCommand(_ []string) {
	var commandList []Group
	for _, command := range commands {
		var usages []string
		for _, argument := range command.Args {
			if argument.Required {
				usages = append(usages, "<"+argument.Identifier+">")
			} else {
				usages = append(usages, "["+argument.Identifier+"]")
			}
		}
		usage := strings.Join(usages, " ")
		commandList = append(commandList, Group{
			A: command.Name + " " + usage,
			B: command.Short,
		})
	}
	Print(GroupContainer(commandList...))
}

func SysCommand(_ []string) {
	Print(GroupContainer([]Group{
		{A: "Username", B: username},
		{A: "Device", B: device},
		{A: "Operating System", B: runtime.GOOS},
		{A: "", B: ""},
		{A: "FyUTILS", B: version},
		{A: "Uptime", B: time.Since(startTime)},
		{A: "Root Path", B: mainDir},
		{A: "Temp Path", B: tempDir},
		{A: "Download Path", B: downloadDir},
		{A: "Config Path", B: configDir},
		{A: "FUEL Path", B: fuelDir},
	}...))
}

func ClearCommand(_ []string) {
	Clear()
	Menu()
}

func ExitCommand(_ []string) {
	Print("Shutting down FyUTILS...")
	os.Exit(0)
}
