package main

import (
	"fyutils/log"
	"fyutils/parser"
	"fyutils/registration"
)

func main() {
	registration.RegisterCommands()

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
