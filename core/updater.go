package core

import (
	"context"
	"time"
)

func InitializeReleaseSubscriber(bridge chan bool) {
	for {
		latestRelease, _, err := GithubClient.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "fyutils")
		if err != nil {
			return
		}
		bridge <- latestRelease.GetTagName() == ""
		time.Sleep(5 * time.Minute)
	}
}
