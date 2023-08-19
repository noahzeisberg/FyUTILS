package main

type Arguments []string

func CommandRegistration() {
	RegisterCommand("flood", "Run a denial of service attack on the target.", Arguments{"addr", "port"}, FloodCommand)
	RegisterCommand("portscan", "Scan for open ports on the target.", Arguments{"addr"}, PortscanCommand)
	RegisterCommand("gather", "Gather information about the target.", Arguments{"addr"}, GatherCommand)
	RegisterCommand("test", "Used for debugging and testing.", Arguments{"argument"}, TestCommand)
	RegisterCommand("update", "Update your FyUTILS instance.", Arguments{}, UpdateCommand)
	RegisterCommand("clear", "Clear the console window.", Arguments{}, ClearCommand)
	RegisterCommand("calc", "Calculate an expression.", Arguments{}, CalculatorCommand)
	RegisterCommand("help", "Show some help about the commands.", Arguments{}, HelpCommand)
	RegisterCommand("exit", "Exit the application.", Arguments{}, ExitCommand)
}
