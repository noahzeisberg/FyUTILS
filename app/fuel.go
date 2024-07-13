package app

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

func ParseRepository(input string) (FuelPackage, error) {
	unparsedRepoString, branch, _ := strings.Cut(input, "@")
	if branch == "" {
		branch = "master"
	}

	owner, repository, _ := strings.Cut(unparsedRepoString, "/")
	if owner == unparsedRepoString {
		owner = "noahzeisberg"
	}

	if repository == "" {
		repository = unparsedRepoString
	}

	return FuelPackage{
		Owner:      owner,
		Repository: repository,
		Branch:     branch,
	}, nil
}

func (pkg FuelPackage) AsPackage() string {
	return pkg.Owner + "." + pkg.Repository
}

func (pkg FuelPackage) AsRepository() string {
	return pkg.Owner + "/" + pkg.Repository
}

func FetchRepositoryContent(input string, path string, start time.Time) {
	pkg, err := ParseRepository(input)
	if err != nil {
		log.Error(err.Error())
		return
	}
	packageDirectory := FuelDir + pkg.AsPackage() + "\\"

	log.Print("Fetching FUEL " + color.Blue + pkg.AsRepository() + color.Reset + "...")

	_, repositoryContents, res, err := githubClient.Repositories.GetContents(context.Background(), pkg.Owner, pkg.Repository, path, &github.RepositoryContentGetOptions{Ref: pkg.Branch})
	if err != nil {
		log.Error(err.Error())
		return
	}
	log.Print("Server returned " + color.Blue + fmt.Sprint(res.StatusCode) + color.Reset + " via " + res.Proto)

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
	log.Print("Successfully collected package " + color.Blue + pkg.AsRepository() + color.Reset + "! " + color.Gray + "(" + fmt.Sprint(math.Round(time.Since(start).Seconds())) + "s)")
}
