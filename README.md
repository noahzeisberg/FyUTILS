# FyUTILS
A simple python hacking terminal application for windows with some more commands than in the default windows command prompt.

# Light documentation (Getting started)

First, you need to install the PyPi librarys by running:

`pip install -r requirements.txt`

Note: The requirements file won't work for any legacy versions. Every version whose librarys can be installed with those files, can be found in the [Release Section](https://github.com/NoahOnFyre/FyUTILS/releases)

Now you can start FyUTILS by double-clicking on the "main.py" file.

Once the initialisation process has passed, you should have an input field. There you can execute any windows default command, but there are some special commands.

## Flood

The first one i'd like to talk about is the `flood` command. You can use it to send very big data packages to a target IP/domain. Everything you have to enter is the IP/domain and the port you want to send these packages to.

## Portscan

The name of the `portscan` command already tells you what you can do with this command. You have to enter a target IP/domain and FyUTILS will get all open ports on this target. These port numbers you can use for the `flood` command.

## Exit

I think I don't need to explain you the usage of the `exit` command, right?

## Clear, Cls and Rl

The base command for the action is the `clear` command. This is the only command, that have a large amount of aliases to use. Some of them are `cls` and `rl`.

## SSH

The `ssh` command will run an SSH session on the target with the given credentials. Those are: Target IP/domain, SSH port, Username and Password.
SSH is the short form of [Secure Shell](https://de.wikipedia.org/wiki/Secure_Shell). If you don't know anything about it, you can check out the Wikipedia page of [Secure Shell](https://de.wikipedia.org/wiki/Secure_Shell).

## Display

`display` will send a http/https request to the given web server. FyUTILS will also print out the ping latency. It will send a request every half a minute.

## Restart

`restart` will just restart FyUTILS. It's useful for applying an update or something.

## Calc and Calculate

`calc` is a simple calculator. You can use `calculate` too. Example: `║ Calculate > 1+1`

`[19:06:35] [FyUTILS/INFO] 1+1 is 2`

## Fetch

`fetch` can be used for downloading files and websites. Its argument is the URL of the file/website.

## YouTube

`youtube` lets you download a YouTube video. The arguments of this commands are just the YouTube URL of the video.

## FUEL

`fuel` lets you easily add FUELS to FyUTILS. You just need to enter the path of the FUEL and it will be copied to the FUEL save directory.

## FUELs

`fuels` will list every FUEL that is currently installed and running.
