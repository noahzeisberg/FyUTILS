package main

import (
	"encoding/json"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/logging"
	"io"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"
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

func PortscanCommand(args []string) {
	addr := args[0]
	maxPort, err := strconv.Atoi(args[1])
	if err != nil {
		logging.Error("Failed to parse maxPort parameter!")
		return
	}
	var wg sync.WaitGroup

	logging.Log("Scanning ports...")
	logging.Warn("This can take a few minutes and can push your CPU utilization up to 100% for a few minutes.")

	for port := 1; port <= maxPort; port++ {
		wg.Add(1)
		go ScanPort(addr, port, &wg)
	}
	wg.Wait()

	logging.Log("Ports successfully scanned!")
}

func GatherCommand(args []string) {
	addr := args[0]

	data := AddressInformation{}

	res, err := http.Get("https://ipwho.is/" + addr)

	if err != nil {
		logging.Error("API requests failed!")
	}

	defer res.Body.Close()
	body, err := io.ReadAll(res.Body)

	if err != nil {
		logging.Error("Reading response body failed!")
	}

	err = json.Unmarshal(body, &data)
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
	Menu()
}

func ExitCommand(args []string) {
	logging.Log("Shutting down FyUTILS...")
	os.Exit(0)
}
