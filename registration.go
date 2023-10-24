package main

import (
	"github.com/NoahOnFyre/gengine/logging"
	"strconv"
)

func CommandRegistration() {
	RegisterCommand("flood", "Run a denial of service attack on the target.", Arguments{"addr", "port"}, FloodCommand)
	RegisterCommand("portscan", "Scan for open ports on the target.", Arguments{"addr"}, PortscanCommand)
	RegisterCommand("gather", "Gather information about the target.", Arguments{"addr"}, GatherCommand)
	// RegisterCommand("update", "Update your FyUTILS instance.", Arguments{}, UpdateCommand)
	RegisterCommand("help", "Show some help about the commands.", Arguments{}, HelpCommand)
	RegisterCommand("clear", "Clear the console window.", Arguments{}, ClearCommand)
	RegisterCommand("exit", "Exit the application.", Arguments{}, ExitCommand)
}

func RegisterCommand(name string, description string, args []string, runnable func([]string)) {
	arguments := Args{
		Count: len(args),
		Get:   args,
	}
	commands = append(commands, Command{
		Name:        name,
		Description: description,
		Args:        arguments,
		Run:         runnable,
	})

	logging.Log("Successfully registered command \"" + name + "\" with " + strconv.Itoa(len(args)) + " arguments.")
}
