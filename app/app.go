package app

import (
	"context"
	"fmt"
	"github.com/google/go-github/github"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/log"
	"github.com/noahzeisberg/FyUTILS/utils"
	"golang.org/x/mod/semver"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"time"
)

var (
	Username, _ = strings.CutPrefix(fmt.Sprint(utils.Catch(os.UserHomeDir())), "C:\\Users\\")
	Device, _   = os.Hostname()
	Version     = "v1.23.0"
	HomeDir, _  = os.UserHomeDir()
	MainDir     = HomeDir + "\\.fy\\"
	TempDir     = MainDir + "temp\\"
	DownloadDir = MainDir + "download\\"
	ConfigDir   = MainDir + "config\\"
	FuelDir     = MainDir + "fuel\\"
	HttpClient  = &http.Client{Transport: &http.Transport{}}
	StartTime   = time.Now()

	NewestRelease *github.RepositoryRelease
	Commands      []Command
)

func Main() {
	go func() {
		release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "FyUTILS")
		if err != nil {
			log.Error("Failed to get latest release! " + err.Error())
			return
		}
		NewestRelease = release
	}()

	CheckPaths([]string{
		HomeDir,
		MainDir,
		TempDir,
		DownloadDir,
		ConfigDir,
		FuelDir,
	})

	CommandRegistration()
	Menu()

	for {
		log.Print()
		currentDir, _ := os.Getwd()
		input := log.Input(color.Gray + "┌─[" + color.Blue + Username + color.Gray + "@" + color.Reset + Device + color.Gray + "]─(" + color.Reset + GetPathAlias(currentDir) + color.Gray + ")\n" + color.Gray + "└─> " + color.Reset)
		if input != "" {
			log.Print()
			split := strings.Split(input, " ")
			command := split[0]
			args := utils.RemoveElement(split, 0)
			RunCommand(command, args)
		}
		if semver.Compare(NewestRelease.GetTagName(), Version) == 1 {
			log.Print()
			log.Print(color.Gray + "┌" + utils.MultiString("─", 120-1))
			log.Print(color.Gray + "│ " + color.Reset + "A new version of FyUTILS is available! Run " + color.Blue + "\"update\"" + color.Reset + " to download.")
			log.Print(color.Gray + "│ " + color.Reset + "Version Diff: " + color.Red + Version + color.Gray + " -> " + color.Green + NewestRelease.GetTagName())
			log.Print(color.Gray + "└" + utils.MultiString("─", 120-1))
		}
	}
}

func RunCommand(command string, args []string) {
	commandFound := false
	for _, cmd := range Commands {
		if cmd.Name == command {
			var requiredArgs int
			for _, argument := range cmd.Args {
				if argument.Required {
					requiredArgs++
				}
			}
			if len(args) >= requiredArgs {
				cmd.Run(args)
				commandFound = true
			} else {
				var usage string
				for _, argument := range cmd.Args {
					if argument.Required {
						usage += "<" + argument.Identifier + "> "
					} else {
						usage += "[" + argument.Identifier + "] "
					}
				}
				log.Error("Invalid arguments!" + color.Gray + " - " + color.Red + "Usage: " + command + " " + usage)
				commandFound = true
			}
		}
	}
	if !commandFound {
		_, err := exec.LookPath(command)
		if err != nil {
			log.Error("Command not found! - Run \"help\" to see all commands.")
			return
		}
		var cmdArgs []string
		cmdArgs = append(cmdArgs, "/c", command)
		runnable := exec.Command("cmd.exe", append(cmdArgs, args...)...)

		runnable.Stdout, runnable.Stderr, runnable.Stdin = os.Stdout, os.Stderr, os.Stdin

		err = runnable.Run()
		if err != nil {
			log.Error("Failed to run command! " + err.Error())
			return
		}
	}
}
