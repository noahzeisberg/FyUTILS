package main

import (
	"fmt"
	"io"
	"os/exec"
)

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
