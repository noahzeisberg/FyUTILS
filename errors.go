package main

import "github.com/noahzeisberg/FyUTILS/log"

func Catch(thing any, err error) any {
	if err != nil {
		log.Error("An error occurred during the process: ", err.Error())
	}
	return thing
}
