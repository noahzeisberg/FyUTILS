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
import tkinter.filedialog
import traceback
from pathlib import Path
import easygui

import paramiko
import phonenumbers
import psutil
import pwinput
import requests
import scapy.layers.l2 as scapy
from colorama import Fore, init
from phonenumbers import geocoder, carrier, timezone
from pypresence import Presence
from pytube import YouTube

init(convert=True)


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
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + fuel_color() + "FUEL" + accent_color() + "] " + text_color()
    elif type == "SHIELD":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.YELLOW + "SHIELD" + accent_color() + "] " + text_color()
    else:
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + current_thread_name + accent_color() + "/" + Fore.WHITE + str(type).upper() + accent_color() + "] " + text_color()


def version_is_newer(value):
    split = str(version).split(".")
    major = split[0]
    minor = split[1]
    patch = split[2]

    second_split = str(value).split(".")
    second_major = second_split[0]
    second_minor = second_split[1]
    second_patch = second_split[2]

    if version == value:
        return False

    if major <= second_major:
        if minor <= second_minor:
            if patch <= second_patch:
                return True


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
    os.system("title FyUTILS " + version + " - " + user + "@" + server + " - " + status)
    try:
        rpc.update(
            state="[REMOTE] " + status, details=user + "@" + server, small_image="ssh",
            large_image="large",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"},
                     {"label": "View Project", "url": "https://github.com/NoahOnFyre/FyUTILS/"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def resolve_fuel_information(file):
    fuel = open(fuel_content_dir + file, mode="rt")
    fuel_json = json.load(fuel)
    print(prefix("FUEL") + "FUEL information of: " + file)
    print(prefix("FUEL") + "FUEL name: " + fuel_json["name"])
    print(prefix("FUEL") + "FUEL version: v" + fuel_json["version"])
    print(prefix("FUEL") + "FUEL author: " + fuel_json["author"])
    print(prefix("FUEL") + "FUEL description: " + fuel_json["description"])
    print(prefix("FUEL") + "FUEL format: " + str(fuel_json["format"]))
    print(prefix("FUEL") + "FUEL type: " + fuel_json["properties"]["type"])
    match fuel_json["properties"]["type"]:
        case "DEFAULT":
            print(prefix("FUEL") + "FUEL command name: " + fuel_json["properties"]["command_name"])
            print(prefix("FUEL") + "Head enabled: " + str(fuel_json["head"]["enabled"]))
            print(prefix("FUEL") + "Body enabled: " + str(fuel_json["body"]["enabled"]))
            print(prefix("FUEL") + "Argument length: " + str(fuel_json["head"]["argument_length"]))
            print(prefix("FUEL") + "Command status: " + fuel_json["head"]["status"])
            fuels.update({fuel_json["properties"]["command_name"]: fuel_content_dir + file})

        case "MIXIN":
            print(prefix("FUEL") + "WARNING: If you are a FUEL developer, please use a")
            print(prefix("FUEL") + "default FUEL and use a command for your injection.")
            print(prefix("FUEL") + "Support for mixins injecting on initialisation will be added soon.")
            time.sleep(2.5)

        case _:
            print(prefix("FUEL") + "FUEL type is not supported by this version.")
    fuel.close()


def color(): return src_color


def fuel_color(): return src_fuel_color


def accent_color(): return src_accent_color


def text_color(): return src_text_color


def menu():
    os.system("cls")
    print(color() + "  __________               _____  __   ________   ________   ______       ________")
    time.sleep(1/1000)
    print(color() + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    time.sleep(1/1000)
    print(color() + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \ ")
    time.sleep(1/1000)
    print(color() + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    time.sleep(1/1000)
    print(color() + "  /_/         _\__, /      \____/      /_/        /___/      /_____/      /____/  ")
    time.sleep(1/1000)
    print(color() + "             ___/  /")
    time.sleep(1/1000)
    print(color() + "            /_____/ " + " "*5 + accent_color() + "v" + text_color() + version.replace(".", accent_color() + "." + text_color()) + accent_color() + " | " + text_color() + "Made by NoahOnFyre")
    time.sleep(1/1000)
    print("")
    time.sleep(1/1000)
    print(accent_color() + "╔" + "═"*119)
    time.sleep(1/1000)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Username: " + username)
    time.sleep(1/1000)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Device: " + device)
    time.sleep(1/1000)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Private IP: " + private_ip)
    time.sleep(1/1000)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Version: " + version)
    time.sleep(1/1000)
    if update_available:
        print(accent_color() + "╠" + "═"*119)
        time.sleep(1/1000)
        print(accent_color() + "║ " + accent_color() + "[" + color() + "UPDATE" + accent_color() + "] " + text_color() + "A new version of FyUTILS is available! Install it now using \"update\".")
        time.sleep(1/1000)
        print(accent_color() + "║ " + accent_color() + "[" + color() + "UPDATE" + accent_color() + "] " + text_color() + Fore.RED + version + accent_color() + " => " + Fore.GREEN + newest_version + text_color())
        time.sleep(1/1000)
    print(accent_color() + "╚" + "═"*119)


# INIT PHASE
os.system("title FyUTILS")

# Color initialization

src_color = Fore.LIGHTBLUE_EX
src_fuel_color = Fore.LIGHTMAGENTA_EX
src_accent_color = Fore.LIGHTBLACK_EX
src_text_color = Fore.WHITE

# Variable initialization
try:
    print(prefix("INIT") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INIT") + "Username: " + username)
    device = platform.node()
    print(prefix("INIT") + "Device: " + device)
    start_time = time.time()
    print(prefix("INIT") + "Start time: " + str(start_time))
    current_dir = sys.path[0]
    print(prefix("INIT") + "Directory: " + current_dir)
    version = "1.5.7"
    print(prefix("INIT") + "Version: " + version)
    threads = multiprocessing.cpu_count()
    print(prefix("INIT") + "ThreadWorkers: " + str(threads))
    private_ip = socket.gethostbyname(socket.gethostname())
    print(prefix("INIT") + "Private IP: " + private_ip)
    user_dir = str(Path.home())
    print(prefix("INIT") + "User specific directory: " + user_dir)
    appdata_dir = user_dir + "\\AppData"
    print(prefix("INIT") + "AppData directory: " + appdata_dir)
    main_dir = appdata_dir + "\\Roaming\\FyUTILS\\"
    print(prefix("INIT") + "FyUTILS AppData directory: " + main_dir)
    tmp_dir = user_dir + "\\AppData\\Roaming\\FyUTILS\\tmp\\"
    print(prefix("INIT") + "Temp files directory: " + tmp_dir)
    download_content_dir = main_dir + "content\\"
    print(prefix("INIT") + "Download Content Location: " + download_content_dir)
    fuel_content_dir = main_dir + "fuels\\"
    print(prefix("INIT") + "FUEL Content Location: " + fuel_content_dir)
    cpu = platform.processor()
    print(prefix("INIT") + "CPU: " + cpu)
    releases = "https://api.github.com/repos/NoahOnFyre/FyUTILS/releases"
    print(prefix("INIT") + "Releases URL: " + releases)
    memory_amount = psutil.virtual_memory().total
    print(prefix("INIT") + "Memory amount: " + str(round(memory_amount/1024/1024)) + "MB")
except Exception as e:
    print(prefix("ERROR") + "Failed to get system variables!")
    print(traceback.format_exc())
    print(prefix("ERROR") + "Shutting down...")
    os.system("pause")
    sys.exit(2048)

# Update checker
print(prefix("INIT") + "Checking for updates...")
try:
    releases_json = requests.get(releases).json()
    newest_release = releases_json[0]
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            release_download_url = ""
            continue
    newest_version = newest_release["tag_name"]
    if version_is_newer(newest_version):
        print(prefix("INIT") + "A new version of FyUTILS is available!")
        print(prefix("INIT") + "Current version identifier: " + version)
        print(prefix("INIT") + "Newest version identifier: " + newest_version)
        update_available = True
    else:
        print(prefix("INIT") + "No update found!")
        print(prefix("INIT") + "Current version identifier: " + version)
        print(prefix("INIT") + "Newest version identifier: " + newest_version)
        update_available = False
except Exception as e:
    print(prefix("ERROR") + "Checking for updates failed. Please check your internet connection.")
    update_available = False

# Discord RPC initialization
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
    time.sleep(0.25)

# FUEL initialization

print(prefix("INIT") + "Initializing FUELS...")
fuels = {}
if not os.path.exists(fuel_content_dir):
    os.makedirs(fuel_content_dir)
for file in os.listdir(fuel_content_dir):
    resolve_fuel_information(file)

print(prefix("INIT") + "FUELS initialized")

print(prefix("INIT") + "Initialization phase completed!")
update_status("Initialization phase completed!")

# INIT PHASE END

menu()
try:
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
                cwd_abbreviation = os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower()
            request = input(accent_color() + "╔═══[" + color() + username + accent_color() + "@" + text_color() + device + accent_color() + "]══(" + color() + current_thread_name + accent_color() + "/" + text_color() + version + accent_color() + ")══[" + text_color() + cwd_abbreviation + accent_color() + "]\n" +
                            accent_color() + "╚═══> " + text_color()).split(" ")
            cmd = request[0].lower()
            request.__delitem__(0)
            args = request
            print("")
        except KeyboardInterrupt:
            try:
                update_status("Shutting down...")
                print("\n" + prefix("INFO") + "Shutting down FyUTILS...")
                time.sleep(1)
                sys.exit(0)
            except KeyboardInterrupt:
                continue

        match cmd:
            case "flood":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                port = int(args[1])
                activity_start = time.time()
                update_status("Flooding " + target + ":" + str(port))

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.connect((target, port))
                    for i in range(sys.maxsize):
                        try:
                            sock.send(random.randbytes(10240))
                            print(prefix("INFO") + "Attacking target: " + color() + target + accent_color() + ":" + color() + str(port) + text_color() + "..." + accent_color() + " - " + text_color() + "Attack: " + color() + str(i + 1) + accent_color(), end='\r')
                        except socket.error:
                            print("")
                            print(prefix("ERROR") + "Request " + color() + str(i) + text_color() + " failed.", end='\r')
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "portscan":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                activity_start = time.time()
                update_status("Scanning on " + target)

                try:
                    print(prefix("INFO") + "Preparing scan.", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan..", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan...", end='\r')
                    for port in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(0.05)
                        result = sock.connect_ex((target, port))
                        print(prefix("INFO") + "Scanning Port... " + color() + str(port), end='\r')
                        if result == 0:
                            print(prefix("INFO") + "Port " + color() + str(port) + text_color() + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "arp":
                activity_start = time.time()
                update_status("ARP scanning in " + private_ip + "...")

                try:
                    print(prefix("INFO") + "Make sure you have WinPcap or Npcap installed!")
                    print(prefix("INFO") + "Initialising ARP service...")
                    arp = scapy.ARP(pdst=private_ip + "/24")
                    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                    packet = ether/arp
                    print(prefix("INFO") + "Sending ARP packets...")
                    content = scapy.srp(packet, timeout=2, verbose=0)[0]
                    clients = []
                    print(prefix("INFO") + "Receiving data from " + private_ip + "...")
                    for sent, received in content:
                        clients += [[received.psrc, received.hwsrc]]
                    print(prefix("INFO") + "Processing received data...")
                    print(prefix("INFO") + "Data received and processed.")
                    client_count = len(clients)
                    for i in range(client_count):
                        print(prefix("INFO") + accent_color() + "[" + color() + str(i) + accent_color() + "] " + text_color() + "IP: " + clients[i][0] + " MAC: " + clients[i][1])
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "checkport":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                port = int(args[1])
                activity_start = time.time()
                update_status("Checking" + target + ":" + str(port))

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        print(prefix("INFO") + "Port " + color() + str(port) + text_color() + " is open!")
                    else:
                        print(prefix("ERROR") + "Port " + color() + str(port) + text_color() + " is not open!")
                    sock.close()
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "ssh":
                if len(args) != 3:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                server = args[0]
                port = int(args[1])
                user = args[2]
                activity_start = time.time()
                update_status("Starting FySSH service...")

                print(prefix("INFO") + "Connecting to " + server + ":" + str(port) + " as " + user)
                print(prefix("INFO") + "Creating SSH client...")
                ssh = paramiko.SSHClient()
                print(prefix("INFO") + "Loading host keys...")
                ssh.load_system_host_keys()
                print(prefix("INFO") + "Adding policy...")
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(prefix("INFO") + "Requesting user's password...")
                password = pwinput.pwinput(text_color() + "Enter password" + accent_color() + " > " + text_color(), "*")
                print(prefix("INFO") + "Connecting...")
                print("")
                try:
                    ssh.connect(server, port=port, username=user, password=password)
                    while True:
                        try:
                            update_ssh_status("Idle")
                            ssh_cmd = input(accent_color() + "╔═══[" + fuel_color() + user + accent_color() + "@" + fuel_color() + server + accent_color() + ":" + fuel_color() + str(port) + accent_color() + "]═══(" + color() + "FySSH " + text_color() + version + accent_color() + ")" + "\n" + "╚═══" + accent_color() + "> " + text_color())
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
                except Exception as e:
                    print(prefix("ERROR") + "Can't connect to SSH host. Please make sure, that the requested port is open.")
                    print(prefix("ERROR") + "SSH error: " + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                    print(prefix("INFO") + "Cleaning up...")
                    continue

                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + color() + server + accent_color() + ":" + color() + str(port) + text_color() + "...")
                try:
                    ssh.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "fetch":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                filename = args[1]
                activity_start = time.time()
                update_status("Fetching: " + url)

                try:
                    print(prefix("INFO") + "Fetching " + url + "...")
                    fetch_content = requests.get(url).content
                    print(prefix("INFO") + "Content of " + url + " cached!")
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                    print(prefix("INFO") + "Writing content of " + url + " from cache to local storage!")

                    try:
                        open(download_content_dir + "\\" + filename, mode="xb").write(fetch_content)
                        os.system("start explorer.exe " + download_content_dir)
                    except Exception as e:
                        print("\n" + prefix("ERROR") + "Could not save content to file.")
                        print(prefix("ERROR") + str(e))
                        print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                        print("")
                except KeyboardInterrupt:
                    print("")
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            case "phone":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                number = args[0]
                activity_start = time.time()
                update_status("Retrieving information for " + number)

                try:
                    parsed_number = phonenumbers.parse(number)
                    location = geocoder.description_for_number(parsed_number, "de")
                    carrier = carrier.name_for_number(parsed_number, "de")
                    zone = timezone.time_zones_for_number(parsed_number)
                    print(prefix("INFO") + "Phone number information of " + number + ":")
                    print(prefix("INFO") + "Location: " + location)
                    print(prefix("INFO") + "Carrier: " + carrier)
                    print(prefix("INFO") + "Timezone: " + str(zone))
                except KeyboardInterrupt:
                    print("")
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            case "youtube":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                activity_start = time.time()
                update_status("Downloading: " + url)

                try:
                    youtube = YouTube(url)
                    update_status("Downloading: " + youtube.title.title())
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                        print(prefix("INFO") + "Media directory created!")
                    print(prefix("INFO") + "Download started!")
                    youtube.streams.filter(file_extension="mp4").order_by('resolution').desc().first().download(download_content_dir)
                    print(prefix("INFO") + f"Download finished in {time.time() - activity_start: 0.2f} seconds!")
                    os.system("start explorer.exe " + download_content_dir)
                except KeyboardInterrupt:
                    print("")
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            case "log":
                os.system("explorer.exe /select,\"" + main_dir + "crash.log" + "\"")

            case "fuels":
                print(prefix("FUEL") + "Active FUELS:")
                for path in fuels.values():
                    print(prefix("FUEL") + os.path.basename(path).split("/")[-1])

            case "fuel":
                if len(args) != 2:
                    if len(args) == 1 and (args[0] == "add" or args[0] == "remove"):
                        None
                    else:
                        print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                        continue
                fuel_action = args[0]
                if len(args) == 2:
                    fuel_location = args[1]
                activity_start = time.time()
                update_status("Installing FUEL...")

                if fuel_action == "install":
                    print(prefix("FUEL") + "Installation process started!")
                    filename = fuel_location + ".json"
                    print(prefix("FUEL") + "Using \"" + filename + "\" as target package.")
                    print(prefix("FUEL") + "Checking FUEL directory...")
                    if not os.path.exists(fuel_content_dir):
                        os.makedirs(fuel_content_dir)
                    if os.path.exists(fuel_content_dir + filename):
                        print(prefix("ERROR") + "Package \"" + filename + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package is already installed.")
                        continue
                    print(prefix("FUEL") + "Installing to: " + fuel_content_dir + "...")
                    print(prefix("FUEL") + "Checking FUEL in NoahOnFyre/FUELS...")
                    fuel_repo_contents = requests.get("https://api.github.com/repos/NoahOnFyre/FUELS/contents/").json()
                    for i in range(len(fuel_repo_contents)):
                        fuel_download_url = ""
                        if fuel_repo_contents[i]["name"] == filename:
                            fuel_download_url = fuel_repo_contents[i]["download_url"]
                            break
                        else:
                            continue
                    if fuel_download_url == "":
                        print(prefix("ERROR") + "Package \"" + filename + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package not found.")
                        continue
                    print(prefix("FUEL") + "Fetching FUEL from NoahOnFyre/FUELS...")
                    fuel_file_content = requests.get(fuel_download_url).content
                    print(prefix("FUEL") + "Writing content to file...")
                    local_fuel_file = open(fuel_content_dir + filename, mode="xb")
                    local_fuel_file.write(fuel_file_content)
                    local_fuel_file.close()
                    local_fuel_file = open(fuel_content_dir + filename, mode="rt")
                    print(prefix("FUEL") + "FUEL " + fuel_color() + filename + text_color() + " successfuly installed to \"" + fuel_content_dir + "\".")
                    print(prefix("FUEL") + "Adding FUEL to FyUTILS...")
                    local_fuel_file_json = json.load(local_fuel_file)
                    if local_fuel_file_json["properties"]["type"] == "DEFAULT":
                        fuels.update({local_fuel_file_json["properties"]["command_name"]: fuel_content_dir + filename})
                    print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to install package " + fuel_color() + fuel_location + text_color() + "!")

                elif fuel_action == "add":
                    if len(args) == 1:
                        fuel_location = easygui.fileopenbox(msg="Import FUEL into FyUTILS", title="FUEL Managment Utilities", filetypes=[["*.json", "FUEL files"]], multiple=False)
                    print(prefix("FUEL") + "Installation process started!")
                    filename = os.path.basename(fuel_location).split("/")[-1]
                    print(prefix("FUEL") + "Checking FUEL directory...")
                    if not os.path.exists(fuel_content_dir):
                        os.makedirs(fuel_content_dir)
                    if os.path.exists(fuel_content_dir + filename):
                        print(prefix("ERROR") + "Package \"" + fuel_location + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package is already installed.")
                        continue
                    print(prefix("FUEL") + "Installing to: " + fuel_content_dir + "...")
                    print(prefix("FUEL") + "Copying FUEL from " + fuel_location + "...")
                    shutil.copy(fuel_location, fuel_content_dir)
                    local_fuel_file = open(fuel_content_dir + filename)
                    print(prefix("FUEL") + "FUEL " + fuel_color() + filename + text_color() + " successfuly copied to \"" + fuel_content_dir + "\".")
                    print(prefix("FUEL") + "Adding FUEL to FyUTILS...")
                    local_fuel_file_json = json.load(local_fuel_file)
                    if local_fuel_file_json["properties"]["type"] == "DEFAULT":
                        fuels.update({local_fuel_file_json["properties"]["command_name"]: fuel_content_dir + filename})
                    print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to install package " + fuel_color() + filename + text_color() + "!")

                elif fuel_action == "remove":
                    if len(args) == 1:
                        temp = os.getcwd()
                        os.chdir(fuel_content_dir)
                        fuel_location = easygui.fileopenbox(msg="Removing FUEL from FyUTILS", title="FUEL Managment Utilities", filetypes=[["*.json", "FUEL files"]], multiple=False)
                        os.chdir(temp)
                    filename = os.path.basename(fuel_location).split("/")[-1]
                    print(prefix("FUEL") + "Unregistering " + fuel_content_dir + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        temp = open(fuel_content_dir + filename)
                        fuels.pop(json.load(temp)["properties"]["command_name"])
                        temp.close()
                    else:
                        print(prefix("ERROR") + "Package \"" + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix("FUEL") + "Deleting " + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        os.remove(fuel_content_dir + filename)
                    else:
                        print(prefix("ERROR") + "Package \"" + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to remove package " + fuel_color() + filename)

                try:
                    None
                except KeyboardInterrupt:
                    print("")
                    print(accent_color() + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "update":
                update_status("Updating FyUTILS...")

                if update_available:
                    print(prefix("INFO") + "Update found!")
                    print(prefix("INFO") + "Version Comparison: " + Fore.RED + version + accent_color() + " => " + Fore.GREEN + newest_version + text_color() + "...")
                    newest_file_content = requests.get(release_download_url).content
                    open(current_dir + "\\main.py", mode="wb").write(newest_file_content)
                    print(prefix("INFO") + "Update successfully installed!")
                    time.sleep(1)
                    print(prefix("INFO") + "Restarting FyUTILS...")
                    os.system("start " + current_dir + "\\main.py")
                    sys.exit(512)
                else:
                    print(prefix("ERROR") + "You're running the latest version of FyUTILS!")
                    print(prefix("INFO") + "Version comparison: " + Fore.GREEN + version + accent_color() + " = " + Fore.GREEN + newest_version + text_color() + "...")

            case "edit":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                filepath = args[0]
                activity_start = time.time()
                update_status("Editing " + filepath + "...")

                if not os.path.exists(filepath):
                    print(prefix("ERROR") + "File not found!")
                    confirmation = input(prefix("INFO") + "Do you want to let FyUTILS create a new file? (y/n): ")
                    if confirmation.lower() == "n":
                        continue
                    file = open(filepath, "x+")
                    print(prefix("INFO") + "File created successfuly.")
                    print(prefix("INFO") + "End file editing by entering \"END\".")
                else:
                    file = open(filepath, "w+")
                    print(prefix("INFO") + "File opened successfuly.")
                    print(prefix("INFO") + "End file editing by entering \"END\".")
                string = ""
                for i in range(1, sys.maxsize):
                    try:
                        line = input(str(i) + ": ")
                        if line == "END":
                            break
                        string = string + line + "\n"
                    except KeyboardInterrupt:
                        print("END")
                        print("")
                        break
                print(prefix("INFO") + "Writing cached content to " + filepath + "...")
                file.writelines(string)
                print(prefix("INFO") + "Saving file to " + filepath + "...")
                print(prefix("INFO") + "Closing " + filepath + "...")
                file.close()
                print(prefix("INFO") + "File is saved and closed!")
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "calc":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                calculation = args[0]
                activity_start = time.time()
                update_status("Calculating " + calculation)

                print(prefix("INFO") + calculation + " is " + str(eval(calculation)))

            case "read":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                filepath = args[0]
                activity_start = time.time()
                update_status("Reading " + filepath + "...")

                if not os.path.exists(filepath):
                    print(prefix("ERROR") + "File not found!")
                    continue
                else:
                    file = open(filepath, "rt")
                    print(prefix("INFO") + "File opened successfuly.")
                i = 1
                for line in file.readlines():
                    print(str(i) + ": " + line, end="\r")
                    i += 1
                print(prefix("INFO") + "Closing " + filepath + "...")
                file.close()
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "ls":
                try:
                    print(prefix("INFO") + "Content of " + os.getcwd())
                    for file in os.listdir(os.getcwd()):
                        if file.startswith("."):
                            if os.path.isfile(file):
                                print(prefix("INFO") + accent_color() + file)
                            elif os.path.isdir(file):
                                print(prefix("INFO") + accent_color() + "/" + file)
                        elif os.path.isfile(file):
                            print(prefix("INFO") + file)
                        elif os.path.isdir(file):
                            print(prefix("INFO") + Fore.GREEN + "/" + file)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "exit":
                update_status("Shutting down...")
                print(prefix("INFO") + "Shutting down FyUTILS...")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling action")
                    continue
                print("logout")
                sys.exit(0)

            case "cd":
                if len(args) != 1:
                    print(prefix("INFO") + os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower())
                    continue
                change_dir = args[0]
                activity_start = time.time()
                update_status("Switching to " + change_dir + "...")

                match change_dir:
                    case "~":
                        change_dir = user_dir

                    case "#":
                        change_dir = current_dir

                    case "@":
                        change_dir = appdata_dir

                    case "/":
                        change_dir = "C:\\"

                    case _:
                        change_dir = change_dir

                try:
                    os.chdir(change_dir)
                    if os.getcwd() == current_dir:
                        cwd_abbreviation = "#"
                    elif os.getcwd() == "C:\\":
                        cwd_abbreviation = "/"
                    elif os.getcwd() == user_dir:
                        cwd_abbreviation = "~"
                    elif os.getcwd() == appdata_dir:
                        cwd_abbreviation = "@"
                    else:
                        cwd_abbreviation = os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower()
                    print(prefix("INFO") + cwd_abbreviation)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "raise":
                update_status("Raising exception...")
                raise Exception("Executed by raise command.")

            case "clear":
                update_status("Reloading...")
                os.system("cls")
                menu()

            case "rl":
                update_status("Reloading...")
                os.system("cls")
                menu()

            case "restart":
                print("logout")
                os.system("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case "rs":
                print("logout")
                os.system("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case _:
                if fuels.keys().__contains__(cmd.lower()):
                    fuel_file = open(fuels.get(cmd.lower()), mode="rt")
                    json_fuel_file = json.load(fuel_file)
                    if json_fuel_file["head"]["enabled"]:
                        if len(args) != json_fuel_file["head"]["argument_length"]:
                            print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                            continue
                        for entry in range(len(json_fuel_file["head"]["arguments"])):
                            exec(list(json_fuel_file["head"]["arguments"])[entry] + " = args[" + str(entry) + "]")
                        activity_start = time.time()
                        update_status(json_fuel_file["head"]["status"])

                    if json_fuel_file["body"]["enabled"]:
                        exec("\n".join(list(json_fuel_file["body"]["content"])))
                else:
                    arg_string = " "
                    for entry in args:
                        arg_string += entry + " "
                    os.system(cmd + arg_string)
except Exception as e:
    os.system("title FyUTILS Crash Handler - Crash Log")
    print(prefix("ERROR") + "FyUTILS CRASH LOG @ " + datetime.datetime.now().strftime("%H:%M:%S"))
    print(prefix("ERROR") + "Error: " + str(e))
    temp = open(main_dir + "crash.log", "w+")
    temp.writelines("FyUTILS - Traceback crash log of  " + datetime.datetime.now().strftime("%H:%M:%S") + "\n" + "="*50 + "\n\n" + traceback.format_exc())
    temp.close()
    print(prefix("ERROR") + "The full crash log has been saved to: " + main_dir + "crash.log")
    os.system("explorer.exe /select,\"" + main_dir + "crash.log" + "\"")
    os.system("pause")
    sys.exit(1024)
