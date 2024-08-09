package log

import (
	"bufio"
	"fmt"
	"github.com/noahzeisberg/FyUTILS/cli/color"
	"github.com/noahzeisberg/FyUTILS/cli/log/trace"
	"os"
	"runtime"
	"strings"
)

// Print prints the given objects to `os.Stdout`. It takes the objects as arguments.
func Print(msg ...any) {
	fmt.Print(append([]any{color.Reset}, msg...)...)
}

// Println prints the given objects to `os.Stdout` and appends a newline. It takes the objects as arguments.
func Println(msg ...any) {
	Print(append(msg, "\n")...)
}

// PrintR prints the given objects to `os.Stdout` and appends a carriage return. It takes the objects as arguments.
func PrintR(msg ...any) {
	Print(append(msg, "\r")...)
}

func Error(err error, fatal bool) {
	pc, filename, line, _ := runtime.Caller(1)
	stackTrace := trace.GenerateTrace(err, pc, filename, line)
	Println(stackTrace.Error.Error())
	Println(stackTrace.FileName)
	Println(stackTrace.Line)
	Println(stackTrace.FuncName)
	Println(stackTrace.Package) // github.com/noahzeisberg/fyutils
	Println(stackTrace.SubPackage)

	if fatal {
		Input(color.Red + "Press enter to exit.")
		os.Exit(1)
	}
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
