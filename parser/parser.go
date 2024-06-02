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

func ComposeArguments(input string) ([]types.Argument, error) {
	var args []types.Argument
	argStrings := strings.Split(input, " ")
	for _, arg := range argStrings {
		if strings.HasPrefix(arg, "<") && strings.HasSuffix(arg, ">") {
			args = append(args, types.Argument{
				Name:     strings.Trim(arg, "<>"),
				Required: true,
			})
		} else if strings.HasPrefix(arg, "[") && strings.HasSuffix(arg, "]") {
			args = append(args, types.Argument{
				Name:     strings.Trim(arg, "[]"),
				Required: false,
			})
		} else {
			return []types.Argument{}, errors.New("failed to compose argument")
		}
	}
	return args, nil
}
