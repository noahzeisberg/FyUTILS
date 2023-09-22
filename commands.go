package main

import (
	"encoding/json"
	"io"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/mnogu/go-calculator"
)

func RegisterCommand(name string, description string, args []string, runnable func([]string)) {
	arguments := Args{
		Count: len(args),
		Get:   args,
	}
	commands = append(commands, Command{
		Name:        name,
		Description: description,
		Args:        arguments,
		Run:         runnable,
	})

	Print(Prefix(0) + "Successfully registered command \"" + name + "\" with " + strconv.Itoa(len(args)) + " arguments.")
}

func FloodCommand(args []string) {
	host := args[0]
	port := args[1]

	conn, err := net.Dial("tcp", net.JoinHostPort(host, port))

	if err != nil {
		Print(Prefix(2) + "Failed to connect to target: " + err.Error())
	}

	i := 0

	for {
		i++
		bytes, err := RandomBytes(1024)

		if err != nil {
			Print(Prefix(2) + "Cannot generate random bytes.")
		}

		conn.Write(bytes)
		PrintR(Prefix(0) + "Bytes successfully sent to " + conn.RemoteAddr().String() + Gray + " (" + strconv.Itoa(i) + ")" + "\r")
	}
}

func PortscanCommand(args []string) {
	addr := args[0]
	ports := 65536

	wg := sync.WaitGroup{}

	Print(Prefix(0) + "Scanning ports... This may take a while.")
	for port := 1; port < ports; port++ {
		wg.Add(1)
		go func(port int) {
			ScanPort(addr, port, 5*time.Second)
			wg.Done()
		}(port)
	}
	wg.Wait()
}

func GatherCommand(args []string) {
	addr := args[0]

	data := AddressInformation{}

	res, err := http.Get("https://ipwho.is/" + addr)

	if err != nil {
		Print(Prefix(2) + "API requests failed!")
	}

	defer res.Body.Close()
	body, err := io.ReadAll(res.Body)

	if err != nil {
		Print(Prefix(2) + "Reading response body failed!")
	}

	json.Unmarshal(body, &data)

	Print(Prefix(0) + "Gathering report for " + Blue + data.IP)
	Print(Prefix(0) + "Addess type" + Gray + ": " + Blue + data.Type)
	Print(Prefix(0) + "Continent" + Gray + ": " + Blue + data.Continent + Gray + "(" + data.ContinentCode + ")")
	Print(Prefix(0) + "Country" + Gray + ": " + Blue + data.Country + Gray + "(" + data.CountryCode + ")")
	Print(Prefix(0) + "Region" + Gray + ": " + Blue + data.Region + Gray + "(" + data.RegionCode + ")")
	Print(Prefix(0) + "City" + Gray + ": " + Blue + data.City)
	Print(Prefix(0) + "Latitude" + Gray + ": " + Blue + strconv.FormatFloat(data.Latitude, 'f', -1, 64))
	Print(Prefix(0) + "Longitude" + Gray + ": " + Blue + strconv.FormatFloat(data.Longitude, 'f', -1, 64))
	Print(Prefix(0) + "Location" + Gray + ": " + Blue + "https://www.openstreetmap.org/#map=10/" + strconv.FormatFloat(data.Latitude, 'f', -1, 64) + "/" + strconv.FormatFloat(data.Longitude, 'f', -1, 64))
	Print(Prefix(0) + "Is EU country" + Gray + ": " + Blue + strconv.FormatBool(data.IsEU))
	Print(Prefix(0) + "Postal code" + Gray + ": " + Blue + data.PostalCode)
	Print(Prefix(0) + "Calling code" + Gray + ": " + Blue + data.CallingCode)
	Print(Prefix(0) + "Capital city" + Gray + ": " + Blue + data.Capital)
	Print(Prefix(0) + "System number (ASN)" + Gray + ": " + Blue + strconv.Itoa(data.Connection.SystemNumber))
	Print(Prefix(0) + "Organisation (ORG)" + Gray + ": " + Blue + data.Connection.Organisation)
	Print(Prefix(0) + "Internet Service Provider (ISP)" + Gray + ": " + Blue + data.Connection.ServiceProvider)
	Print(Prefix(0) + "ISP domain" + Gray + ": " + Blue + data.Connection.ISPDomain)
	Print(Prefix(0) + "Timezone" + Gray + ": " + Blue + data.Timezone.ID)
	Print(Prefix(0) + "Timezone Abbreviation" + Gray + ": " + Blue + data.Timezone.Abbreviation)
	Print(Prefix(0) + "UTC" + Gray + ": " + Blue + data.Timezone.UTC)
}

func ClearCommand(args []string) {
	Print("\033[H\033[2J")
	MainMenu()
}

func HelpCommand(args []string) {
	for _, cmd := range commands {
		argstring := ""
		for _, argument := range cmd.Args.Get {
			argstring = argstring + "<" + argument + "> "
		}
		Print(Prefix(0) + Blue + strings.ToUpper(cmd.Name) + Gray + " - " + Reset + cmd.Description + Gray + " - " + Blue + argstring + Gray + "(" + strconv.Itoa(cmd.Args.Count) + ")")
	}
}

func CalculatorCommand(args []string) {
	final, err := calculator.Calculate(RInput(Prefix(0) + "Calculate: " + Blue))

	if err != nil {
		Print(Prefix(2) + "Bad syntax.")
		return
	}

	Print(Prefix(0) + "= " + strconv.FormatFloat(final, 'f', -1, 64))
}

func TestCommand(args []string) {
	Print(Prefix(0) + "Test output.")
	time.Sleep(500 * time.Millisecond)
	Print(Prefix(1) + "Test warning.")
	time.Sleep(500 * time.Millisecond)
	Print(Prefix(2) + "Test error.")
}

func UpdateCommand(args []string) {
	Print(Prefix(0) + "Updating instance...")
	DownloadNewestVersion()
	Print(Prefix(0) + "Please restart the program to apply the update.")
	StopRPC()
	os.Exit(0)
}

func ExitCommand(args []string) {
	Print(Prefix(0) + "Exiting program...")
	StopRPC()
	os.Exit(0)
}
