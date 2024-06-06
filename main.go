package main

import (
	"fyutils/color"
	"fyutils/core"
	"fyutils/log"
	"golang.org/x/mod/semver"
	"golang.org/x/text/cases"
	"golang.org/x/text/language"
	"os"
	"strings"
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
		workingDir, _ := os.Getwd()
		input := log.Input(color.Gray + "┌──(" + color.Blue + strings.Split(core.User.Username, "\\")[1] + color.Gray + "@" + color.Reset + core.Device + color.Gray + ")─[" + color.Reset + workingDir + color.Gray + "]\n└─> " + color.Reset)
		cmdName, args := core.ParseInput(input)
		command, err := core.GetCommand(cmdName)
		if err != nil {
			log.Error("Command not found!")
			continue
		}

		log.Print()
		err = command.Run(args)
		if err != nil {
			log.Error(cases.Title(language.English, cases.Compact).String(err.Error()) + ".")
			continue
		}
		log.Print()

		if semver.Compare(core.LatestRelease.GetTagName(), core.Version) == 1 {
			log.Print(log.Container("A new FyUTILS release is freshly available for you!", "Diff: "+color.Red+core.Version+color.Gray+" -> "+color.Green+core.LatestRelease.GetTagName()))
		}
	}
}
