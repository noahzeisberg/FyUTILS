package types

import (
	"fyutils/log"
)

var Commands []Command

type Command struct {
	Name     string
	Args     []Argument
	Help     string
	Runnable func([]string)
}

type Argument struct {
	Name     string
	Required bool
}

func (c *Command) Run(args []string) {
	var minArgs int
	maxArgs := len(c.Args)
	for _, arg := range c.Args {
		if arg.Required {
			minArgs += 1
		}
	}
	if len(args) < minArgs {
		log.Error("Not enough arguments to execute command.")
		return
	}
	if len(args) > maxArgs {
		log.Error("Too many arguments to execute command.")
		return
	}
	c.Runnable(args)
}
