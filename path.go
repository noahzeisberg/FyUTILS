package main

import (
	"io/fs"
	"os"
)

func CheckPaths(paths []string) int {
	paths_fixed := 0
	for _, path := range paths {
		if !Exists(path) {
			os.Mkdir(path, fs.ModeDir)
			Print(Prefix(1) + "Fixing non-existing path...")
			paths_fixed += 1
		} else {
			Print(Prefix(0) + "Path \"" + path + "\" exists!")
		}
	}
	return paths_fixed
}

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
