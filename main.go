package main

import (
	"bytes"
	"context"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"github.com/NoahOnFyre/gengine/utils"
	"github.com/google/go-github/github"
	"golang.org/x/mod/semver"
	"io"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"time"
)

var (
	username, _   = strings.CutPrefix(convert.ValueOf(utils.Catch(os.UserHomeDir())), "C:\\Users\\")
	device, _     = os.Hostname()
	version       = "v1.18.1"
	homeDir, _    = os.UserHomeDir()
	mainDir       = homeDir + "\\.fy\\"
	tempDir       = mainDir + "temp\\"
	downloadDir   = mainDir + "download\\"
	configDir     = mainDir + "config\\"
	fuelDir       = mainDir + "fuel\\"
	newestRelease *github.RepositoryRelease
	httpClient    = &http.Client{Transport: &http.Transport{}}
	startTime     = time.Now()
	commands      []Command
)

func Menu() {
	Print(color.Blue + "    ______      __  ______________   _____")
	Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Gray + "\uE795" + color.Reset + " Version" + ": " + color.Blue + version + color.Reset)
	Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Gray + "\uF007" + color.Reset + " User" + ": " + color.Blue + username + color.Reset)
	Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Gray + "\U000F01C5" + color.Reset + " Device" + ": " + color.Blue + device + color.Reset)
	Print(color.Blue + "       __/ /")
	Print(color.Blue + "     /____/" + color.Reset + "   Made by NoahOnFyre with" + color.Blue + " \uf004")
}

func main() {
	go func() {
		release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
		if err != nil {
			return
		}
		newestRelease = release
	}()

	CheckPaths([]string{
		homeDir,
		mainDir,
		tempDir,
		downloadDir,
		configDir,
		fuelDir,
	})

	CommandRegistration()
	Menu()

	for {
		SetState("Idle")
		Print()
		currentDir, _ := os.Getwd()
		input := Input(color.Gray + "┌─[" + color.Blue + username + color.Gray + "@" + color.Reset + device + color.Gray + "]─(" + color.Reset + "\U000F024B" + " " + currentDir + color.Gray + ")\n" + color.Gray + "└─> " + color.Reset)
		if input != "" {
			Print()
			split := strings.Split(input, " ")
			command := split[0]
			args := utils.RemoveElement(split, 0)
			RunCommand(command, args)
		}
		if semver.Compare(version, newestRelease.GetTagName()) == -1 {
			Print()
			Print(color.Gray + "┌" + MultiString("─", 120-1))
			Print(color.Gray + "│ " + color.Reset + "A new version of FyUTILS is available! Run " + color.Blue + "\"update\"" + color.Reset + " to download.")
			Print(color.Gray + "│ " + color.Reset + "Version Diff: " + color.Red + version + color.Gray + " -> " + color.Green + newestRelease.GetTagName())
			Print(color.Gray + "└" + MultiString("─", 120-1))
		}
	}
}

func RunCommand(command string, args []string) {
	commandFound := false
	for _, cmd := range commands {
		if cmd.Name == command {
			var requiredArgs int
			for _, argument := range cmd.Arguments {
				if argument.Required {
					requiredArgs++
				}
			}
			if len(args) >= requiredArgs {
				SetState("Running: " + cmd.Name)
				cmd.Run(args)
				commandFound = true
			} else {
				var usage string
				for _, argument := range cmd.Arguments {
					if argument.Required {
						usage += "<" + argument.Identifier + "> "
					} else {
						usage += "[" + argument.Identifier + "] "
					}
				}
				Error("Invalid arguments!" + color.Gray + " - " + color.Red + "Usage: " + command + " " + usage)
				commandFound = true
			}
		}
	}
	if !commandFound {
		_, err := exec.LookPath(command)
		if err != nil {
			Error("Command not found! - Run \"help\" to see all commands.")
			return
		}
		var cmdArgs []string
		cmdArgs = append(cmdArgs, "/c")
		cmdArgs = append(cmdArgs, command)
		cmdArgs = append(cmdArgs, args...)
		SetState("Running: " + command)
		runnable := exec.Command("cmd.exe", cmdArgs...)

		var stdBuffer bytes.Buffer
		mw := io.MultiWriter(os.Stdout, &stdBuffer)

		runnable.Stdout = mw
		runnable.Stderr = mw

		err = runnable.Run()
		if err != nil {
			Error("Failed to run command!", err.Error())
			return
		}
	}
}
