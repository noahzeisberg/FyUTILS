package main

import (
	"bufio"
	"fmt"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/convert"
	"os"
	"strings"
)

func Print(msg ...any) {
	var items []string
	for _, item := range msg {
		items = append(items, convert.ValueOf(item))
	}
	output := strings.Join(items, " ")
	fmt.Println(color.Reset + output)
}

func PrintR(msg any) {
	fmt.Print(msg)
}

func Warn(msg ...any) {
	var items []string
	for _, item := range msg {
		items = append(items, convert.ValueOf(item))
	}
	output := strings.Join(items, " ")
	fmt.Println(color.Yellow + output)
}

func Error(msg ...any) {
	var items []string
	for _, item := range msg {
		items = append(items, convert.ValueOf(item))
	}
	output := strings.Join(items, " ")
	fmt.Println(color.Red + output)
}

func Input(msg string) string {
	scanner := bufio.NewScanner(os.Stdin)
	PrintR(msg)
	scanner.Scan()
	return scanner.Text()
}

func Clear() {
	PrintR("\033[H\033[2J")
}
