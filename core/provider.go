package core

import (
	"fyutils/types"
	"github.com/google/go-github/github"
	"net/http"
	"os"
	"os/user"
)

var (
	User, _       = user.Current()
	Device, _     = os.Hostname()
	HomeDir, _    = os.UserHomeDir()
	MainDir       = HomeDir + "\\.fy\\"
	ExtensionsDir = MainDir + "\\extensions\\"
	TempDir       = MainDir + "\\temp\\"
	LogsDir       = MainDir + "\\logs\\"
	DownloadDir   = MainDir + "\\download\\"
	Version       = "v1.23.0"
	HttpClient    = http.Client{Transport: &http.Transport{}}
	GithubClient  = github.NewClient(&HttpClient)
	Commands      []types.Command
	LatestRelease *github.RepositoryRelease
)
