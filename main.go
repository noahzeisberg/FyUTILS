package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/hugolgst/rich-go/client"
)

var (
	scanner = bufio.NewScanner(os.Stdin)

	version        string    = "2.0.0"
	username, _              = strings.CutPrefix(ValueOf(os.UserHomeDir()), "C:\\Users\\")
	device, _                = os.Hostname()
	appdata_dir, _           = os.UserHomeDir()
	main_dir       string    = appdata_dir + "\\.fyutils"
	config_path    string    = main_dir + "\\config.json"
	config         Config    = GetDefaultConfig()
	rpc_active     bool      = false
	state          string    = ""
	start_time     time.Time = time.Now()

	commands = []Command{}
)

func main() {
	SetState("Initializing...")
	Print(Prefix(0) + "Initializing...")

	SetState("Checking paths...")
	Print(Prefix(0) + "Checking paths...")

	paths_fixed := CheckPaths([]string{
		appdata_dir,
		main_dir,
	})

	Print(Prefix(0) + "Fixed " + strconv.Itoa(paths_fixed) + " paths!")

	SetState("Checking config...")
	Print(Prefix(0) + "Checking config...")

	if !Exists(config_path) {
		var dst bytes.Buffer
		content, err := json.Marshal(config)
		json.Indent(&dst, content, "", "	")

		if err != nil {
			Print(Prefix(2) + "Failed to parse default config: " + err.Error())
		}

		os.WriteFile(config_path, dst.Bytes(), os.ModePerm)
	}

	SetState("Initializing config...")
	Print(Prefix(0) + "Initializing config...")
	unparsed, err := os.ReadFile(config_path)

	if err != nil {
		Print(Prefix(2) + "Failed to open config file: " + err.Error())
	}

	err = json.Unmarshal(unparsed, &config)

	if err != nil {
		Print(Prefix(2) + "Failed to parse config.")
	}

	if config.EnableDiscordRPC {
		SetState("Starting discord RPC...")
		Print(Prefix(0) + "Starting discord RPC...")
		go func() {
			err := client.Login("1141702837810769950")

			if err == nil {
				rpc_active = true
			}
		}()
	}

	SetState("Registering commands...")
	Print(Prefix(0) + "Registering commands...")
	CommandRegistration()

	SetState("Starting up...")
	Print(Prefix(0) + "Starting up...")
	MainMenu()
	SetState("Initialization completed!")

	for {
		SetState("Idle")
		Print()
		command, args := CommandInput()
		SetState("Running " + command + "...")
		Print()

		RunCommand(command, args)
	}
}
