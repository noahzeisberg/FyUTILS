package app

import "github.com/noahzeisberg/FyUTILS/typing"

func CommandRegistration() {
	typing.Command{
		Name:  "flood",
		Short: "Run a denial of service attack on the target.",
		Args: []typing.Argument{
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
	}.Register(&Commands)

	typing.Command{
		Name:  "portscan",
		Short: "Scan for open ports on the target.",
		Args: []typing.Argument{
			{
				Identifier: "ip",
				Required:   true,
			},
		},
		Run: PortscanCommand,
	}.Register(&Commands)

	typing.Command{
		Name:  "whois",
		Short: "Gather WHOIS information about the target.",
		Args: []typing.Argument{
			{
				Identifier: "ip",
				Required:   true,
			},
		},
		Run: WhoisCommand,
	}.Register(&Commands)

	typing.Command{
		Name:  "retrieve",
		Short: "Retrieve local information.",
		Args: []typing.Argument{
			{
				Identifier: "item",
				Required:   true,
			},
		},
		Run: RetrieveCommand,
	}.Register(&Commands)

	typing.Command{
		Name:  "sniff",
		Short: "Capture traffic of a specific interface.",
		Args: []typing.Argument{
			{
				Identifier: "interface",
				Required:   true,
			},
		},
		Run: SniffCommand,
	}.Register(&Commands)

	typing.Command{
		Name:  "fetch",
		Short: "Download a file from the specific URL.",
		Args: []typing.Argument{
			{
				Identifier: "url",
				Required:   true,
			},
		},
		Run: FetchCommand,
	}.Register(&Commands)

	typing.Command{
		Name:  "cd",
		Short: "Change your current working directory.",
		Args: []typing.Argument{
			{
				Identifier: "path",
				Required:   false,
			},
		},
		Run: CdCommand,
	}.Register(&Commands)

	typing.Command{Name: "ls", Short: "List all files in a directory.", Args: nil, Run: LsCommand}.Register(&Commands)
	typing.Command{Name: "dir", Short: "Open your FyUTILS directory.", Args: nil, Run: DirCommand}.Register(&Commands)
	typing.Command{Name: "update", Short: "Update your FyUTILS instance to the newest version.", Args: nil, Run: UpdateCommand}.Register(&Commands)
	typing.Command{Name: "help", Short: "Show the help about all the commands.", Args: nil, Run: HelpCommand}.Register(&Commands)
	typing.Command{Name: "clear", Short: "Clear the console screen", Args: nil, Run: ClearCommand}.Register(&Commands)
	typing.Command{Name: "exit", Short: "Gracefully exit FyUTILS", Args: nil, Run: ExitCommand}.Register(&Commands)
}
