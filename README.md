<div align="center">
  <img height="200" src="img\FyUTILS.png" width="200"/>
</div>

# FyUTILS

FyUTILS is a simple python hacking and utility terminal application for windows including tools like a denial of service initiator, a port scanner and several more. FyUTILS comes with an integrated package manager, community driven libraries and plenty of other features.

![Language](https://img.shields.io/badge/dynamic/json?color=blue&label=Language&query=language&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNoahOnFyre%2FFyUTILS&style=for-the-badge)
![GitHub all releases](https://img.shields.io/github/downloads/NoahOnFyre/FyUTILS/total?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/NoahOnFyre/FyUTILS?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/NoahOnFyre/FyUTILS?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/NoahOnFyre/FyUTILS?style=for-the-badge)

## Table of contents (TOC)
<!-- TOC -->
* [FyUTILS](#fyutils)
  * [Table of contents (TOC)](#table-of-contents-toc)
  * [Authors and Contributors](#authors-and-contributors)
* [Documentation](#documentation)
  * [Prerequisites](#prerequisites)
  * [Stable installation (Recommended)](#stable-installation-recommended)
  * [Developer installation](#developer-installation)
  * [First Launch](#first-launch)
  * [How to use](#how-to-use)
  * [Prefix](#prefix)
  * [Libraries](#libraries)
  * [Commands](#commands)
    * [Flood](#flood)
    * [Portscan](#portscan)
    * [WIRE](#wire)
    * [Resolve](#resolve)
    * [ARP](#arp)
    * [Vars](#vars)
    * [Checkport](#checkport)
    * [SSH](#ssh)
    * [Fetch](#fetch)
    * [YouTube](#youtube)
    * [Log](#log)
    * [Config](#config)
    * [StreamHunter](#streamhunter)
    * [GetIP](#getip)
    * [FUELS](#fuels)
    * [FUEL](#fuel)
    * [Update](#update)
    * [Edit](#edit)
    * [Calc](#calc)
    * [Read](#read)
    * [LS](#ls)
    * [Shell](#shell)
    * [Exit](#exit)
    * [CD](#cd)
    * [Help](#help)
    * [Raise](#raise)
    * [Clear & rl](#clear--rl)
    * [Restart & rs](#restart--rs)
* [License](#license)
* [Things used in FyUTILS](#things-used-in-fyutils)
    * [Languages](#languages)
    * [Programs](#programs)
    * [APIs](#apis)
    * [Updating System](#updating-system)
    * [Rich Presence libraries](#rich-presence-libraries)
    * [Networking libraries](#networking-libraries)
    * [Utility libraries](#utility-libraries)
    * [Development tools](#development-tools)
<!-- TOC -->

## Authors and Contributors

- Project owner: [@NoahOnFyre](https://www.github.com/NoahOnFyre)
- Issues: [@NoahOnFyre](https://www.github.com/NoahOnFyre)
- Maintainer: [@NoahOnFyre](https://www.github.com/NoahOnFyre)
- Documentation writing: [@NoahOnFyre](https://www.github.com/NoahOnFyre)

# Documentation
This Documentation will guide you through the installation, the first launch and configuration and the daily use of FyUTILS.

## Prerequisites

**NOTE:** This tool is made for Windows. Many features **won't** work on **Linux** or **macOS**. The documentation will only guide you through the installation steps on Windows 11 (on Windows 10 and earlier it's literally the same process).
If you don't already have **Python 3.10 or higher** with **PIP** installed, you can download it [here](https://www.python.org/downloads/)

If you want to install the developer version, make sure you have [Git](https://git-scm.com) installed on your PC.

## Stable installation (Recommended)

To install the latest stable FyUTILS version, download all assets of a published release.
We always recommend you to use the latest version of FyUTILS, so we can guarantee you the latest features, bugfixes and fixed security vulnerabilities. You can find the latest release [here](https://github.com/NoahOnFyre/FyUTILS/releases/latest).
Put your downloaded files into a directory of your choice, open up PowerShell or Command Prompt in this directory and run the following command:

```
pip install -r requirements.txt
```

## Developer installation
Using the newest version that may be in development will give you the newest features, but may contain bugs or vulnerabilities.

Open up PowerShell or Command Prompt and clone the GitHub repository by running:
```
git clone https://github.com/NoahOnFyre/FyUTILS %userprofile%\Desktop\FyUTILS
```
If the command causes errors, check if your desktop is locally stored on your machine or on OneDrive. If so, just use:

```
git clone https://github.com/NoahOnFyre/FyUTILS %userprofile%\OneDrive\Desktop\FyUTILS
```

Go into your directory using:
```
cd %userprofile%\Desktop\FyUTILS
```
or

```
cd %userprofile%\OneDrive\Desktop\FyUTILS
```

Now run the following command to install the dependencies from the requirement.txt file.
```
pip install -r requirements.txt
```
## First Launch

After installing the dependencies for FyUTILS you can start it by either entering:
```
python main.py
```
Or by just double-clicking on the **main.py**.
## How to use
FyUTILS has a very large amount of commands you can execute and try out. But some important information you need is the structure of commands.

Every command you'll execute in FyUTILS is structured in different units. We take for example the `flood` command. Here you can see a basic operation with the command:

```
flood 82.169.42.61 80
```

What this command does will be explained later, but you can see we have several spaces which **structure** the request. So let's put them in a table and go through them.

| Used in example | Abbreviation | Required | Description                                 |
|-----------------|--------------|----------|---------------------------------------------|
| flood           | command      | true     | The command you want to run.                |
| 82.169.42.61    | target       | true     | The IP address or the domain of the target. |
| 80              | port         | true     | The port of the target you want to attack.  |

When an argument is required it will be bordered by < and >.
When it isn't required it will be bordered by [ and ]

Every command is structured like this, but all of them have a different amount of arguments. Some commands can also have no arguments like `ls`.

## Prefix

Here you can find everything you need to understand the **prefix** in FyUTILS.

Here's an example:

```
[16:32:00] [FyUTILS/INFO] Stuff after prefix like text.
```

| Used in example               | Description                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------|
| 16:32:00                      | Current time based on your timezone etc.                                                   |
| FyUTILS/                      | Protocol layer (Some short, additional information about what FyUTILS is doing right now.) |
| INFO                          | Logging level (e.g. INFO, ERROR or WARN)                                                   |
| Stuff after prefix like text. | Stuff after the prefix (I think this is obvious)                                           |

## Libraries
FUELS (FyUTILS extending libraries) are simple lightweight scripts that can add a certain behaviour or action when you execute a command.
At the moment you can contribute by [Forking](https://github.com/NoahOnFyre/FUELS/fork) the repository, add your FUEL and create a [Pull Request](https://github.com/NoahOnFyre/FUELS/pulls) by clicking on **Contribute** and then on **New pull request**.
Then you have to wait for a FUEL or project maintainer to verify that your FUEL is safe and doesn't contain malware or other malicious stuff.
When you want to update your FUEL, make sure that your fork is up-to-date with **master** on NoahOnFyre/FUELS. You can ensure this by clicking on **Sync fork** and then on **Update branch**.

Information about contributing to FUELS in the official repository may be outdated.

## Commands
The commands in FyUTILS are very simple. Below, there's a list of all commands and the arguments they take.

### Flood
```
flood <target> <port>
```
Flood will launch a denial of service attack on target:port. It can be very powerful, so be aware, because you'll maybe lose internet connection for a few seconds or minutes.
### Portscan
```
portscan <target>
```
Portscan scans for opened ports on the target.
### WIRE
```
wire <action> [target/argument]
```
WIRE is a tool package including several wireless hacking tools for Wi-Fi and Bluetooth. The target or argument will depend on which action you want to execute.
### Resolve
```
resolve <ip/phone/domain> <target>
```
Resolves information about the specified target. If the target is a domain, the IPv4 address will be returned too.
### ARP
```
arp
```
ARP (Address resolution protocol) scans for devices in your current network and lists up its IP address and MAC address.
### Vars
```
vars
```
Vars will list up all system variables set by FyUTILS.
### Checkport
```
checkport <target> <port>
```
Checkport checks if the port on the target is open. You can use this tool to double-check a port you resolved using `portscan`.
### SSH
```
ssh <host> <port> <username>
```
SSH will initiate a secure shell connection to the host on the specified port with the given credentials (Username & Password)

You'll have to enter a password after running the commands. Your input will be censored.
### Fetch
```
fetch <url> <filename>
```
Fetch downloads a file or a website, that can be saved to a file in your content directory. You need to specify the name of the file too.
### YouTube
```
youtube <video_url>
```
This command will download the highest definition file of a YouTube video (most likely HD).
### Log
```
log
```
Opens the folder, your log files are in and automatically highlights the **crash.log**
### Config
```
config [action]
```
When you run it without arguments, the config file will be opened for writing. If you run it as `config reset`, the config will be reset to the defaults.
### StreamHunter
```
streamhunter
```
Runs a lite an optimised instance of my fork of StreamHunter by Eltotiz.
### GetIP
```
getip
```
Returns your current public IP address. Be careful using this in front of people.
### FUELS
```
fuels
```
FUELS lists all the installed and registered FUELs associated with FyUTILS.
### FUEL
```
fuel <install/remove> <package_name>
```
The FUEL command has multiple different actions. One of them is `fuel install`. It will install a verified FUEL, found in [NoahOnFyre/FUELS](https://github.com/NoahOnFyre/FUELS) and register it. `fuel remove` will unregister and delete the FUEL.
### Update
```
update
```
The update command automatically updates FyUTILS to the newest version found in the [Releases section](https://github.com/NoahOnFyre/FyUTILS/releases).
### Edit
```
edit <file>
```
Using edit, you can easily edit files using your terminal. If the file doesn't exist, you can either cancel the process or let FyUTILS create a new file and open it.
### Calc
```
calc <calculation>
```
With calc, you can calculate any calculation like 3*7 or 20+1.

WARNING: Decimal calculations are currently NOT supported and may produce false results.
### Read
```
read <file>
```
You can read files with this command. It's very similar to the `edit` command.
### LS
```
ls
```
`ls` does the same thing, it does in a UNIX environment. It'll list all files in the directory you're currently in.
### Shell

```
shell <args>
```
Will execute the given system default command with the given arguments.
### Exit
```
exit
```
I think I don't need to explain what this command does.
### CD
```
cd [directory]
```
`cd` changes your current working directory to the directory in argument one. In this case, argument one is not necessary, so if you leave it out, `cd` will just return the directory you're currently in.

DISCLAIMER: FyUTILS modifies the paths of directory and files to feel more like a UNIX environment.
### Help
```
help
```
The help command will bring up this page here, so you can look up the syntax of a command or if you just need help using commands.
### Raise
```
raise
```
Raises an exception (primarily used for debug purposes)
### Clear & rl
```
clear / rl
```
Reloads FyUTILS
### Restart & rs
```
restart / rs
```
Restarts FyUTILS

# License

[FyUTILS Exclusive Publishing License (FUEPL)](https://github.com/NoahOnFyre/FyUTILS/blob/master/LICENSE)

# Things used in FyUTILS
All tools, languages and whatever I used for FyUTILS
### Languages
| Language | Used for            |
|----------|---------------------|
| Python   | Client Application  |
| JSON     | Libraries (FUELS)   |
| Batch    | System interactions |
| Markdown | Documentation       |

### Programs
- [NoahOnFyre's fork](https://github.com/NoahOnFyre/StreamHunter) of [StreamHunter by Eltotiz](https://github.com/Eltotiz/StreamHunter) (Lite version)

### APIs
- [IP WhoIs](http://ipwho.is/)
- [Ipify](http://ipify.org/)

### Updating System
- [GitHub API](https://api.github.com)

### Rich Presence libraries
- DiscordRPC (pypresence)

### Networking libraries
- Requests (requests)
- Scapy (scapy)
- SSH (paramiko)
- PyTube (pytube)

### Utility libraries
- PhoneNumbers (phonenumbers)
- Colorama (colorama)
- DateTime (datetime)
- Process and System Util (psutil)
- Password Input (pwinput)

### Development tools

| Used for                                  | Tool                                                                                         |
|-------------------------------------------|----------------------------------------------------------------------------------------------|
| Code writing & Debugging                  | [PyCharm](https://jetbrains.com/pycharm/download)                                            |
| Documentation                             | [PyCharm](https://jetbrains.com/pycharm/download) & [Visual Studio Code](https://vscode.dev) |
| FUEL Development                          | [Visual Studio Code](https://vscode.dev)                                                     |
| Version control, Publishing, Distribution | [GitHub](https://github.com)                                                                 |


Thanks to the creators of these tools and libraries and to everyone supporting me during development through issues and other contributions. ❤️