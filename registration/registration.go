package registration

import (
	"fyutils/log"
	"fyutils/parser"
	"fyutils/types"
)

func Register(name string, argString string, help string, runnable func([]string)) {
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
