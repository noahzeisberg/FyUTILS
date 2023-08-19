package main

type Config struct {
	EnableDiscordRPC bool   `json:"discord_rpc_enabled"`
	EnableDebugMode  bool   `json:"enable_debug"`
	UseAuth          bool   `json:"gh_api_auth"`
	AuthToken        string `json:"gh_api_token"`
	AuthName         string `json:"gh_api_username"`
	UploadLogs       bool   `json:"upload_logs"`
	UpdatingBranch   string `json:"branch"`
}

func GetDefaultConfig() Config {
	return Config{
		EnableDiscordRPC: true,
		EnableDebugMode:  false,
		UseAuth:          false,
		AuthToken:        "",
		AuthName:         "",
		UploadLogs:       true,
		UpdatingBranch:   "master",
	}
}
