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

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func SpacingRow(msg string, trim int) string {
	spacing := trim - len(msg)
	return msg + MultiString(" ", spacing)
}

func SpacingRowColorChange(msg string, color string, trim int) string {
	spacing := trim - len(msg) + len(color)
	return msg + MultiString(" ", spacing)
}
