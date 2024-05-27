package parser

import (
	"errors"
	"fyutils/types"
	"strings"
)

func ParseInput(input string) (string, []string) {
	split := strings.Split(input, " ")
	command := split[0]
	return command, append(split[:0], split[1:]...)
}

func GetCommand(name string) (types.Command, error) {
	for _, command := range types.Commands {
		if command.Name == name {
			return command, nil
		}
	}
	return types.Command{}, errors.New("command not found")
}
