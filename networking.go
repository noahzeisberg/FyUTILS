package main

import (
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"net"
	"strings"
	"sync"
)

func ScanPort(target string, port int, wg *sync.WaitGroup) {
	defer wg.Done()
	address := net.JoinHostPort(target, convert.FormatInt(port))
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return
	}
	defer func(conn net.Conn) {
		err := conn.Close()
		if err != nil {

		}
	}(conn)
	Print("Port " + color.Blue + convert.FormatInt(port) + color.Reset + " is open!")
}

func ScanNetworks(data string) []string {
	var networks []string
	for _, line := range strings.Split(data, "\n") {
		if strings.Contains(line, "SSID") {
			trimSpace := strings.TrimSpace(strings.Split(line, ":")[1])
			if trimSpace != "" {
				networks = append(networks, trimSpace)
			} else {
				networks = append(networks, "Unknown Network")
			}
		}
	}
	return networks
}
