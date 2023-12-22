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

func Wait(title string) {
	Input(title)
}

func Clear() {
	PrintR("\033[H\033[2J")
}
