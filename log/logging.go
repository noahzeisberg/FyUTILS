package log

import (
	"bufio"
	"fmt"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/typing"
	"github.com/noahzeisberg/FyUTILS/utils"
	"os"
	"strings"
)

func Print(msg ...any) {
	fmt.Println(color.Reset + fmt.Sprint(msg...))
}

func PrintC(msg ...any) {
	fmt.Print(color.Reset + fmt.Sprint(msg...))
}

func PrintR(msg ...any) {
	fmt.Print(color.Reset + fmt.Sprint(msg...) + "\r")
}

func Warn(msg ...any) {
	fmt.Println(color.Yellow + fmt.Sprint(msg...))
}

func Error(msg ...any) {
	fmt.Println(color.Red + fmt.Sprint(msg...))
}

func Input(msg ...any) string {
	scanner := bufio.NewScanner(os.Stdin)
	PrintC(msg...)
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
	container += color.Gray + "┌" + utils.MultiString("─", 120-1) + "\n"
	for _, row := range rows {
		container += color.Gray + "│ " + color.Reset + row + "\n"
	}
	container += color.Gray + "└" + utils.MultiString("─", 120-1)
	return container
}

func GroupContainer(contents ...typing.Group) string {
	var maxLength int
	for _, item := range contents {
		if len(fmt.Sprint(item.A)) > maxLength {
			maxLength = len(fmt.Sprint(item.A))
		}
	}
	var container string
	container += color.Gray + "┌" + utils.MultiString("─", 120-1) + "\n"
	for _, item := range contents {
		container += color.Gray + "│ " + color.Blue + fmt.Sprint(item.A) + utils.MultiString(" ", maxLength-len(fmt.Sprint(item.A))+3) + color.Reset + fmt.Sprint(item.B) + "\n"
	}
	container += color.Gray + "└" + utils.MultiString("─", 120-1)
	return container
}

func Menu() {
	Print(color.Blue + "    ______      __  ______________   _____")
	Print(color.Blue + "   / ____/_  __/ / / /_  __/  _/ /  / ___/")
	Print(color.Blue + "  / /_  / / / / / / / / /  / // /   \\__ \\")
	Print(color.Blue + " / __/ / /_/ / /_/ / / / _/ // /______/ /")
	Print(color.Blue + "/_/    \\__, /\\____/ /_/ /___/_____/____/")
	Print(color.Blue + "       __/ /")
	Print(color.Blue + "     /____/")
}
