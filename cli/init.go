package cli

import (
	"github.com/noahzeisberg/FyUTILS/cli/log"
	"net/http"
)

var (
	Version string = "v2.0.0"
)

func Main(args []string) {
	log.Println(args)
	_, err := http.Get("https://asigansiiagsidnasndaw.tk")
	log.Error(err, true)
}
