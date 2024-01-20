package main

import (
	"bufio"
	"fmt"
	"github.com/NoahOnFyre/gengine/color"
	"os"
	"strings"
)

func Print(msg ...string) {
	fmt.Println(color.Reset + strings.Join(msg, " "))
}

func PrintR(msg any) {
	fmt.Print(msg)
}

func Warn(msg ...string) {
	fmt.Println(color.Yellow + strings.Join(msg, " "))
}

func Error(msg ...string) {
	fmt.Println(color.Red + strings.Join(msg, " "))
}

func Input(msg string) string {
	scanner := bufio.NewScanner(os.Stdin)
	PrintR(msg)
	scanner.Scan()
	return scanner.Text()
}

func Confirm(title string) bool {
	for {
		confirmation := Input(title + " " + color.Gray + "(yes/no): " + color.Reset)
		if confirmation == "yes" {
			return true
		} else if confirmation == "no" {
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
