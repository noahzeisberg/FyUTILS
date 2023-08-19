package main

import (
	"bufio"
	"bytes"
	"context"
	"encoding/json"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/google/go-github/github"
	"github.com/hugolgst/rich-go/client"
	"golang.org/x/mod/semver"
)

var (
	scanner = bufio.NewScanner(os.Stdin)

	version          string    = "2.0.0"
	username, _                = strings.CutPrefix(ValueOf(os.UserHomeDir()), "C:\\Users\\")
	device, _                  = os.Hostname()
	appdata_dir, _             = os.UserHomeDir()
	current_dir, _             = os.Getwd()
	main_dir         string    = appdata_dir + "\\.fyutils"
	config_path      string    = main_dir + "\\config.json"
	config           Config    = GetDefaultConfig()
	rpc_active       bool      = false
	state            string    = ""
	start_time       time.Time = time.Now()
	gh_client                  = github.NewClient(nil)
	update_available bool      = false
	newest_version   string    = ""

	commands = []Command{}
)

func main() {
	SetState("Initializing...")
	Print(Prefix(0) + "Initializing...")

	wg := sync.WaitGroup{}
	wg.Add(1)

	/////////////////////////
	// Path initialization //
	/////////////////////////
	SetState("Checking paths...")
	Print(Prefix(0) + "Checking paths...")

	paths_fixed := CheckPaths([]string{
		appdata_dir,
		main_dir,
	})

	Print(Prefix(0) + "Fixed " + strconv.Itoa(paths_fixed) + " paths!")

	////////////////////
	// Update checker //
	////////////////////

	go func() {
		SetState("Checking for updates...")
		Print(Prefix(0) + "Checking for updates...")

		update_available = false

		latest_release, _, err := gh_client.Repositories.GetLatestRelease(context.Background(), "NoahOnFyre", "FyUTILS")

		if err != nil {
			Print(Prefix(2) + "GitHub API request failed! " + err.Error())
		}

		if semver.Compare("v"+version, "v"+latest_release.GetTagName()) != 0 {
			update_available = true
			newest_version = latest_release.GetTagName()
		}
		wg.Done()
	}()

	////////////////////
	// Config checker //
	////////////////////

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

	///////////////////////////
	// Config initialization //
	///////////////////////////

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

	////////////////////////////////
	// Discord RPC initialization //
	////////////////////////////////

	if config.EnableDiscordRPC {
		go func() {
			SetState("Starting discord RPC...")
			Print(Prefix(0) + "Starting discord RPC...")

			err := client.Login("1141702837810769950")

			if err == nil {
				rpc_active = true
			}
		}()
	}

	//////////////////////////
	// Command registration //
	//////////////////////////

	SetState("Registering commands...")
	Print(Prefix(0) + "Registering commands...")

	CommandRegistration()

	///////////////////////
	// Finish init steps //
	///////////////////////

	SetState("Starting up...")
	Print(Prefix(0) + "Starting up...")

	SetState("Initialization completed!")
	Print(Prefix(0) + "Initialization completed!")

	SetState("Waiting for goroutines to finish...")
	Print(Prefix(0) + "Waiting for goroutines to finish...")

	wg.Wait()

	MainMenu()

	for {
		SetState("Idle")
		Print()
		command, args := CommandInput()
		SetState("Running " + command + "...")
		Print()

		RunCommand(command, args)
	}
}
