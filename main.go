package main

import (
	"fyutils/color"
	"fyutils/core"
	"fyutils/log"
	"golang.org/x/text/cases"
	"golang.org/x/text/language"
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

	core.RegisterCommands()
	go core.InitializeReleaseSubscriber()

	for {
		input := log.Input(color.Gray + "┌──(" + color.Blue + "noah" + color.Gray + "@" + color.Reset + "DESKTOP" + color.Gray + ")─[" + color.Reset + "~" + color.Gray + "]\n└─> " + color.Reset)
		cmdName, args := core.ParseInput(input)
		command, err := core.GetCommand(cmdName)
		if err != nil {
			log.Error("Command not found!")
			continue
		}

		err = command.Run(args)
		if err != nil {
			log.Error(cases.Title(language.English, cases.Compact).String(err.Error()) + ".")
			return
		}
	}
}
