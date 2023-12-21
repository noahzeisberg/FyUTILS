package main

import (
	"context"
	"encoding/json"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/logging"
	"github.com/NoahOnFyre/gengine/networking/requests"
	"github.com/google/go-github/github"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"sync"
)

var (
	githubClient = github.NewClient(nil)
)

func FloodCommand(args []string) {
	host := args[0]
	port := args[1]

	conn, err := net.Dial("tcp", net.JoinHostPort(host, port))

	if err != nil {
		Error("Failed to connect to target: " + err.Error())
		return
	}

	i := 0

	for {
		i++
		bytes, err := RandomBytes(1024)

		if err != nil {
			logging.Error("Cannot generate random bytes.")
			break
		}

		_, err = conn.Write(bytes)
		if err != nil {
			logging.Error("Failed to send data to connection.")
			break
		}
		Print("Bytes successfully sent to", conn.RemoteAddr().String()+color.Gray, "("+strconv.Itoa(i)+")")
	}
}

// PortscanCommand Needs a better solution for not crashing, when too many ports are scanned at once.
// This is currently fixed by using a limit of 1024 ports to scan.
func PortscanCommand(args []string) {
	addr := args[0]
	var wg sync.WaitGroup

	Print("Scanning ports...")

	for port := 1; port <= 1024; port++ {
		wg.Add(1)
		go ScanPort(addr, port, &wg)
	}
	wg.Wait()

	Print("Ports successfully scanned!")
}

func GatherCommand(args []string) {
	addr := args[0]

	data := AddressInformation{}

	body := requests.Get("https://ipwho.is/" + addr)

	err := json.Unmarshal(body, &data)
	if err != nil {
		Error("Failed to parse data.")
		return
	}

	Print("Gathering report for " + color.Blue + data.IP)
	Print("Address type" + color.Gray + ": " + color.Blue + data.Type)
	Print("Continent" + color.Gray + ": " + color.Blue + data.Continent + color.Gray + " (" + data.ContinentCode + ")")
	Print("Country" + color.Gray + ": " + color.Blue + data.Country + color.Gray + " (" + data.CountryCode + ")")
	Print("Region" + color.Gray + ": " + color.Blue + data.Region + color.Gray + " (" + data.RegionCode + ")")
	Print("City" + color.Gray + ": " + color.Blue + data.City)
	Print("Latitude" + color.Gray + ": " + color.Blue + convert.FormatFloat(data.Latitude))
	Print("Longitude" + color.Gray + ": " + color.Blue + convert.FormatFloat(data.Longitude))
	Print("Location" + color.Gray + ": " + color.Blue + "https://www.openstreetmap.org/#map=10/" + convert.FormatFloat(data.Latitude) + "/" + convert.FormatFloat(data.Longitude))
	Print("Is EU country" + color.Gray + ": " + color.Blue + convert.FormatBool(data.IsEU))
	Print("Postal code" + color.Gray + ": " + color.Blue + data.PostalCode)
	Print("Calling code" + color.Gray + ": " + color.Blue + data.CallingCode)
	Print("Capital city" + color.Gray + ": " + color.Blue + data.Capital)
	Print()
	Print("System number (ASN)" + color.Gray + ": " + color.Blue + convert.FormatInt(data.Connection.SystemNumber))
	Print("Organisation (ORG)" + color.Gray + ": " + color.Blue + data.Connection.Organisation)
	Print("Internet Service Provider (ISP)" + color.Gray + ": " + color.Blue + data.Connection.ServiceProvider)
	Print("ISP domain" + color.Gray + ": " + color.Blue + data.Connection.ISPDomain)
	Print()
	Print("Timezone" + color.Gray + ": " + color.Blue + data.Timezone.ID)
	Print("Timezone Abbreviation" + color.Gray + ": " + color.Blue + data.Timezone.Abbreviation)
	Print("UTC" + color.Gray + ": " + color.Blue + data.Timezone.UTC)
}

func CdCommand(args []string) {
	dir := args[0]
	err := os.Chdir(dir)
	if err != nil {
		logging.Error(err)
		return
	}
}

func LsCommand(args []string) {
	dir, err := os.Getwd()
	if err != nil {
		Error(err)
	}
	files, err := os.ReadDir(dir)
	if err != nil {
		Error(err)
	}
	for _, file := range files {
		if file.IsDir() {
			Print(color.Blue + "/" + file.Name())
		} else if strings.HasPrefix(file.Name(), ".") {
			Print(color.Gray + file.Name())
		} else {
			Print(file.Name())
		}
	}
}

func UpdateCommand(args []string) {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahonfyre", "FyUTILS")
	if err != nil {
		Error("Failed to fetch version information from GitHub.")
		return
	}

	Print("Version Diff: " + color.Red + version + color.Gray + " -> " + color.Green + release.GetTagName())
	Print()
	Print("Target Version: " + color.Blue + release.GetTagName() + color.Gray + " (" + release.GetNodeID() + ")")
	Print("Description: " + color.Gray + strings.Split(release.GetBody(), "\n")[0])
	Print("Uploaded:"+color.Blue, release.GetPublishedAt().Month(), release.GetPublishedAt().Day(), release.GetPublishedAt().Year(), color.Gray+" - by @noahonfyre")
	Print()
	for {
		confirmation := Input(logging.Prefix(0) + " " + "Do you want to update to this version? " + color.Gray + "(yes/no): " + color.Reset)
		if confirmation == "yes" {
			break
		} else if confirmation == "no" {
			return
		} else {
			continue
		}
	}
	err = exec.Command("powershell.exe", "/c", "Invoke-Expression(Invoke-RestMethod(https://raw.githubusercontent.com/noahonfyre/FyUTILS/master/get.ps1))").Run()
	if err != nil {
		Error("Failed to update.")
		return
	}
	os.Exit(0)
}

func HelpCommand(args []string) {
	Print(color.Blue + "    ______      __  ______________   _____")
	Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\")
	Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /")
	Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/")
	Print(color.Blue + "       __/ /")
	Print(color.Blue + "     /____/" + color.Reset + "   Version: " + version)
	Print()
	Print(color.Gray + "┌" + MultiString("─", 120-1))
	for _, command := range commands {
		var usages []string
		for _, argument := range command.Args.Get {
			usages = append(usages, "<"+argument+">")
		}
		usage := strings.Join(usages, " ")
		Print(color.Gray + "│ " + color.Blue + SpacingRowColorChange(command.Name+color.Gray+" "+usage, color.Gray, 24) + color.Reset + command.Description)
	}
	Print(color.Gray + "└" + MultiString("─", 120-1))
	Print()
	Print(color.Gray + "\U000F0219" + color.Reset + " Documentation: " + color.Blue + "https://github.com/noahonfyre/FyUTILS")
	Print()
	Print(color.Gray + "\U000F02D6" + color.Reset + " Submit Issue: " + color.Blue + "https://github.com/noahonfyre/FyUTILS/issues/new")
	Print()
	Print(color.Gray + "\uF407" + color.Reset + " View Pulls: " + color.Blue + "https://github.com/noahonfyre/FyUTILS/pulls")
}

func ClearCommand(args []string) {
	Clear()
	Menu()
}

func ExitCommand(args []string) {
	Print("Shutting down FyUTILS...")
	os.Exit(0)
}
