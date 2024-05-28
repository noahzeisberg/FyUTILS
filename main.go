package main

import (
	"fyutils/color"
	"fyutils/log"
	"fyutils/parser"
	"fyutils/registration"
)

func main() {
	log.Print(color.Blue + "    ______      __  ______________   _____")
	log.Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	log.Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\")
	log.Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /")
	log.Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/")
	log.Print(color.Blue + "       __/ /")
	log.Print(color.Blue + "     /____/")
	log.Print()

	registration.RegisterCommands()

	for {
		input := log.Input(color.Gray + "┌──(" + color.Blue + "noah" + color.Gray + "@" + color.Reset + "DESKTOP" + color.Gray + ")─[" + color.Reset + "~" + color.Gray + "]\n└─> " + color.Reset)
		cmdName, args := parser.ParseInput(input)
		command, err := parser.GetCommand(cmdName)
		if err != nil {
			log.Error("Command not found!")
			continue
		}
		command.Run(args)
	}
}
