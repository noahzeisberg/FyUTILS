package cmd

import (
	"fyutils/log"
)

func Info(args []string) {
	log.Print("Test")
	for _, arg := range args {
		log.Print(arg)
	}
}
