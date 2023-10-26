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
		logging.Error("Failed to connect to target: " + err.Error())
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
		logging.Log("Bytes successfully sent to", conn.RemoteAddr().String()+color.Gray, "("+strconv.Itoa(i)+")")
	}
}

// PortscanCommand Needs a better solution for not crashing, when too many ports are scanned at once.
// This is currently fixed by using a limit of 1024 ports to scan.
func PortscanCommand(args []string) {
	addr := args[0]
	var wg sync.WaitGroup

	logging.Log("Scanning ports...")

	for port := 1; port <= 1024; port++ {
		wg.Add(1)
		go ScanPort(addr, port, &wg)
	}
	wg.Wait()

	logging.Log("Ports successfully scanned!")
}

func GatherCommand(args []string) {
	addr := args[0]

	data := AddressInformation{}

	body := requests.Get("https://ipwho.is/" + addr)

	err := json.Unmarshal(body, &data)
	if err != nil {
		logging.Error("Failed to parse data.")
		return
	}

	logging.Log("Gathering report for " + color.Blue + data.IP)
	logging.Log("Address type" + color.Gray + ": " + color.Blue + data.Type)
	logging.Log("Continent" + color.Gray + ": " + color.Blue + data.Continent + color.Gray + " (" + data.ContinentCode + ")")
	logging.Log("Country" + color.Gray + ": " + color.Blue + data.Country + color.Gray + " (" + data.CountryCode + ")")
	logging.Log("Region" + color.Gray + ": " + color.Blue + data.Region + color.Gray + " (" + data.RegionCode + ")")
	logging.Log("City" + color.Gray + ": " + color.Blue + data.City)
	logging.Log("Latitude" + color.Gray + ": " + color.Blue + convert.FormatFloat(data.Latitude))
	logging.Log("Longitude" + color.Gray + ": " + color.Blue + convert.FormatFloat(data.Longitude))
	logging.Log("Location" + color.Gray + ": " + color.Blue + "https://www.openstreetmap.org/#map=10/" + convert.FormatFloat(data.Latitude) + "/" + convert.FormatFloat(data.Longitude))
	logging.Log("Is EU country" + color.Gray + ": " + color.Blue + convert.FormatBool(data.IsEU))
	logging.Log("Postal code" + color.Gray + ": " + color.Blue + data.PostalCode)
	logging.Log("Calling code" + color.Gray + ": " + color.Blue + data.CallingCode)
	logging.Log("Capital city" + color.Gray + ": " + color.Blue + data.Capital)
	logging.Log()
	logging.Log("System number (ASN)" + color.Gray + ": " + color.Blue + convert.FormatInt(data.Connection.SystemNumber))
	logging.Log("Organisation (ORG)" + color.Gray + ": " + color.Blue + data.Connection.Organisation)
	logging.Log("Internet Service Provider (ISP)" + color.Gray + ": " + color.Blue + data.Connection.ServiceProvider)
	logging.Log("ISP domain" + color.Gray + ": " + color.Blue + data.Connection.ISPDomain)
	logging.Log()
	logging.Log("Timezone" + color.Gray + ": " + color.Blue + data.Timezone.ID)
	logging.Log("Timezone Abbreviation" + color.Gray + ": " + color.Blue + data.Timezone.Abbreviation)
	logging.Log("UTC" + color.Gray + ": " + color.Blue + data.Timezone.UTC)
}

func UpdateCommand(args []string) {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
	if err != nil {
		logging.Error("Failed to fetch version information from GitHub.")
		return
	}

	logging.Log("Version Diff: " + color.Red + version + color.Gray + " -> " + color.Green + release.GetTagName())
	logging.Print()
	logging.Log("Target Version: " + color.Blue + release.GetTagName() + color.Gray + " (" + release.GetNodeID() + ")")
	logging.Log("Description: " + color.Gray + strings.Split(release.GetBody(), "\n")[0])
	logging.Log("Uploaded:"+color.Blue, release.GetPublishedAt().Month(), release.GetPublishedAt().Day(), release.GetPublishedAt().Year(), color.Gray+" - by @noahonfyre")
	logging.Print()
	for {
		confirmation := logging.Input(logging.Prefix(0) + " " + "Do you want to update to this version? " + color.Gray + "(yes/no): " + color.Reset)
		if confirmation == "yes" {
			break
		} else if confirmation == "no" {
			return
		} else {
			continue
		}
	}
	logging.Log("Starting updater...")
	exec.Command("cmd.exe", "/c", "start", "updater.exe")
	os.Exit(0)
}

func HelpCommand(args []string) {
	for _, command := range commands {
		s := ""
		for _, argument := range command.Args.Get {
			s += "<" + argument + "> "
		}
		logging.Log(color.Blue + strings.ToUpper(command.Name) + color.Gray + ": " + color.Reset + command.Description + color.Gray + " - " + color.Blue + s)
	}
}

func ClearCommand(args []string) {
	logging.Clear()
	Menu()
}

func ExitCommand(args []string) {
	logging.Log("Shutting down FyUTILS...")
	os.Exit(0)
}
