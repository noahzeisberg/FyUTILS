# FyUTILS 2.X.X (FyUTILS Go)
FyUTILS is a CLI hacking, networking and utility tool for all platforms.

# Installation

## Nitro installation
You can install FyUTILS by running the following command in the Nitro CLI:
```
install fyutils
```

## Default installation
### Windows
Download the setup.bat and the .exe file out of the [latest release](https://github.com/NoahOnFyre/FyUTILS/releases/latest). Open up a command prompt in your current directory and run:
```
setup
```
This will run all installation steps.
After the setup has completed, you can start FyUTILS with the `fyutils` command.

### Other OS
If you want to install FyUTILS on another OS you'll have to compile yourself. Just download or clone the repository, make sure you have Go installed and run the build using:
```
go build -o FyUTILS -v
```
Move the binary file to a location where it's easy accessable and start it to initialize the FyUTILS components.