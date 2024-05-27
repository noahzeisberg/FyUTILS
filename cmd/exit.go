package cmd

import (
	"fyutils/log"
	"os"
)

func Exit(args []string) {
	log.Print("Exiting...")
	os.Exit(0)
}
