package main

import (
	"github.com/noahzeisberg/FyUTILS/cli"
	"os"
)

func main() {
	var filepath = os.Args[0]
	var args = os.Args[:1]

	if filepath == args[0] {
		args = []string{}
	}

	cli.Main(filepath, args)
}
