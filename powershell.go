package main

import (
	"fmt"
	"os/exec"
)

func PowerShellRunElevated(command string) {
	cmd := exec.Command("powershell.exe", "-verb runas", "-nologo", "-noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		Error("Failed to connect to PowerShell session!")
		return
	}
	go func() {
		defer stdin.Close()
		fmt.Fprintln(stdin, command)
	}()
	out, err := cmd.CombinedOutput()
	if err != nil {
		Error(err.Error())
	}
	Print(string(out))
}
