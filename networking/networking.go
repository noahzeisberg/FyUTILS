package networking

import (
	"fmt"
	"github.com/noahzeisberg/FyUTILS/log"
	"net"
	"strings"
	"time"
)

func ScanPort(target string, port int, results chan<- int) {
	log.PrintR("Scanning: ", port, "...")
	address := net.JoinHostPort(target, fmt.Sprint(port))
	conn, err := net.DialTimeout("tcp", address, time.Millisecond*500)
	if err != nil {
		return
	}
	err = conn.Close()
	if err != nil {
		log.Error(err.Error())
		return
	}
	results <- port
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
