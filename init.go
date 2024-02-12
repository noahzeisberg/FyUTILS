package main

import (
	"context"
	"fmt"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/log"
	"io/fs"
	"os"
)

var (
	pathAliases = []PathAlias{
		{
			Short: "~",
			Path:  StripPath(HomeDir),
		},
		{
			Short: "#",
			Path:  StripPath(MainDir),
		},
		{
			Short: "/",
			Path:  "C:\\",
		},
		{
			Short: "@",
			Path:  StripPath("C:\\Windows\\"),
		},
	}
)

func CheckUpdates() {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahzeisberg", "FyUTILS")
	if err != nil {
		return
	}
	NewestRelease = release
}

func CheckPaths(paths []string) int {
	pathsFixed := 0
	for _, path := range paths {
		if !Exists(path) {
			err := os.Mkdir(path, fs.ModeDir)
			if err != nil {
				log.Error("Failed to create directory!")
				return pathsFixed
			}
			pathsFixed += 1
		}
	}
	return pathsFixed
}

func Menu() {
	log.Print(color.Blue + "    ______      __  ______________   _____")
	log.Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	log.Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Gray + "\uE795" + color.Reset + " Version" + ": " + color.Blue + Version + color.Reset)
	log.Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Gray + "\uF007" + color.Reset + " User" + ": " + color.Blue + Username + color.Reset)
	log.Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Gray + "\U000F01C5" + color.Reset + " Device" + ": " + color.Blue + Device + color.Reset)
	log.Print(color.Blue + "       __/ /")
	log.Print(color.Blue + "     /____/" + color.Reset + "   Made by NoahOnFyre with" + color.Blue + " \uf004")
}

func Container(rows ...string) string {
	var container string
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, row := range rows {
		container += color.Gray + "│ " + color.Reset + row + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
	return container
}

func GroupContainer(contents ...Group) string {
	var maxLength int
	for _, item := range contents {
		if len(fmt.Sprint(item.A)) > maxLength {
			maxLength = len(fmt.Sprint(item.A))
		}
	}
	var container string
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, item := range contents {
		container += color.Gray + "│ " + color.Blue + fmt.Sprint(item.A) + MultiString(" ", maxLength-len(fmt.Sprint(item.A))+3) + color.Reset + fmt.Sprint(item.B) + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
	return container
}
