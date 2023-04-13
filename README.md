# FyUTILS
A simple python hacking and utility terminal application for windows with an integrated package manager, community driven librarys and plenty of other features.



## Getting started with FyUTILS

Please make sure you're using FyUTILS in a Windows environment since it's "native" for windows only. Most

First, open up a command prompt window as administrator and go to the directory, your main.py is located:

`cd path/to/fyutils/directory`

Then, you need to install the PyPi librarys by running:

`pip install -r requirements.txt`

Note: The requirements file won't work for any legacy versions. Every version whose librarys can be installed with those files, can be found in the [Release Section](https://github.com/NoahOnFyre/FyUTILS/releases)

Now you can start FyUTILS by double-clicking on the "main.py" file.
Once the initialisation process has passed, you should have an input field. There you can execute any windows default command, but there are some special commands.
But before the explanation, you need to know how to execute commands.
The format of every command is the same: `command_name arg1 arg2 arg3 ...` and so on.
So there is one command name and then the arguments. Those are most likely not more than 5. The average amount of arguments is 1-3.
Some command doesn't even need an argument, like `ls` or `restart`.

## Flood

The first one I'd like to talk about is the `flood` command. You can use it to send very big data packages to a target IP/domain. Everything you have to enter is the IP/domain and the port you want to send these packages to.

Usage: `flood <target> <port>`

## Portscan

The name of the `portscan` command already tells you what you can do with this command. You have to enter a target IP/domain and FyUTILS will get all open ports on this target. These port numbers you can use for the `flood` command.

Usage: `portscan <target>`

## Exit

I think I don't need to explain you the usage of the `exit` command, right?

Usage: `exit`

## Clear, Reload and Rl

The base command for the action is the `clear` command. This is the only command, that have a large amount of aliases to use. Some of them are `reload` and `rl`.

Usage: `clear`, `reload`, `rl`

## SSH

The `ssh` command will run an SSH session on the target with the given credentials.
SSH is the short form of [Secure Shell](https://de.wikipedia.org/wiki/Secure_Shell).

Usage: `ssh <server> <port> <username>`

NOTE: You'll have to enter your password shortly after running the command. It will be censored on enter.

## Restart

`restart` will just restart FyUTILS. It's useful for applying an update or something.

Usage: `restart`

## Calc

`calc` is a simple calculator. Just enter for example `calc 9*2`

Usage: `calc <calculation>`

## Fetch

`fetch` can be used for downloading files and websites.

Usage: `fetch <url> <filename>`

## YouTube

`youtube` lets you download a YouTube video.

Usage: `youtube <video_url>`

## FUEL

`fuel` lets you easily add FUELS to FyUTILS.

Usage: `fuel <install/remove/add> <fuel_name>`

## FUELs

`fuels` will list every FUEL that is currently installed and running.

Usage: `fuels`

## Edit

Using `edit` you can write content to files. If the file doesn't exists, you can either create it or cancel the process.

Usage: `edit <filename>`

## LS

`ls` does the same thing `ls` does in a UNIX environment. It lists all files in a directory. Hidden files or folders will be slightly gray, directories are green and marked with a slash in front of the name and normal files are white.

Usage: `ls`
