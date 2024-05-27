package cmd

import (
	"fyutils/log"
	"os"
	"strconv"
)

func Exit(args []string) {
	log.Print("Exiting...")

	if len(args) == 0 {
		os.Exit(0)
	}

	exitCode, err := strconv.Atoi(args[0])
	if err != nil {
		log.Error(err)
		os.Exit(1)
	}
	os.Exit(exitCode)
}
