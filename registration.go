package main

import (
	"github.com/noahzeisberg/FyUTILS/regex"
)

func CommandRegistration() {
	Command{
		Name:  "flood",
		Short: "Run a denial of service attack on the target.",
		Args: []Argument{
			{
				Identifier: "ip",
				Required:   true,
				Expect:     regex.AcceptsIP,
			},
			{
				Identifier: "port",
				Required:   true,
				Expect:     regex.AcceptsPort,
			},
		},
		Run: FloodCommand,
	}.Register()

	Command{
		Name:  "portscan",
		Short: "Scan for open ports on the target.",
		Args: []Argument{
			{
				Identifier: "ip",
				Required:   true,
				Expect:     regex.AcceptsIP,
			},
		},
		Run: PortscanCommand,
	}.Register()

	Command{
		Name:  "whois",
		Short: "Gather WHOIS information about the target.",
		Args: []Argument{
			{
				Identifier: "ip",
				Required:   true,
				Expect:     regex.AcceptsIP,
			},
		},
		Run: WhoisCommand,
	}.Register()

	Command{
		Name:  "retrieve",
		Short: "Retrieve local information.",
		Args: []Argument{
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
		Args: []Argument{
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
		Args: []Argument{
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
		Args: []Argument{
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
		Args: []Argument{
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
	Command{Name: "clear", Short: "Clear the console screen", Args: nil, Run: ClearCommand}.Register()
	Command{Name: "exit", Short: "Gracefully exit FyUTILS", Args: nil, Run: ExitCommand}.Register()
}

func (cmd Command) Register() {
	Commands = append(Commands, cmd)
}
