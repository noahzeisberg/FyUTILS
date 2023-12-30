package main

import (
	"crypto/rand"
	"fmt"
	"github.com/NoahOnFyre/gengine/filesystem"
	"github.com/NoahOnFyre/gengine/utils"
	"io"
	"io/fs"
	"os"
	"os/exec"
)

var (
	state = "No State"
)

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func CheckPaths(paths []string) int {
	pathsFixed := 0
	for _, path := range paths {
		if !filesystem.Exists(path) {
			err := os.Mkdir(path, fs.ModeDir)
			if err != nil {
				Error("Failed to create directory!")
				return pathsFixed
			}
			pathsFixed += 1
		}
	}
	return pathsFixed
}

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func SpacingRow(msg string, trim int) string {
	spacing := trim - len(msg)
	return msg + MultiString(" ", spacing)
}

func SpacingRowColorChange(msg string, color string, trim int) string {
	spacing := trim - len(msg) + len(color)
	return msg + MultiString(" ", spacing)
}

func SetState(msg string) {
	state = msg
	utils.SetTitle("FyUTILS " + version + " - " + username + "@" + device + " - " + state)
}

func GetState() string {
	return state
}

func PowerShellRun(command string) {
	cmd := exec.Command("powershell.exe", "-nologo", "-noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		Error("Failed to connect to PowerShell session!")
		return
	}
	go func() {
		defer func(stdin io.WriteCloser) {
			err = stdin.Close()
			if err != nil {
				Error("Failed to close stdin pipe..")
			}
		}(stdin)
		_, err = fmt.Fprintln(stdin, command)
		if err != nil {
			Error("Failed to run PowerShell command.")
		}
	}()
}
