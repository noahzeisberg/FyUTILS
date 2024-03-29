package main

import (
	"context"
	"fmt"
	"github.com/google/go-github/github"
	"github.com/noahzeisberg/FyUTILS/color"
	"github.com/noahzeisberg/FyUTILS/log"
	"github.com/noahzeisberg/FyUTILS/networking/requests"
	"math"
	"os"
	"strings"
	"sync"
	"time"
)

func ParseRepository(repo string) (string, string) {
	if strings.Contains(repo, "/") {
		return strings.ToLower(strings.Split(repo, "/")[0]), strings.ToLower(strings.Split(repo, "/")[1])
	} else {
		return "noahonfyre", strings.ToLower(repo)
	}
}

func FetchRepositoryContent(pkg string, path string, start time.Time) {
	owner, repository := ParseRepository(pkg)
	pkg = owner + "/" + repository
	packageDirectory := FuelDir + owner + "." + repository + "\\"

	log.Print("Fetching FUEL " + color.Blue + pkg + color.Reset + "...")

	_, repositoryContents, r, err := githubClient.Repositories.GetContents(context.Background(), owner, repository, path, nil)
	if err != nil {
		log.Error(err.Error())
		return
	}
	log.Print("Server returned " + color.Blue + fmt.Sprint(r.StatusCode) + color.Reset + " via " + r.Proto)

	err = os.MkdirAll(packageDirectory+strings.ReplaceAll(path, "/", "\\"), os.ModePerm)
	if err != nil {
		log.Error(err.Error())
		return
	}

	var wg sync.WaitGroup
	wg.Add(len(repositoryContents))

	for _, props := range repositoryContents {
		go func(props *github.RepositoryContent) {
			if props.GetType() != "file" {
				log.Print("Not a file! Skipping " + props.GetName() + "...")
				wg.Done()
				return
			}

			file, err := os.Create(packageDirectory + props.GetName())
			if err != nil {
				log.Error(err.Error())
				return
			}

			fileContent := requests.Get(props.GetDownloadURL())

			bytesWritten, err := file.Write(fileContent)
			if err != nil {
				log.Error(err.Error())
				return
			}

			err = file.Close()
			if err != nil {
				log.Error(err.Error())
				return
			}

			log.Print("File " + color.Blue + props.GetName() + color.Reset + " successfully collected! " + color.Gray + "(" + fmt.Sprint(bytesWritten) + " bytes)")

			wg.Done()
		}(props)
	}

	wg.Wait()
	log.Print("Successfully collected package " + color.Blue + pkg + color.Reset + "! " + color.Gray + "(" + fmt.Sprint(math.Round(time.Since(start).Seconds())) + "s)")
}
