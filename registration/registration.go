package registration

import (
	"fyutils/cmd"
	"fyutils/log"
	"fyutils/parser"
	"fyutils/types"
)

func RegisterCommands() {
	register("info", "<text> [number]", "Test command used for debugging.", cmd.Info)
	register("exit", "[code]", "Exit the application.", cmd.Exit)
}

func register(name string, argString string, help string, runnable func([]string)) {
	args, err := parser.ComposeArguments(argString)
	if err != nil {
		log.Error(err)
		return
	}
	types.Commands = append(types.Commands, types.Command{
		Name:     name,
		Args:     args,
		Help:     help,
		Runnable: runnable,
	})
}
