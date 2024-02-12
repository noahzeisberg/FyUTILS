package utils

import (
	"fmt"
	"github.com/noahzeisberg/FyUTILS/log"
	"os/exec"
)

func PowerShellRun(command string) {
	cmd := exec.Command("cmd.exe", "/c", "powershell.exe -nologo -noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		log.Error("Failed to connect to PowerShell session!")
		return
	}
	_, err = fmt.Fprintln(stdin, command)
	if err != nil {
		log.Error("Failed to run PowerShell command.")
		return
	}
	err = stdin.Close()
	if err != nil {
		log.Error("Failed to close pipe..")
		return
	}
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Error(err.Error())
	}
	log.Print(string(out))
}
