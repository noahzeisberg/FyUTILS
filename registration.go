package main

func CommandRegistration() {
	RegisterCommand("flood", "Run a denial of service attack on the target.", []string{"ip", "port"}, FloodCommand)
	RegisterCommand("portscan", "Scan for open ports on the target.", []string{"ip"}, PortscanCommand)
	RegisterCommand("whois", "Gather WHOIS information about the target.", []string{"ip"}, WhoisCommand)
	RegisterCommand("retrieve", "Retrieve local information.", []string{"item"}, RetrieveCommand)
	RegisterCommand("sniff", "Capture traffic of a specific interface.", []string{"interface"}, SniffCommand)
	RegisterCommand("cd", "Change your current working directory.", []string{"dir"}, CdCommand)
	RegisterCommand("ls", "List all files in a directory.", []string{}, LsCommand)
	RegisterCommand("update", "Update your FyUTILS instance to the newest version.", []string{}, UpdateCommand)
	RegisterCommand("help", "Show the help about all the commands.", []string{}, HelpCommand)
	RegisterCommand("clear", "Clear the console screen.", []string{}, ClearCommand)
	RegisterCommand("exit", "Gracefully exit FyUTILS.", []string{}, ExitCommand)
}

func RegisterCommand(name string, description string, args []string, runnable func([]string)) {
	arguments := Args{
		Count: len(args),
		Usage: args,
	}
	commands = append(commands, Command{
		Name:        name,
		Description: description,
		Args:        arguments,
		Run:         runnable,
	})
}
