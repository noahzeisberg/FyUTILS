package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/noahzeisberg/gengine/color"
)

func Print(msg ...any) {
	fmt.Println(color.Reset + fmt.Sprint(msg...))
}

func PrintR(msg ...any) {
	fmt.Print(color.Reset + fmt.Sprint(msg...))
}

func Warn(msg ...any) {
	fmt.Println(color.Yellow + fmt.Sprint(msg...))
}

func Error(msg ...any) {
	fmt.Println(color.Red + fmt.Sprint(msg...))
}

func Input(msg ...any) string {
	scanner := bufio.NewScanner(os.Stdin)
	PrintR(msg...)
	scanner.Scan()
	return scanner.Text()
}

func Menu() {
	Print(color.Blue + "    ______      __  ______________   _____")
	Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\" + "     " + color.Gray + "\uE795" + color.Reset + " Version" + ": " + color.Blue + version + color.Reset)
	Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /" + "     " + color.Gray + "\uF007" + color.Reset + " User" + ": " + color.Blue + username + color.Reset)
	Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/" + "      " + color.Gray + "\U000F01C5" + color.Reset + " Device" + ": " + color.Blue + device + color.Reset)
	Print(color.Blue + "       __/ /")
	Print(color.Blue + "     /____/" + color.Reset + "   Made by NoahOnFyre with" + color.Blue + " \uf004")
}

func Confirm(title string) bool {
	for {
		confirmation := Input(title + " " + color.Gray + "(y/n): " + color.Reset)
		if strings.ToLower(confirmation) == "y" {
			return true
		} else if strings.ToLower(confirmation) == "n" {
			return false
		} else {
			continue
		}
	}
}

func Clear() {
	PrintR("\033[H\033[2J")
}

func Container(rows ...string) string {
	var container string
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, row := range rows {
		container += color.Gray + "│ " + color.Reset + row + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
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
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, item := range contents {
		container += color.Gray + "│ " + color.Blue + fmt.Sprint(item.A) + MultiString(" ", maxLength-len(fmt.Sprint(item.A))+3) + color.Reset + fmt.Sprint(item.B) + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
	return container
}
