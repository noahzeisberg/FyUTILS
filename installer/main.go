package main

import (
	"context"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/logging"
	"github.com/NoahOnFyre/gengine/networking/requests"
	"github.com/google/go-github/github"
	"golang.org/x/sys/windows/registry"
	"os"
	"os/exec"
	"strings"
)

var githubClient = github.NewClient(nil)

func main() {
	logging.SetMainColor(color.BlueBg)

	logging.Warn("PLEASE BE SURE TO RUN THIS AS ADMINISTRATOR.")
	logging.Warn("If this program doesn't has elevated privileges, it'll crash.")
	logging.Warn("Please exit now, if the installer doesn't has elevated privileges.")

	logging.Print(color.Reset)
	logging.Input("Press enter to continue.")
	logging.Print(color.Reset)

	logging.Clear()

	logging.Log("Starting FyUTILS installer...")
	logging.Log("Fetching newest release...")
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
	if err != nil {
		return
	}
	logging.Print()
	logging.Log("Target Version: " + color.Blue + release.GetTagName() + color.Gray + " (" + release.GetNodeID() + ")")
	logging.Log("Description: " + color.Gray + strings.Split(release.GetBody(), "\n")[0])
	logging.Log("Uploaded:"+color.Blue, release.GetPublishedAt().Month(), release.GetPublishedAt().Day(), release.GetPublishedAt().Year(), color.Gray+" - by @noahonfyre")
	logging.Print()
	for {
		confirmation := logging.Input(logging.Prefix(0) + " " + "Do you want to download this version? " + color.Gray + "(yes/no): " + color.Reset)
		if confirmation == "yes" {
			logging.Log("Starting installation...")
			break
		} else if confirmation == "no" {
			logging.Log("Exiting...")
			return
		} else {
			logging.Error("Invalid argument!")
			continue
		}
	}

	homeDir, _ := os.UserHomeDir()
	mainDir := homeDir + "\\.fy"
	os.MkdirAll(mainDir, os.ModePerm)

	for _, asset := range release.Assets {
		if asset.GetName() == "fy.exe" {
			content := requests.Get(asset.GetBrowserDownloadURL())
			err := os.WriteFile(mainDir+"\\fy.exe", content, os.ModePerm)
			if err != nil {
				logging.Error("Failed to write content to file!")
				logging.Error("Please try to run the installer as administrator/sudo again.")
				return
			}
			break
		}
	}
	logging.Print()
	logging.Log("Download complete!")
	logging.Log("File saved in \"" + color.Blue + mainDir + "\\fy.exe" + color.Reset + "\"!")
	logging.Log("Backing up your PATH variable...")
	pathBackup := GetEnvironment("PATH")
	err = os.WriteFile("C:\\PATHBACKUP.TXT", []byte(pathBackup), os.ModePerm)
	if err != nil {
		logging.Error("Failed to backup PATH!")
		return
	}
	logging.Log("PATH backup file saved in \"" + color.Blue + "C:\\PATHBACKUP.TXT" + color.Reset + "\"")
	logging.Log("Adding FyUTILS to path...")
	SetEnvironment("PATH", pathBackup+";"+mainDir)
	logging.Log("Success!")
	logging.Print()
	logging.Warn("If you enjoy FyUTILS, please consider to star my repository on GitHub.")
	logging.Warn("This would support me a lot and is completely free for you. :D")
	logging.Warn("⭐ https://github.com/NoahOnFyre/FyUTILS ⭐")
	logging.Print()
	logging.Log("Please restart your PC now to apply changes.")
	logging.Input("Press enter to restart your PC.")
	exec.Command("shutdown", "-r").Run()
	os.Exit(0)
}

func SetEnvironment(key string, value string) {
	k, err := registry.OpenKey(registry.LOCAL_MACHINE, `SYSTEM\ControlSet001\Control\Session Manager\Environment`, registry.ALL_ACCESS)
	if err != nil {
		logging.Error("Failed to open registry entry:", err)
		return
	}
	defer k.Close()

	err = k.SetStringValue(key, value)
	if err != nil {
		logging.Error("Failed to write registry entry:", err)
		return
	}
}

func GetEnvironment(key string) string {
	k, err := registry.OpenKey(registry.LOCAL_MACHINE, `SYSTEM\ControlSet001\Control\Session Manager\Environment`, registry.ALL_ACCESS)
	if err != nil {
		logging.Error("Failed to open registry entry:", err)
		os.Exit(1)
	}
	defer k.Close()

	value, _, err := k.GetStringValue(key)
	if err != nil {
		logging.Error("Failed to read registry entry:", err)
		os.Exit(1)
	}
	return value
}
