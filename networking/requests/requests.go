package requests

import (
	"github.com/noahzeisberg/FyUTILS/log"
	"io"
	"net/http"
	"os"
)

func Get(url string) []byte {
	response, err := http.Get(url)

	if err != nil {
		log.Error("Failed to make GET request:", err.Error())
		return nil
	}

	content, err := io.ReadAll(response.Body)
	if err != nil {
		log.Error("Failed to read body contents:", err.Error())
		os.Exit(1)
	}

	err = response.Body.Close()
	if err != nil {
		log.Error("Failed to make GET request:", err.Error())
		return nil
	}

	return content
}
