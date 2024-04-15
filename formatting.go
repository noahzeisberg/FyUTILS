package main

import (
	"fmt"
	"github.com/noahzeisberg/FyUTILS/color"
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
