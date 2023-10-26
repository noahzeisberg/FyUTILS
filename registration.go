package main

func CommandRegistration() {
	RegisterCommand("flood", "Run a denial of service attack on the target.", []string{"addr", "port"}, FloodCommand)
	RegisterCommand("portscan", "Scan for open ports on the target.", []string{"addr"}, PortscanCommand)
	RegisterCommand("gather", "Gather information about the target.", []string{"addr"}, GatherCommand)
	RegisterCommand("update", "Update your FyUTILS instance.", []string{}, UpdateCommand)
	RegisterCommand("help", "Show some help about the commands.", []string{}, HelpCommand)
	RegisterCommand("clear", "Clear the console window.", []string{}, ClearCommand)
	RegisterCommand("exit", "Exit the application.", []string{}, ExitCommand)
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
}
