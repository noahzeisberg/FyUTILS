package main

import (
	"fyutils/log"
	"fyutils/parser"
)

func main() {
	for {
		input := log.Input("Enter command: ")
		cmdName, args := parser.ParseInput(input)
		command, err := parser.GetCommand(cmdName)
		if err != nil {
			log.Error(err)
		}
		command.Run(&command, args)
	}
}
