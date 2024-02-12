package main

import (
	"github.com/noahzeisberg/FyUTILS/log"
	"io/fs"
	"os"
	"strings"
)

var (
	PathAliases = []PathAlias{
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

func Exists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		return true
	}
	if os.IsNotExist(err) {
		return false
	}
	return false
}

func StripPath(path string) string {
	return strings.TrimSuffix(path, "\\")
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

func GetPathAlias(path string) string {
	for _, alias := range PathAliases {
		if strings.ToLower(alias.Path) == strings.ToLower(path) {
			return alias.Short
		}
	}
	return path
}

func GetAliasPath(alias string) string {
	for _, path := range PathAliases {
		if path.Short == alias {
			return path.Path
		}
	}
	return alias
}
