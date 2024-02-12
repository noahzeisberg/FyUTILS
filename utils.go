package main

import (
	"crypto/rand"
	"fmt"
	"github.com/NoahOnFyre/gengine/utils"
	"os/exec"
	"strings"
)

var (
	state = "No State"
)

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func SetState(msg string) {
	state = msg
	utils.SetTitle("FyUTILS " + version + " - " + username + "@" + device + " - " + state)
}

func PowerShellRun(command string) {
	cmd := exec.Command("cmd.exe", "/c", "powershell.exe -nologo -noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		Error("Failed to connect to PowerShell session!")
		return
	}
	_, err = fmt.Fprintln(stdin, command)
	if err != nil {
		Error("Failed to run PowerShell command.")
		return
	}
	err = stdin.Close()
	if err != nil {
		Error("Failed to close pipe..")
		return
	}
	out, err := cmd.CombinedOutput()
	if err != nil {
		Error(err.Error())
	}
	Print(string(out))
}

func StripPath(path string) string {
	return strings.TrimSuffix(path, "\\")
}

func GetPathAlias(path string) string {
	for _, alias := range pathAliases {
		if strings.ToLower(alias.Path) == strings.ToLower(path) {
			return alias.Short
		}
	}
	return path
}

func GetAliasPath(alias string) string {
	for _, path := range pathAliases {
		if path.Short == alias {
			return path.Path
		}
	}
	return alias
}
