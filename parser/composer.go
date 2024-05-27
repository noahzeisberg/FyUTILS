package parser

import (
	"errors"
	"fyutils/log"
	"fyutils/types"
	"strings"
)

func ComposeArguments(input string) ([]types.Argument, error) {
	var args []types.Argument
	argStrings := strings.Split(input, " ")
	for _, arg := range argStrings {
		log.Print(arg)
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
