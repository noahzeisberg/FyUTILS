package main

func CommandRegistration() {
	RegisterCommand("flood", "Run a denial of service attack on the target.", []Argument{
		{
			Identifier: "ip",
			Required:   true,
		},
		{
			Identifier: "port",
			Required:   true,
		},
	}, FloodCommand)

	RegisterCommand("portscan", "Scan for open ports on the target.", []Argument{
		{
			Identifier: "ip",
			Required:   true,
		},
	}, PortscanCommand)

	RegisterCommand("whois", "Gather WHOIS information about the target.", []Argument{
		{
			Identifier: "ip",
			Required:   true,
		},
	}, WhoisCommand)

	RegisterCommand("retrieve", "Retrieve local information.", []Argument{
		{
			Identifier: "item",
			Required:   true,
		},
	}, RetrieveCommand)

	RegisterCommand("sniff", "Capture traffic of a specific interface.", []Argument{
		{
			Identifier: "interface",
			Required:   true,
		},
	}, SniffCommand)

	RegisterCommand("cd", "Change your current working directory.", []Argument{
		{
			Identifier: "directory",
			Required:   false,
		},
	}, CdCommand)

	RegisterCommand("ls", "List all files in a directory.", []Argument{}, LsCommand)
	RegisterCommand("update", "Update your FyUTILS instance to the newest version.", []Argument{}, UpdateCommand)
	RegisterCommand("help", "Show the help about all the commands.", []Argument{}, HelpCommand)
	RegisterCommand("sys", "Show system and FyUTILS related information.", []Argument{}, SysCommand)
	RegisterCommand("clear", "Clear the console screen.", []Argument{}, ClearCommand)
	RegisterCommand("exit", "Gracefully exit FyUTILS.", []Argument{}, ExitCommand)
}

func RegisterCommand(name string, description string, args []Argument, runnable func([]string)) {
	commands = append(commands, Command{
		Name:        name,
		Description: description,
		Arguments:   args,
		Run:         runnable,
	})
}
