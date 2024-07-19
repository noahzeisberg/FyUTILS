package utils

import (
	"fmt"
	"os/exec"
)

func PowerShellRun(command string) (string, error) {
	cmd := exec.Command("cmd.exe", "/c", "powershell.exe -nologo -noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		return "", err
	}
	_, err = fmt.Fprintln(stdin, command)
	if err != nil {
		return "", err
	}
	err = stdin.Close()
	if err != nil {
		return "", err
	}
	out, err := cmd.CombinedOutput()
	if err != nil {
		return "", err
	}
	return string(out), nil
}
