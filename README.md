# FyUTILS 2.X.X (FyUTILS Go)
FyUTILS is a hacking, networking and utility CLI tool for all platforms.

![nitro](/badges/nitro.svg)
![golang](/badges/golang.svg)
![github](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/github_vector.svg)

# Disclaimer
Hacking is illegal. This tool is only made for ethical purposes like analysing your own infrastructure. You'll be responsible for everything you do with this tool.

# Installation
How can I install it?

## Nitro installation
You can install FyUTILS by running the following command in the [Nitro CLI](https://github.com/NoahOnFyre/Nitro) (Requires Nitro 1.1.0):
```
install fyutils
```

## Default installation
How to install without using Nitro.

### Windows
Download the setup.bat and the .exe file out of the [latest release](https://github.com/NoahOnFyre/FyUTILS/releases/latest). Open up a command prompt in your current directory and run:
```
setup
```
This will run all installation steps.
After the setup has completed, you can start FyUTILS with the `fyutils` command.

### Other OS
If you want to install FyUTILS on another OS you'll have to compile yourself. Just download or clone the repository, make sure you have Go installed and create the build using:
```
go build -o FyUTILS -v
```
Move the binary file to a location where it's easy accessable and start it to initialize the FyUTILS components.

