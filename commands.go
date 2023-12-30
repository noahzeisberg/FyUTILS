package main

import (
	"context"
	"encoding/json"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/networking/requests"
	"github.com/google/go-github/github"
	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
	"net"
	"os"
	"strings"
	"sync"
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

	i := 0

	for {
		i++
		bytes, err := RandomBytes(1024)

		if err != nil {
			Error("Cannot generate random bytes.")
			break
		}

		_, err = conn.Write(bytes)
		if err != nil {
			Error("Failed to send data to connection.")
			break
		}

		Print("Bytes successfully sent to " + color.Blue + conn.RemoteAddr().String() + color.Gray + " (" + convert.FormatInt(i) + ")")
	}
}

func PortscanCommand(args []string) {
	ip := args[0]
	var wg sync.WaitGroup
	Print("Scanning ports...")
	for port := 1; port <= 1024*64; port++ {
		wg.Add(1)
		go ScanPort(ip, port, &wg)
	}
	wg.Wait()

	Print("Ports successfully scanned!")
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

	Print("Gathering Report for " + color.Blue + data.IP)
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
	case "":

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

func CdCommand(args []string) {
	dir := args[0]
	err := os.Chdir(dir)
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

func UpdateCommand(_ []string) {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahonfyre", "FyUTILS")
	if err != nil {
		Error("Failed to fetch version information from GitHub.")
		return
	}

	Print(Container(
		"Version Diff"+color.Gray+": "+color.Red+version+color.Gray+" -> "+color.Green+release.GetTagName(),
		"Target Version"+color.Gray+": "+color.Blue+release.GetTagName()+color.Gray+" ("+release.GetNodeID()+")",
		"Description"+color.Gray+": "+color.Reset+strings.Split(release.GetBody(), "\n")[0],
		"URL"+color.Gray+": "+color.Blue+release.GetHTMLURL(),
	))
	Print()

	if Confirm("Do you want to update to this version?") {
		PowerShellRun("Invoke-RestMethod https://raw.githubusercontent.com/noahonfyre/FyUTILS/master/get.ps1 | Invoke-Expression")
		if err != nil {
			Error("Failed to update.", err.Error())
			return
		}
	} else {
		Print("Update cancelled!")
	}
}

func HelpCommand(_ []string) {
	var commandList []Group
	for _, command := range commands {
		var usages []string
		for _, argument := range command.Args.Usage {
			usages = append(usages, "<"+argument+">")
		}
		usage := strings.Join(usages, " ")
		commandList = append(commandList, Group{
			A: command.Name + " " + usage,
			B: command.Description,
		})
	}
	Print(GroupContainer(commandList...))
}

func ClearCommand(_ []string) {
	Clear()
	Menu()
}

func ExitCommand(_ []string) {
	Print("Shutting down FyUTILS...")
	os.Exit(0)
}
