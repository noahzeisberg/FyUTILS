package main

import (
	"bufio"
	"fmt"
	"github.com/NoahOnFyre/gengine/color"
	"os"
)

func Log(msg ...any) {
	msg = append(msg, color.Reset)
	fmt.Println(msg...)
}

func Warn(msg ...any) {
	msg = append(msg, color.Yellow)
	fmt.Println(msg...)
}

func Error(msg ...any) {
	msg = append(msg, color.Red)
	fmt.Println(msg...)
}

func Print(msg ...any) {
	fmt.Println(msg...)
}

func PrintR(msg ...any) {
	fmt.Print(msg...)
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
