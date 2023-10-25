package main

import (
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/logging"
	"github.com/NoahOnFyre/gengine/utils"
	"os"
	"os/exec"
	"strings"
)

var (
	username, _   = strings.CutPrefix(convert.ValueOf(utils.Catch(os.UserHomeDir())), "C:\\Users\\")
	device, _     = os.Hostname()
	version       = "v1.13.0"
	homeDir, _    = os.UserHomeDir()
	currentDir, _ = os.Getwd()
	mainDir       = homeDir + "\\.fy\\"
	configPath    = mainDir + "config.json"

	commands []Command
)

func Menu() {
	logging.Clear()

	logging.Print()
	logging.Print(color.Blue + "    ______      __  ______________   _____")
	logging.Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	logging.Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Gray + "Version" + ": " + color.Blue + version + color.Reset)
	logging.Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Gray + "User" + ": " + color.Blue + username + color.Reset)
	logging.Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Gray + "Device" + ": " + color.Blue + device + color.Reset)
	logging.Print(color.Blue + "       __/ /")
	logging.Print(color.Blue + "     /____/")
}

func main() {
	SetState("Initializing...")
	logging.SetMainColor(color.BlueBg)

	logging.Log("Checking paths...")
	SetState("Checking paths...")
	CheckPaths([]string{
		homeDir,
		mainDir,
	})

	logging.Log("Registering commands...")
	SetState("Registering commands...")
	CommandRegistration()

	Menu()

	for {
		SetState("Idle")
		logging.Print()
		input := logging.Input(color.Gray + "┌───[" + color.Blue + username + color.Gray + "@" + color.Reset + device + color.Gray + "]───(" + color.Reset + currentDir + color.Gray + ")\n" + color.Gray + "└─> " + color.Reset)
		if input == "" {
			continue
		}
		logging.Print()
		command, args := ParseCommand(input)
		RunCommand(command, args)
	}
}

func ParseCommand(input string) (string, []string) {
	split := strings.Split(input, " ")
	command := split[0]
	args := utils.RemoveElement(split, 0)
	return command, args
}

func RunCommand(command string, args []string) {
	commandFound := false
	for _, cmd := range commands {
		if cmd.Name == command {
			if len(args) == cmd.Args.Count {
				cmd.Run(args)
				commandFound = true
			} else {
				s := ""
				for _, argument := range cmd.Args.Get {
					s = s + "<" + argument + "> "
				}
				logging.Error("Invalid arguments!" + color.Gray + " - " + color.Red + "Usage: " + command + " " + s)
				commandFound = true
			}
		}
	}
	if !commandFound {
		_, err := exec.LookPath(command)
		if err != nil {
			logging.Error("Command not found! - Run \"help\" to see all commands.")
			return
		}
		var cmdArgs []string
		cmdArgs = append(cmdArgs, "/c")
		cmdArgs = append(cmdArgs, command)
		cmdArgs = append(cmdArgs, args...)
		output, _ := exec.Command("cmd.exe", cmdArgs...).CombinedOutput()
		logging.Print(string(output))
	}
}
