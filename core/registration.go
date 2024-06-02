package core

import (
	"fyutils/cmd"
	"fyutils/log"
	"fyutils/types"
)

func RegisterCommands() {
	register("exit", "[code]", "Exit the application.", cmd.Exit)
}

func register(name string, argString string, help string, runnable func([]string)) {
	args, err := ComposeArguments(argString)
	if err != nil {
		log.Error(err)
		return
	}
	Commands = append(Commands, types.Command{
		Name:     name,
		Args:     args,
		Help:     help,
		Runnable: runnable,
	})
}
