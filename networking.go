package main

import (
	"net"
	"strconv"
	"strings"
	"time"
)

func ScanPort(addr string, port int, timeout time.Duration) bool {
	conn, err := net.DialTimeout("tcp", net.JoinHostPort(addr, strconv.Itoa(port)), timeout)

	if err != nil {
		if strings.Contains(err.Error(), "too many open files") {
			Print(Prefix(1) + "Timeout exceed")
			time.Sleep(timeout)
			return ScanPort(addr, port, timeout)
		} else {
			return false
		}
	}

	conn.Close()
	return true
}
