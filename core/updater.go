package core

import (
	"context"
	"time"
)

func InitializeReleaseSubscriber() {
	for {
		release, _, err := GithubClient.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "fyutils")
		if err != nil || release == nil {
			return
		}
		LatestRelease = release
		time.Sleep(1 * time.Minute)
	}
}
