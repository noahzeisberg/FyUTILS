package main

import (
	"github.com/noahzeisberg/FyUTILS/cli"
	"os"
)

func main() {
	cli.Main(append(os.Args[:0], os.Args[1:]...))
}
