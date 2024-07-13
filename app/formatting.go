package app

import (
	"fmt"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/log"
	"github.com/noahzeisberg/FyUTILS/utils"
)

func Container(rows ...string) string {
	var container string
	container += color.Gray + "┌" + utils.MultiString("─", 120-1) + "\n"
	for _, row := range rows {
		container += color.Gray + "│ " + color.Reset + row + "\n"
	}
	container += color.Gray + "└" + utils.MultiString("─", 120-1)
	return container
}

func GroupContainer(contents ...Group) string {
	var maxLength int
	for _, item := range contents {
		if len(fmt.Sprint(item.A)) > maxLength {
			maxLength = len(fmt.Sprint(item.A))
		}
	}
	var container string
	container += color.Gray + "┌" + utils.MultiString("─", 120-1) + "\n"
	for _, item := range contents {
		container += color.Gray + "│ " + color.Blue + fmt.Sprint(item.A) + utils.MultiString(" ", maxLength-len(fmt.Sprint(item.A))+3) + color.Reset + fmt.Sprint(item.B) + "\n"
	}
	container += color.Gray + "└" + utils.MultiString("─", 120-1)
	return container
}

func Menu() {
	log.Print(color.Blue + "    ______      __  ______________   _____")
	log.Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	log.Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Reset + " Version" + ": " + color.Blue + Version + color.Reset)
	log.Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Reset + " User" + ": " + color.Blue + Username + color.Reset)
	log.Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Reset + " Device" + ": " + color.Blue + Device + color.Reset)
	log.Print(color.Blue + "       __/ /")
	log.Print(color.Blue + "     /____/")
}
