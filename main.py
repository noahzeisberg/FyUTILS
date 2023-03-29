import concurrent.futures
import datetime
import json
import multiprocessing
import os
import platform
import random
import shutil
import socket
import sys
import threading
import time

import paramiko
import psutil
import requests
import pwinput
from colorama import Fore, init
from pypresence import Presence
from pathlib import Path
from pytube import YouTube

init(convert=True)

"""
FyUTILS SPECIFIC EXIT-CODES:
0: Successful exit (without error)
1024: Variable error (missing variable)
2048: Initialization error (something went wrong during initialization)
"""


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
    elif type == "FUEL":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.LIGHTMAGENTA_EX + "FUEL" + accent_color() + "] " + text_color()
    elif type == "SHIELD":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.YELLOW + "SHIELD" + accent_color() + "] " + text_color()
    else:
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.WHITE + str(type).upper() + accent_color() + "] " + text_color()


def update_status(status):
    os.system("title FyUTILS " + version + " - " + username + "@" + device + " - " + status)
    try:
        rpc.update(
            state=status, details=username + "@" + device, small_image="python",
            large_image="large",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def update_ssh_status(status):
    os.system("title FyUTILS " + version + " - " + ssh_user + "@" + ssh_server + " - " + status)
    try:
        rpc.update(
            state="[REMOTE] " + status, details=ssh_user + "@" + ssh_server, small_image="ssh",
            large_image="large",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def resolve_fuel_informations(file):
    fuel = open(fuel_content_dir + "\\" + file)
    fuel_json = json.load(fuel)
    fuel_command = fuel_json["command_name"]
    fuel_type = fuel_json["type"]
    fuel_content = fuel_json["content"]
    print(prefix("FUEL") + "FUEL information of: " + file)
    print(prefix("FUEL") + "FUEL command name: " + fuel_command)
    print(prefix("FUEL") + "FUEL type: " + fuel_type)
    print(prefix("FUEL") + "FUEL content: " + fuel_content)
    register_fuel(fuel_command, fuel_type, fuel_content)


def register_fuel(command_name, type, content):
    execute_string = ""
    if type == "system":
        execute_string = "os.system('" + content + "')"
    elif type == "default" or type == "python":
        execute_string = content
    globals()["FUEL_SPECIFIC_COMMAND_VARIABLE_" + command_name] = execute_string
    fuel_command_list.append(command_name)


def menu():
    os.system("cls")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "  __________               _____  __   ________   ________   ______       ________")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \ ")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "  /_/         _\__, /      \____/      /_/        /___/      /_____/      /____/  ")
    time.sleep(0.015)
    print(Fore.LIGHTBLUE_EX + "              /____/                                                              ")
    time.sleep(0.015)
    print("")
    time.sleep(0.015)
    print(accent_color() + "╔" + "═"*119)
    time.sleep(0.015)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Username: " + username)
    time.sleep(0.015)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Device: " + device)
    time.sleep(0.015)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Version: " + version)
    time.sleep(0.015)
    print(accent_color() + "╚" + "═"*119)


# INIT PHASE

# Variable initialisation
try:
    print(prefix("INIT") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INIT") + "Username: " + username)
    device = platform.node()
    print(prefix("INIT") + "Device: " + device)
    start_time = time.time()
    print(prefix("INIT") + "Start time: " + str(start_time))
    current_dir = sys.path.__getitem__(0)
    print(prefix("INIT") + "Directory: " + current_dir)
    version = "1.2.1"
    print(prefix("INIT") + "Version: " + version)
    threads = multiprocessing.cpu_count()
    print(prefix("INIT") + "ThreadWorkers: " + str(threads))
    repository = "https://github.com/NoahOnFyre/FyUTILS"
    print(prefix("INIT") + "Repository: " + repository)
    releases = repository + "/releases"
    print(prefix("INIT") + "Releases: " + releases)
    user_dir = str(Path.home())
    print(prefix("INIT") + "User specific directory: " + user_dir)
    appdata_dir = user_dir + "\\AppData"
    print(prefix("INIT") + "AppData directory: " + appdata_dir)
    fyutils_appdata_dir = user_dir + "\\AppData\\Roaming\\FyUTILS\\"
    print(prefix("INIT") + "FyUTILS AppData directory: " + fyutils_appdata_dir)
    tmp_dir = user_dir + "\\AppData\\Roaming\\FyUTILS\\tmp\\"
    print(prefix("INIT") + "Temp files directory: " + tmp_dir)
    download_url = releases + "/download/" + version + "/main.py"
    print(prefix("INIT") + "Download URL: " + download_url)
    download_content_dir = current_dir + "\\DownloadedContent\\"
    print(prefix("INIT") + "Download Content Location: " + download_content_dir)
    fuel_content_dir = current_dir + "\\FUELS\\"
    print(prefix("INIT") + "FUEL Content Location: " + fuel_content_dir)
    cpu = platform.processor()
    print(prefix("INIT") + "CPU: " + cpu)
    memory_amount = psutil.virtual_memory().total
    print(prefix("INIT") + "Memory amount: " + str(round(memory_amount/1024/1024)) + "MB")
except Exception as e:
    print(prefix("ERROR") + "Failed to get system variables!")
    print(prefix("ERROR") + "Shutting down...")
    print(e)
    os.system("pause")
    sys.exit(2048)

# Discord RPC initialisation
try:
    print(prefix("INIT") + "Initializing discord rich presence... (RPC)")
    rpc = Presence("1005822803997638696")
    print(prefix("INIT") + "Presence ID set to: '1005822803997638696'.")
    print(prefix("INIT") + "Connecting to discord...")
    rpc.connect()
    print(prefix("INIT") + "Discord is connected...")
    update_status("Starting up...")
except:
    print(prefix("ERROR") + "Can't connect with the discord RPC.")
    time.sleep(0.5)

# Multithreading initialisation

print(prefix("INIT") + "Initializing multithreading...")
print(prefix("INIT") + "Setting up ThreadPoolExecutor with " + str(threads) + " threads ...")
executor = concurrent.futures.ThreadPoolExecutor(threads, "Worker-")
for i in range(threads):
    print(prefix("INIT") + "Worker-" + str(i+1) + " is online!")
    time.sleep(0.015)
time.sleep(0.5)

# FUEL initialisation

print(prefix("INIT") + "Initializing FUELS...")
fuel_list = []
fuel_command_list = []
for file in os.listdir(fuel_content_dir):
    fuel_list.append(file)
    resolve_fuel_informations(file)
print(prefix("INIT") + "Active FUELS: " + str(fuel_list).replace("[", "").replace("]", "").replace("'", ""))
print(prefix("INIT") + "FUELS initialised")

print(prefix("INIT") + "Init phase complete!")
update_status("Initialisation completed!")
time.sleep(0.5)
print("")

# INIT PHASE END

menu()
while True:
    print("")
    update_status("Idle")
    try:
        if threading.current_thread().name == "MainThread":
            current_thread_name = "FyUTILS"
        else:
            current_thread_name = threading.current_thread().name

        if os.getcwd() == current_dir:
            cwd_abbreviation = "#"
        elif os.getcwd() == "C:\\":
            cwd_abbreviation = "/"
        elif os.getcwd() == user_dir:
            cwd_abbreviation = "~"
        elif os.getcwd() == appdata_dir:
            cwd_abbreviation = "@"
        else:
            cwd_abbreviation = os.getcwd()
        cmd = input(accent_color() + "╔═══[" + color() + username + accent_color() + "@" + text_color() + device + accent_color() + "]══(" + color() + current_thread_name + accent_color() + "/" + text_color() + version + accent_color() + ")══[" + text_color() + cwd_abbreviation + accent_color() + "]\n" +
                    accent_color() + "╚═══> " + text_color())
    except KeyboardInterrupt:
        try:
            update_status("Shutting down...")
            print("\n" + prefix("INFO") + "Shutting down FyUTILS...")
            time.sleep(1)
            sys.exit(0)
        except KeyboardInterrupt:
            continue

    match cmd.lower():
        case "flood":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                flood_target = input(
                    accent_color() + "║ " + text_color() + "Target IP" + accent_color() + " > " + text_color())
                flood_port = int(input(
                    accent_color() + "║ " + text_color() + "Target port" + accent_color() + " > " + text_color()))
                activity_start = time.time()
                update_status(flood_target + ":" + str(flood_port))
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((flood_target, flood_port))
                print(accent_color() + "╚" + "═" * 119)
                print("")
                try:
                    for i in range(sys.maxsize):
                        try:
                            sock.send(random.randbytes(10240))
                            print(prefix("INFO") + "Attacking target: " + color() + flood_target + accent_color() + ":" + color() + str(flood_port) + text_color() + "..." + accent_color() + " - " + text_color() + "Attack: " + color() + str(i + 1) + accent_color(), end='\r')
                        except socket.error:
                            print("")
                            print(prefix("ERROR") + "Request " + color() + str(i) + text_color() + " failed.", end='\r')
                            time.sleep(0.1)
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")
            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
            except:
                print("")
                print(accent_color() + "╚" + "═" * 119)

        case "portscan":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                scan_target = input(accent_color() + "║ " + text_color() + "Target IP" + accent_color() + " > " + text_color())
                activity_start = time.time()
                update_status(scan_target)
                print(accent_color() + "╚" + "═" * 119)
                print("")
                try:
                    print(prefix("INFO") + "Preparing scan.", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan..", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan...", end='\r')
                    for scan_port in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(0.05)
                        result = sock.connect_ex((scan_target, scan_port))
                        print(prefix("INFO") + "Scanning Port... " + color() + str(scan_port), end='\r')
                        if result == 0:
                            print(prefix("INFO") + "Port " + color() + str(scan_port) + text_color() + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
            except:
                print("")
                print(accent_color() + "╚" + "═" * 119)

        case "checkport":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                check_target = input(accent_color() + "║ " + text_color() + "Target IP" + accent_color() + " > " + text_color())
                check_port = int(input(accent_color() + "║ " + text_color() + "Target port" + accent_color() + " > " + text_color()))
                activity_start = time.time()
                print(accent_color() + "╚" + "═" * 119)
                update_status("Checking port " + str(check_port) + " on " + check_target)
                print("")
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((check_target, check_port))
                    if result == 0:
                        print(prefix("INFO") + "Port " + color() + str(check_port) + text_color() + " is open!")
                    else:
                        print(prefix("ERROR") + "Port " + color() + str(check_port) + text_color() + " is not open!")
                    sock.close()
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print(prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")
            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
            except:
                print(accent_color() + "╚" + "═" * 119)

        case "ssh":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            update_status("Starting FySSH service...")
            try:
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
                ssh_password = pwinput.pwinput(accent_color() + "║ " + text_color() + "Password" + accent_color() + " > " + text_color(), "*")
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
                        print("\n" + prefix("INFO") + "Canceling Action...")
                        break
                    except Exception as e:
                        print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                        print(prefix("ERROR") + str(e))
                        print("")

                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + color() + ssh_server + accent_color() + ":" + color() + str(ssh_port) + text_color() + "...")
                try:
                    ssh.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
            except:
                print("")
                print(accent_color() + "╚" + "═" * 119)

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
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print(prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
            except:
                continue

        case "fetch":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                fetch_url = input(accent_color() + "║ " + text_color() + "Enter URL" + accent_color() + " > " + text_color())
                fetch_file_name = input(accent_color() + "║ " + text_color() + "Enter name (example: file.html)" + accent_color() + " > " + text_color())
                print(accent_color() + "╚" + "═" * 119)
                print("")
                activity_start = time.time()
                update_status("Fetching: " + fetch_url)
                try:
                    fetch_content = requests.get(fetch_url).content.decode()
                    print(prefix("INFO") + "Content of " + fetch_url + " cached!")
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                    print(prefix("INFO") + "Saving content of " + fetch_url + " from memory to local storage!")

                    try:
                        open(download_content_dir + "\\" + fetch_file_name, mode="x").writelines(str(fetch_content))
                    except Exception as e:
                        print("\n" + prefix("ERROR") + "Could not save content to file.")
                        print(prefix("ERROR") + str(e))
                        print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                        print("")
                except KeyboardInterrupt:
                    print("")
                    print(accent_color() + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            except:
                continue

        case "youtube":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                youtube_url = input(accent_color() + "║ " + text_color() + "Enter URL" + accent_color() + " > " + text_color())
                print(accent_color() + "╚" + "═" * 119)
                try:
                    print("")
                    activity_start = time.time()
                    youtube = YouTube(youtube_url)
                    update_status("Downloading: " + youtube.title.title())
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                        print(prefix("INFO") + "Media directory created!")
                    print(prefix("INFO") + "Download started!")
                    youtube.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download(download_content_dir)
                    print(prefix("INFO") + f"Download finished in {time.time() - activity_start: 0.2f} seconds!")
                    os.system("start explorer.exe " + download_content_dir)
                except KeyboardInterrupt:
                    print("")
                    print(accent_color() + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
            except:
                continue

        case "calc":
            while True:
                print("")
                print(accent_color() + "╔" + "═" * 119)
                try:
                    calculation = input(accent_color() + "║ " + text_color() + "Calculate" + accent_color() + " > " + text_color())
                    print(accent_color() + "╚" + "═" * 119)
                    print("")
                    print(prefix("INFO") + calculation + " is " + str(eval(calculation)))
                except KeyboardInterrupt:
                    print("")
                    print(accent_color() + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    break
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

        case "calculate":
            while True:
                print("")
                print(accent_color() + "╔" + "═" * 119)
                try:
                    calculation = input(accent_color() + "║ " + text_color() + "Calculate" + accent_color() + " > " + text_color())
                    print(accent_color() + "╚" + "═" * 119)
                    print("")
                    print(prefix("INFO") + calculation + " is " + str(eval(calculation)))
                except KeyboardInterrupt:
                    print("")
                    print(accent_color() + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    break
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

        case "fuels":
            print("")
            print(prefix("FUEL") + "Active FUELS:")
            for file in fuel_list:
                print(prefix("FUEL") + file)

        case "fuel":
            print("")
            print(accent_color() + "╔" + "═" * 119)
            try:
                fuel_installation_path = input(accent_color() + "║ " + text_color() + "Path of FUEL" + accent_color() + " > " + text_color())
                print(accent_color() + "╚" + "═" * 119)
                print("")
                print(prefix("FUEL") + "Installation process started!")
                time.sleep(0.03)
                print(prefix("FUEL") + "Using \"" + fuel_installation_path + "\" as installation file.")
                time.sleep(0.15)
                print(prefix("FUEL") + "Checking FUEL directory...")
                if not os.path.exists(fuel_content_dir):
                    os.makedirs(fuel_content_dir)
                time.sleep(0.5)
                print(prefix("FUEL") + "Installing to: " + fuel_content_dir + "...")
                time.sleep(0.75)
                shutil.copy(fuel_installation_path, fuel_content_dir)
                print(prefix("FUEL") + "FUEL copied to destination directory.")
                time.sleep(0.05)
                print(prefix("FUEL") + "Origin: " + fuel_installation_path)
                time.sleep(0.05)
                print(prefix("FUEL") + "Destination: " + fuel_content_dir)
                fuel_name = os.path.basename(fuel_installation_path).split("/")[-1]
                fuel_path = fuel_content_dir + fuel_name
                print(prefix("FUEL") + "FUEL \"" + fuel_name + "\" successfuly installed to \"" + fuel_content_dir + "\".")
                time.sleep(0.25)
                print(prefix("FUEL") + "Adding FUEL to FyUTILS...")
                fuel_list.append(fuel_path)
                resolve_fuel_informations(fuel_path)
                time.sleep(0.05)
                print(prefix("FUEL") + "Active FUELS: " + str(fuel_list).replace("[", "").replace("]", "").replace("'", ""))

            except KeyboardInterrupt:
                print("")
                print(accent_color() + "╚" + "═" * 119)
                print("\n" + prefix("INFO") + "Canceling Action...")
            except Exception as e:
                print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                print(prefix("ERROR") + str(e))
                print("")

        case "restart":
            os.system("start " + current_dir + "\\main.py")
            sys.exit(0)

        case "rs":
            os.system("start " + current_dir + "\\main.py")
            sys.exit(0)

        case "exit":
            try:
                update_status("Shutting down...")
                print(prefix("INFO") + "Shutting down FyUTILS...")
                time.sleep(1)
                update_status("FyUTILS stopped!")
                print(prefix("INFO") + "FyUTILS stopped!")
                sys.exit(0)
            except KeyboardInterrupt:
                None

        case "clear":
            update_status("Reloading...")
            menu()

        case "rl":
            update_status("Reloading...")
            menu()

        case "cls":
            update_status("Reloading...")
            menu()

        case "reload":
            update_status("Reloading...")
            menu()

        case _:
            if fuel_command_list.__contains__(cmd.lower()):
                exec(globals()["FUEL_SPECIFIC_COMMAND_VARIABLE_" + cmd.lower()])
                continue
            if cmd.startswith("cd "):
                try:
                    cdir = cmd.replace("cd ", "")
                    if cdir == "~":
                        cdir = user_dir
                    elif cdir == "/":
                        cdir = "C:\\"
                    elif cdir == "#":
                        cdir = current_dir
                    elif cdir == "@":
                        cdir = appdata_dir
                    os.chdir(cdir)
                    print(Fore.WHITE + cdir)
                except:
                    print(prefix("ERROR") + "Couldn't change directory to \"" + cmd.replace("cd ", "") + "\".")
            else:
                os.system(cmd)
                