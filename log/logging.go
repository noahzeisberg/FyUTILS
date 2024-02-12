package log

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/noahzeisberg/FyUTILS/color"
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
