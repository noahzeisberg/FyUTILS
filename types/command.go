package types

import (
	"errors"
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

func (c *Command) Run(args []string) error {
	var minArgs int
	maxArgs := len(c.Args)
	for _, arg := range c.Args {
		if arg.Required {
			minArgs += 1
		}
	}
	if len(args) < minArgs {
		return errors.New("not enough arguments")
	}
	if len(args) > maxArgs {
		return errors.New("too much arguments")
	}

	c.Runnable(args)
	return nil
}
