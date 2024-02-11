package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/NoahOnFyre/gengine/color"
)

func Print(msg ...any) {
	fmt.Println(append([]any{color.Reset}, msg...))
}

func PrintR(msg ...any) {
	fmt.Print(append([]any{color.Reset}, msg...))
}

func Warn(msg ...any) {
	fmt.Println(append([]any{color.Yellow}, msg...))
}

func Error(msg ...any) {
	fmt.Println(append([]any{color.Red}, msg...))
}

func Input(msg ...any) string {
	scanner := bufio.NewScanner(os.Stdin)
	PrintR(msg)
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
		if len(item.A) > maxLength {
			maxLength = len(item.A)
		}
	}
	var container string
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, item := range contents {
		container += color.Gray + "│ " + color.Blue + item.A + MultiString(" ", maxLength-len(item.A)+3) + color.Reset + fmt.Sprint(item.B) + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
	return container
}
