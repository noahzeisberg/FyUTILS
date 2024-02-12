package main

import (
	"crypto/rand"
	"strings"
)

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func StripPath(path string) string {
	return strings.TrimSuffix(path, "\\")
}

func RemoveElement(slice []string, index int) []string {
	return append(slice[:index], slice[index+1:]...)
}

func GetPathAlias(path string) string {
	for _, alias := range pathAliases {
		if strings.ToLower(alias.Path) == strings.ToLower(path) {
			return alias.Short
		}
	}
	return path
}

func GetAliasPath(alias string) string {
	for _, path := range pathAliases {
		if path.Short == alias {
			return path.Path
		}
	}
	return alias
}
