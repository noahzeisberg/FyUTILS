package cli

import (
	"errors"
	"github.com/noahzeisberg/FyUTILS/cli/log"
)

var (
	Version string = "v2.0.0"
)

func Main(args []string) {
	log.Println(args)
	log.Error(errors.New("failed to do something lol"), true)
}