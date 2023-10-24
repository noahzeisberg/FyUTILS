package main

import (
	"crypto/rand"
	"github.com/NoahOnFyre/gengine/filesystem"
	"io/fs"
	"os"
)

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func CheckPaths(paths []string) int {
	pathsFixed := 0
	for _, path := range paths {
		if !filesystem.Exists(path) {
			os.Mkdir(path, fs.ModeDir)
			pathsFixed += 1
		}
	}
	return pathsFixed
}
