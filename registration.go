package main

func CommandRegistration() {
	Command{
		Name:  "flood",
		Short: "Run a denial of service attack on the target.",
		Args: Arguments{
			{
				Identifier: "ip",
				Required:   true,
			},
			{
				Identifier: "port",
				Required:   true,
			},
		},
		Run: FloodCommand,
	}.Register()

	Command{
		Name:  "portscan",
		Short: "Scan for open ports on the target.",
		Args: Arguments{
			{
				Identifier: "ip",
				Required:   true,
			},
		},
		Run: PortscanCommand,
	}.Register()

	Command{
		Name:  "whois",
		Short: "Gather WHOIS information about the target.",
		Args: Arguments{
			{
				Identifier: "ip",
				Required:   true,
			},
		},
		Run: WhoisCommand,
	}.Register()

	Command{
		Name:  "retrieve",
		Short: "Retrieve local information.",
		Args: Arguments{
			{
				Identifier: "item",
				Required:   true,
			},
		},
		Run: RetrieveCommand,
	}.Register()

	Command{
		Name:  "sniff",
		Short: "Capture traffic of a specific interface.",
		Args: Arguments{
			{
				Identifier: "interface",
				Required:   true,
			},
		},
		Run: SniffCommand,
	}.Register()

	Command{
		Name:  "fetch",
		Short: "Download a file from the specific URL.",
		Args: Arguments{
			{
				Identifier: "url",
				Required:   true,
			},
		},
		Run: FetchCommand,
	}.Register()

	Command{
		Name:  "fuel",
		Short: "Manage extensions and libraries.",
		Args: Arguments{
			{
				Identifier: "action",
				Required:   true,
			},
			{
				Identifier: "pkg",
				Required:   false,
			},
		},
		Run: FuelCommand,
	}.Register()

	Command{
		Name:  "cd",
		Short: "Change your current working directory.",
		Args: Arguments{
			{
				Identifier: "path",
				Required:   false,
			},
		},
		Run: CdCommand,
	}.Register()

	Command{Name: "ls", Short: "List all files in a directory.", Args: nil, Run: LsCommand}.Register()
	Command{Name: "dir", Short: "Open your FyUTILS directory.", Args: nil, Run: DirCommand}.Register()
	Command{Name: "update", Short: "Update your FyUTILS instance to the newest version.", Args: nil, Run: UpdateCommand}.Register()
	Command{Name: "help", Short: "Show the help about all the commands.", Args: nil, Run: HelpCommand}.Register()
	Command{Name: "sys", Short: "Show system and FyUTILS related information", Args: nil, Run: SysCommand}.Register()
	Command{Name: "clear", Short: "Clear the console screen", Args: nil, Run: ClearCommand}.Register()
	Command{Name: "exit", Short: "Gracefully exit FyUTILS", Args: nil, Run: ExitCommand}.Register()
}

func (cmd Command) Register() {
	Commands = append(Commands, cmd)
}

func (cmd Command) Unregister() {
	for i, command := range Commands {
		if command.Name == cmd.Name {
			Commands = append(Commands[:i], Commands[i+1:]...)
		}
	}
}
