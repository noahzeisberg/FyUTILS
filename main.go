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
	"os"
	"os/exec"
	"strings"
)

var (
	username, _ = strings.CutPrefix(convert.ValueOf(utils.Catch(os.UserHomeDir())), "C:\\Users\\")
	device, _   = os.Hostname()
	version     = "v1.16.0"
	homeDir, _  = os.UserHomeDir()
	mainDir     = homeDir + "\\.fy\\"
	commands    []Command
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
	var newestRelease *github.RepositoryRelease

	go func() {
		release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
		if err != nil {
			return
		}

		if semver.Compare(release.GetTagName(), version) == 1 {
			newestRelease = release
		}
	}()

	CheckPaths([]string{
		homeDir,
		mainDir,
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
			command, args := ParseCommand(input)
			RunCommand(command, args)
		}
		if newestRelease != nil {
			Print()
			Print(color.Gray + "┌" + MultiString("─", 120-1))
			Print(color.Gray + "│ " + color.Reset + "A new version of FyUTILS is available! Run " + color.Blue + "\"update\"" + color.Reset + " to download.")
			Print(color.Gray + "│ " + color.Reset + "Version Diff: " + color.Red + version + color.Gray + " -> " + color.Green + newestRelease.GetTagName())
			Print(color.Gray + "└" + MultiString("─", 120-1))
		}
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
				SetState("Running: " + cmd.Name)
				cmd.Run(args)
				commandFound = true
			} else {
				s := ""
				for _, argument := range cmd.Args.Get {
					s = s + "<" + argument + "> "
				}
				Error("Invalid arguments!" + color.Gray + " - " + color.Red + "Usage: " + command + " " + s)
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
			return
		}
	}
}
