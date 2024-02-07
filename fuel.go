package main

import (
	"context"
	"encoding/json"
	"fmt"
	"github.com/NoahOnFyre/gengine/color"
	"github.com/NoahOnFyre/gengine/networking/requests"
	"github.com/google/go-github/github"
	"math"
	"os"
	"os/exec"
	"strings"
	"sync"
	"time"
)

func ParseRepository(repo string) (string, string) {
	if strings.Contains(repo, "/") {
		return strings.Split(repo, "/")[0], strings.Split(repo, "/")[1]
	} else {
		return "noahonfyre", strings.ToLower(repo)
	}
}

func FetchRepositoryContent(pkg string, path string, start time.Time) {
	owner, repository := ParseRepository(pkg)
	pkg = owner + "/" + repository
	packageDirectory := fuelDir + owner + "." + repository + "\\"

	Print("Fetching FUEL " + color.Blue + pkg + color.Reset + "...")

	_, repositoryContents, r, err := githubClient.Repositories.GetContents(context.Background(), owner, repository, path, nil)
	if err != nil {
		Error(err.Error())
		return
	}
	Print("Server returned " + color.Blue + fmt.Sprint(r.StatusCode) + color.Reset + " via " + r.Proto)

	err = os.MkdirAll(packageDirectory+strings.ReplaceAll(path, "/", "\\"), os.ModePerm)
	if err != nil {
		Error(err.Error())
		return
	}

	var wg sync.WaitGroup
	wg.Add(len(repositoryContents))

	for _, props := range repositoryContents {
		go func(props *github.RepositoryContent) {
			if props.GetType() != "file" {
				Print("Not a file! Skipping " + props.GetName() + "...")
				wg.Done()
				return
			}

			file, err := os.Create(packageDirectory + props.GetName())
			if err != nil {
				Error(err.Error())
				return
			}

			fileContent := requests.Get(props.GetDownloadURL())

			bytesWritten, err := file.Write(fileContent)
			if err != nil {
				Error(err.Error())
				return
			}

			err = file.Close()
			if err != nil {
				Error(err.Error())
				return
			}

			Print("File " + color.Blue + props.GetName() + color.Reset + " successfully collected! " + color.Gray + "(" + fmt.Sprint(bytesWritten) + " bytes)")

			wg.Done()
		}(props)
	}

	wg.Wait()

	var fuelpackage FuelManifest
	file, err := os.ReadFile(fuelDir + owner + "." + repository + "\\fuelpackage.json")
	if err != nil {
		Error(err.Error())
		return
	}

	err = json.Unmarshal(file, &fuelpackage)
	if err != nil {
		Error(err.Error())
		return
	}

	if fuelpackage.Repository == owner+"/"+repository {
		if fuelpackage.Type == "extension" && fuelpackage.Extension.NeedsBuilding {
			Print("Building application...")
			err = exec.Command(fuelpackage.Extension.BuildCommand).Run()
			if err != nil {
				Error(err.Error())
				return
			}
		} else {
			Error("FUEL is not executable!")
		}
	} else {
		Error("FUEL validation failure")
	}
	Print("Successfully collected package " + color.Blue + pkg + color.Reset + "! " + color.Gray + "(" + fmt.Sprint(math.Round(time.Since(start).Seconds())) + "s)")
}
