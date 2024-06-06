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
	Home, _       = os.UserHomeDir()
	Version       = "v1.23.0"
	HttpClient    = http.Client{Transport: &http.Transport{}}
	GithubClient  = github.NewClient(&HttpClient)
	Commands      []types.Command
	LatestRelease *github.RepositoryRelease
)
