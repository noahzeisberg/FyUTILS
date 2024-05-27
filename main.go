package main

import (
	"fyutils/cmd"
	"fyutils/log"
	"fyutils/parser"
	"fyutils/registration"
)

func main() {
	registration.Register("info", "<text> [number]", "Test command used for debugging.", cmd.Info)
	for {
		input := log.Input("Enter command: ")
		cmdName, args := parser.ParseInput(input)
		command, err := parser.GetCommand(cmdName)
		if err != nil {
			log.Error("Command not found!")
			continue
		}
		command.Run(args)
	}
}
