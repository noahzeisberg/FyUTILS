package main

import (
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/logging"
	"net"
	"sync"
	"time"
)

func ScanPort(target string, port int, wg *sync.WaitGroup) {
	defer wg.Done()
	address := net.JoinHostPort(target, convert.FormatInt(port))
	conn, err := net.DialTimeout("tcp", address, time.Second*10)
	if err != nil {
		return
	}
	defer conn.Close()
	logging.Log("Port", port, "is open!")
}
