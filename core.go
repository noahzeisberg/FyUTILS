package main

func MainMenu() {
	PrintR("\033[H\033[2J")
	Print(Blue + "    ______      __  ______________   _____ ")
	Print(Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/ ")
	Print(Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\  " + MainMenuEntry("Version", version))
	Print(Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /  " + MainMenuEntry("User", username))
	Print(Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/   " + MainMenuEntry("Device", device))
	Print(Blue + "       __/ /                               ")
	Print(Blue + "     /____/                                ")
}

func MainMenuEntry(title string, description string) string {
	return "   " + Gray + title + ": " + Blue + description + Reset
}

func RunCommand(command string, args []string) {
	command_found := false
	for _, cmd := range commands {
		if cmd.Name == command {
			if len(args) == cmd.Args.Count {
				cmd.Run(args)
				command_found = true
			} else {
				argstring := ""
				for _, argument := range cmd.Args.Get {
					argstring = argstring + "<" + argument + "> "
				}
				Print(Prefix(2) + "Invalid arguments!" + Gray + " - " + Red + "Usage: " + command + " " + argstring)
				command_found = true
			}
		}
	}
	if !command_found {
		Print(Prefix(2) + "Command not found!" + Gray + " - " + Red + "See \"help\" for help.")
	}
}
