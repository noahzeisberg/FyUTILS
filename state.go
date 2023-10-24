package main

import "github.com/NoahOnFyre/gengine/utils"

var (
	state = "No State"
)

func SetState(msg string) {
	state = msg
	utils.SetTitle("FyUTILS " + version + " - " + username + "@" + device + " - " + state)
}

func GetState() string {
	return state
}
