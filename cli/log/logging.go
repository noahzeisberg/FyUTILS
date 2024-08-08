package log

import (
	"bufio"
	"fmt"
	"github.com/noahzeisberg/FyUTILS/cli/color"
	"os"
	"strings"
)

// Println prints the
func Println(msg ...any) {
	fmt.Println(append([]any{color.Reset}, msg...))
}

func Print(msg ...any) {
	fmt.Print(append([]any{color.Reset}, msg...))
}

func PrintR(msg ...any) {
	fmt.Print(append(append([]any{color.Reset}, msg...), "\r"))
}

func Warn(msg ...any) {
	fmt.Println(append([]any{color.Yellow}, msg...))
}

func Error(msg ...any) {
	fmt.Println(append([]any{color.Red}, msg...))
}

func Input(msg ...any) string {
	scanner := bufio.NewScanner(os.Stdin)
	Print(msg...)
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

func Container(rows ...string) string {
	var container string
	container += color.Gray + "┌" + MultiString("─", 120-1) + "\n"
	for _, row := range rows {
		container += color.Gray + "│ " + color.Reset + row + "\n"
	}
	container += color.Gray + "└" + MultiString("─", 120-1)
	return container
}

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func Menu() {
	Println(color.Blue + "    ______      __  ______________   _____")
	Println(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	Println(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\")
	Println(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /")
	Println(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/")
	Println(color.Blue + "       __/ /")
	Println(color.Blue + "     /____/")
}
