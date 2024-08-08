package cli

import (
	"context"
	"github.com/google/go-github/github"
	"golang.org/x/mod/semver"
)

// CheckUpdate returns true if an update is available, false if either none is
// available or an error occurred during execution.
func CheckUpdate(currentVersion string) (bool, error) {
	client := github.NewClient(nil)
	latestRelease, _, err := client.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "fyutils")
	if err != nil {
		return false, err
	}
	latestVersion := latestRelease.GetTagName()
	return semver.Compare(currentVersion, latestVersion) == 1, nil
}
