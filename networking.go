package main

import (
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"net"
	"strings"
	"time"
)

func ScanPort(target string, port int) {
	address := net.JoinHostPort(target, convert.FormatInt(port))
	conn, err := net.DialTimeout("tcp", address, time.Millisecond*250)
	if err != nil {
		return
	}
	defer func(conn net.Conn) {
		err = conn.Close()
		if err != nil {
			Error(err.Error())
			return
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
