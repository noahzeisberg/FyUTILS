package main

import "fmt"

func PrintR(msg any) {
	fmt.Print(msg)
}

func Print(msg ...any) {
	fmt.Println(msg...)
}

func Prefix(level int) string {
	switch level {
	case 0:
		return Black + BlueBg + " INFO " + Reset + " " + Reset
	case 1:
		return Black + YellowBg + " WARN " + Reset + " " + Yellow
	case 2:
		return Black + RedBg + " INFO " + Reset + " " + Red
	default:
		return Black + RedBg + " NONE " + Reset + " " + Reset
	}
}
