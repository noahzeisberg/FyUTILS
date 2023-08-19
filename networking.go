package main

import (
	"context"
	"io"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

func ScanPort(addr string, port int, timeout time.Duration) bool {
	conn, err := net.DialTimeout("tcp", net.JoinHostPort(addr, strconv.Itoa(port)), timeout)

	if err != nil {
		if strings.Contains(err.Error(), "too many open files") {
			Print(Prefix(1) + "Timeout exceed")
			time.Sleep(timeout)
			return ScanPort(addr, port, timeout)
		} else {
			return false
		}
	}

	conn.Close()
	return true
}

func DownloadNewestVersion() {
	latest_release, _, err := gh_client.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")
	if err != nil {
		Print(Prefix(2) + "Failed to get latest release: " + err.Error())
	}

	assets := latest_release.Assets
	asset_found := false

	for _, asset := range assets {
		if asset.GetName() == "FyUTILS.exe" {
			asset_found = true
			Print(Prefix(0) + "Found file \"" + asset.GetName() + "\" in NoahOnFyre/FyUTILS")
			Print(Prefix(0) + "Size: " + strconv.Itoa(asset.GetSize()))
			Print(Prefix(0) + "Downloads: " + strconv.Itoa(asset.GetDownloadCount()))
			Print(Prefix(0) + "Created: " + asset.GetCreatedAt().String())
			Print()
			Print(Prefix(0) + "Downloading... This may take a few seconds based on your connection.")
			res, err := http.Get(asset.GetBrowserDownloadURL())

			if err != nil {
				Print(Prefix(2) + "Failed to download file!")
			}

			content, err := io.ReadAll(res.Body)

			if err != nil {
				Print(Prefix(2) + "Failed to parse body!")
			}

			os.WriteFile(current_dir+"\\FyUTILS.exe", content, os.ModePerm)
		}
	}
	if !asset_found {
		Print(Prefix(2) + "No matching asset found!")
	}
}
