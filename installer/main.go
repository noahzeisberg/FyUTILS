package installer

import (
	"context"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/logging"
	"github.com/NoahOnFyre/gengine/networking/requests"
	"github.com/google/go-github/github"
	"golang.org/x/sys/windows/registry"
	"log"
	"os"
)

var githubClient = github.NewClient(nil)

func main() {
	logging.Warn("PLEASE BE SURE TO RUN THIS AS ADMINISTRATOR.")
	logging.Warn("If this program doesn't have elevated privileges, it'll crash.")
	logging.Warn("Please exit now, if the installer doesn't has elevated privileges.")

	logging.Print()
	logging.Input("Press enter to continue.")
	logging.Print()

	logging.Log("Starting FyUTILS installer...")
	logging.Log("Fetching newest release...")
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
	if err != nil {
		return
	}
	logging.Log("Target version: " + color.Blue + release.GetTagName() + color.Gray + " (" + release.GetNodeID() + ")")
	logging.Log("URL: " + release.GetHTMLURL())
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
	coreDir := homeDir + "\\.fy\\core"
	os.MkdirAll(coreDir, os.ModePerm)

	for _, asset := range release.Assets {
		if asset.GetName() == "fy.exe" {
			content := requests.Get(asset.GetBrowserDownloadURL())
			err := os.WriteFile(coreDir+"\\fy.exe", content, os.ModePerm)
			if err != nil {
				logging.Error("Failed to write content to file!")
				logging.Error("Please try to run the installer as administrator/sudo again.")
				return
			}
			break
		}
	}
	logging.Log("Download complete!")
	logging.Log("File saved in \"" + color.Blue + coreDir + "\\fy.exe" + color.Reset + "\"!")
	logging.Print()
	logging.Log("Backing up your PATH variable...")
	pathBackup := GetEnvironment("PATH")
	os.WriteFile("C:\\PATHBACKUP.TXT", []byte(pathBackup), os.ModePerm)
	logging.Log("PATH backup file saved in \"" + color.Blue + "C:\\PATHBACKUP.TXT" + color.Reset + "\"")
	logging.Log("")
	logging.Print()
	os.Exit(0)
}

func SetEnvironment(key string, value string) {
	k, err := registry.OpenKey(registry.LOCAL_MACHINE, `SYSTEM\ControlSet001\Control\Session Manager\Environment`, registry.ALL_ACCESS)
	if err != nil {
		log.Fatal(err)
	}
	defer k.Close()

	err = k.SetStringValue(key, value)
	if err != nil {
		log.Fatal(err)
	}
}

func GetEnvironment(key string) string {
	k, err := registry.OpenKey(registry.LOCAL_MACHINE, `SYSTEM\ControlSet001\Control\Session Manager\Environment`, registry.ALL_ACCESS)
	if err != nil {
		logging.Error("Failed to open registry entry:", err)
	}
	defer k.Close()

	value, _, err := k.GetStringValue(key)
	if err != nil {
		logging.Error("Failed to read registry entry:", err)
	}
	return value
}
