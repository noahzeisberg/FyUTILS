package main

import (
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/logging"
	"net"
	"sync"
)

func ScanPort(target string, port int, wg *sync.WaitGroup) {
	defer wg.Done()
	address := net.JoinHostPort(target, convert.FormatInt(port))
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return
	}
	defer conn.Close()
	logging.Log("Port", port, "is open!")
}
