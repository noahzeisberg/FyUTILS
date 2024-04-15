package main

import (
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/log"
)

func Menu() {
	log.Print(color.Blue + "    ______      __  ______________   _____")
	log.Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	log.Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Reset + " Version" + ": " + color.Blue + Version + color.Reset)
	log.Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Reset + " User" + ": " + color.Blue + Username + color.Reset)
	log.Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Reset + " Device" + ": " + color.Blue + Device + color.Reset)
	log.Print(color.Blue + "       __/ /")
	log.Print(color.Blue + "     /____/")
}
