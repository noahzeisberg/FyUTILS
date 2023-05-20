import datetime
import json
import multiprocessing
import os
import platform
import random
import shutil
import socket
import subprocess
import sys
import time
import traceback
import paramiko
import phonenumbers
import psutil
import pwinput
import requests
import string
from pathlib import Path
import scapy.packet
from scapy.layers.l2 import ARP, Ether, srp
from scapy.all import sniff
from colorama import Fore, init
from phonenumbers import geocoder, carrier, timezone
from pypresence import Presence
from pytube import YouTube

init(convert=True)
CURRENT_FYUTILS_VERSION = "1.9.1"
SUPPORTED_FUEL_VERSION = 1


def prefix(level: str = "INFO", protocol: str = "FyUTILS"):
    if level == "INFO":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + protocol + accent_color() + "/" + true_color() + level.upper() + accent_color() + "] " + text_color()
    elif level == "WARN":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + protocol + accent_color() + "/" + warn_color() + level.upper() + accent_color() + "] " + text_color()
    elif level == "ERROR":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + protocol + accent_color() + "/" + false_color() + level.upper() + accent_color() + "] " + text_color()
    elif level == "DEBUG":
        return accent_color() + "[" + color() + datetime.datetime.now().strftime("%H:%M:%S") + accent_color() + "]" + " " + accent_color() + "[" + text_color() + protocol + accent_color() + "/" + debug_color() + level.upper() + accent_color() + "] " + text_color()
    else:
        return false_color() + "PREFIX TYPE NOT SUPPORTED. SEE https://github.com/NoahOnFyre/FyUTILS#prefix"


def execute(command):
    subprocess.call(command, shell=True)


def exec_code(command):
    return subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)


def version_is_newer(current, value):
    split = str(current).split(".")
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
    execute("title FyUTILS " + version + " - " + username + "@" + device + " - " + status)
    try:
        rpc.update(
            state=status, details=username + "@" + device, small_image="python",
            large_image="fyutils",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"},
                     {"label": "View Project", "url": "https://github.com/NoahOnFyre/FyUTILS/"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def update_ssh_status(status):
    execute("title FyUTILS " + version + " - " + user + "@" + server + " - " + status)
    try:
        rpc.update(
            state="[REMOTE] " + status, details=user + "@" + server, small_image="ssh",
            large_image="fyutils",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"},
                     {"label": "View Project", "url": "https://github.com/NoahOnFyre/FyUTILS/"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def print_packet(x: scapy.packet.Packet):
    content = str(x)
    print(prefix() + content)


def resolve_fuel_information(file):
    fuel = open(fuel_content_dir + file, mode="rt")
    fuel_json = json.load(fuel)
    print(prefix("INFO", "FUEL") + "FUEL information of: " + file)
    print(prefix("INFO", "FUEL") + "FUEL name: " + fuel_json["name"])
    print(prefix("INFO", "FUEL") + "FUEL version: v" + fuel_json["version"])
    print(prefix("INFO", "FUEL") + "FUEL author: " + fuel_json["author"])
    print(prefix("INFO", "FUEL") + "FUEL description: " + fuel_json["description"])
    print(prefix("INFO", "FUEL") + "FUEL format: " + str(fuel_json["format"]))
    if fuel_json["format"] != SUPPORTED_FUEL_VERSION:
        print(prefix("ERROR", "FUEL") + "FUEL \"" + fuel_json["name"] + "\" isn't supported by this version of FyUTILS.")
        print(prefix("ERROR", "FUEL") + "The FUEL has to be deleted, because otherwise, it could cause problems.")
        time.sleep(1)
        fuel.close()
        os.remove(fuel_content_dir + file)
        return
    print(prefix("INFO", "FUEL") + "FUEL type: " + fuel_json["properties"]["type"])
    match fuel_json["properties"]["type"]:
        case "DEFAULT":
            print(prefix("INFO", "FUEL") + "FUEL command name: " + fuel_json["properties"]["command_name"])
            print(prefix("INFO", "FUEL") + "Head enabled: " + str(fuel_json["head"]["enabled"]))
            print(prefix("INFO", "FUEL") + "Body enabled: " + str(fuel_json["body"]["enabled"]))
            print(prefix("INFO", "FUEL") + "Argument length: " + str(fuel_json["head"]["argument_length"]))
            print(prefix("INFO", "FUEL") + "Command status: " + fuel_json["head"]["status"])
            fuels.update({fuel_json["properties"]["command_name"]: fuel_content_dir + file})

        case "MIXIN":
            print(prefix("WARN", "FUEL") + "WARNING: If you are a FUEL developer, please use a")
            print(prefix("WARN", "FUEL") + "default FUEL and use a command for your injection.")
            print(prefix("WARN", "FUEL") + "Support for mixins injecting on initialisation will be added soon.")
            print(prefix("WARN", "FUEL") + "If you aren't a developer, please remove the affected FUEL.")
            print(prefix("WARN", "FUEL") + "You can use: \"fuel remove " + fuel.name + "\" to remove it.")
            pause("INFO", "FUEL")

        case _:
            print(prefix("ERROR", "FUEL") + "FUEL type is not supported by this version.")
    fuel.close()


def color(): return src_color


def fuel_color(): return src_fuel_color


def accent_color(): return src_accent_color


def text_color(): return src_text_color


def true_color(): return src_true_color


def false_color(): return src_false_color


def warn_color(): return src_warn_color


def debug_color(): return src_debug_color


def pause(level: str = "INFO", protocol: str = "FyUTILS"): input(prefix(level.upper(), protocol) + "Press enter to continue. ")


def crash_log():
    temp = open(main_dir + "crash.log", mode="wb+")
    commands = "\n".join(executed_commands)
    data = f"""FyUTILS Traceback Crash log @ {datetime.datetime.now().strftime("%H:%M:%S")}
================================================================================

Variable stacktrace:
    - User specific:
        └> Username: {username}
        └> Device: {device}
        └> HWID: {hwid}
        └> Start time: {start_time}
        └> Directory: {current_dir}
        └> Version: {version}
        └> Thread count: {threads}
        └> Private IP: {private_ip}
    
    - Operating System specific:
        └> Operating System: {operating_system}
        └> Operating System version: {os_version}
    
    - Python specific:
        └> Python version: {python_version}
        
================================================================================

Command history:
{commands}

================================================================================
        
Python traceback:
{traceback.format_exc()}
"""

    temp.write(data.encode())
    temp.close()
    execute("explorer.exe /select,\"" + main_dir + "crash.log" + "\"")


def menu():
    execute("cls")
    print()
    print(color() + "  __________               _____  __   ________   ________   ______       ________")
    print(color() + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    print(color() + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \\ ")
    print(color() + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    print(color() + "  /_/         _\\__, /      \\____/      /_/        /___/      /_____/      /____/  ")
    print(color() + "             ___/  /")
    print(color() + "            /_____/ " + " "*5 + accent_color() + "v" + text_color() + version.replace(".", accent_color() + "." + text_color()) + accent_color() + " | " + text_color() + "Made by NoahOnFyre")
    print()
    print(accent_color() + "╔" + "═"*119)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Username: " + username)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Device: " + device)
    print(accent_color() + "║ " + accent_color() + "[" + color() + "VAR" + accent_color() + "] " + text_color() + "Version: " + version)
    if update_available:
        print(accent_color() + "╠" + "═"*119)
        print(accent_color() + "║ " + accent_color() + "[" + color() + "UPDATE" + accent_color() + "] " + text_color() + "A new version of FyUTILS is available! Install it now using \"update\".")
        for item in str(update_content).split("\r\n"):
            if not item.startswith("**Full Changelog**:"):
                if not item == "":
                    print(accent_color() + "║ " + accent_color() + "[" + color() + "UPDATE" + accent_color() + "] " + text_color() + item)
        print(accent_color() + "║ " + accent_color() + "[" + color() + "UPDATE" + accent_color() + "] " + text_color() + false_color() + version + accent_color() + " => " + true_color() + newest_version + text_color())
    print(accent_color() + "╚" + "═"*119)


# INIT PHASE
execute("title FyUTILS")

# Color initialisation
src_color = Fore.LIGHTBLUE_EX
src_fuel_color = Fore.LIGHTMAGENTA_EX
src_accent_color = Fore.LIGHTBLACK_EX
src_text_color = Fore.WHITE
src_true_color = Fore.GREEN
src_false_color = Fore.RED
src_warn_color = Fore.YELLOW
src_debug_color = Fore.MAGENTA

# Various stuff initialisation
executed_commands = []

# Config initialisation

temp = str(Path.home()) + "\\AppData\\Roaming\\FyUTILS"
if not os.path.exists(temp + "\\config.json"):
    os.makedirs(temp)
    config = open(temp + "\\config.json", mode="x")
    config_data = {
        "color": Fore.LIGHTBLUE_EX,
        "fuel_color": Fore.LIGHTMAGENTA_EX,
        "accent_color": Fore.LIGHTBLACK_EX,
        "text_color": Fore.WHITE,
        "true_color": Fore.GREEN,
        "false_color": Fore.RED,
        "warn_color": Fore.YELLOW,
        "debug_color": Fore.MAGENTA,
        "enable_debug": False
    }
    json.dump(config_data, config, indent=4)
    print(prefix() + "Config created!")
    config.close()

config = open(temp + "\\config.json", mode="rt+")

configuration = json.load(config)
src_color = configuration["color"]
src_fuel_color = configuration["fuel_color"]
src_accent_color = configuration["accent_color"]
src_text_color = configuration["text_color"]
src_true_color = configuration["true_color"]
src_false_color = configuration["false_color"]
src_warn_color = configuration["warn_color"]
src_debug_color = configuration["debug_color"]
debug_enabled = configuration["enable_debug"]

# Variable initialisation
try:
    # User specific stuff
    print(prefix("INFO", "Init") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INFO", "Init") + "Username: " + username)
    device = platform.node()
    print(prefix("INFO", "Init") + "Device: " + device)
    hwid = str(subprocess.check_output("wmic csproduct get uuid",), "UTF-8").split("\n")[1].strip()
    print(prefix("INFO", "Init") + "Hardware ID: " + hwid)
    start_time = time.time()
    print(prefix("INFO", "Init") + "Start time: " + str(start_time))
    current_dir = sys.path[0]
    print(prefix("INFO", "Init") + "Directory: " + current_dir)
    version = CURRENT_FYUTILS_VERSION
    print(prefix("INFO", "Init") + "Version: " + version)
    threads = multiprocessing.cpu_count()
    print(prefix("INFO", "Init") + "ThreadWorkers: " + str(threads))
    private_ip = socket.gethostbyname(socket.gethostname())
    print(prefix("INFO", "Init") + "Private IP: " + private_ip)
    wire_started = False
    print(prefix("INFO", "Init") + "WIRE started: " + str(wire_started))

    # OS specific stuff.
    operating_system = platform.system()
    print(prefix("INFO", "Init") + "Operating System: " + operating_system)
    os_version = platform.version()
    print(prefix("INFO", "Init") + "OS version: " + os_version)

    # Python specific stuff
    python_version = platform.python_version()
    print(prefix("INFO", "Init") + "Python version: " + python_version)

    # Directory specific stuff
    user_dir = str(Path.home())
    print(prefix("INFO", "Init") + "User specific directory: " + user_dir)
    appdata_dir = user_dir + "\\AppData"
    print(prefix("INFO", "Init") + "AppData directory: " + appdata_dir)
    main_dir = appdata_dir + "\\Roaming\\FyUTILS\\"
    print(prefix("INFO", "Init") + "FyUTILS AppData directory: " + main_dir)
    tmp_dir = main_dir + "tmp\\"
    print(prefix("INFO", "Init") + "Temp files directory: " + tmp_dir)
    download_content_dir = main_dir + "content\\"
    print(prefix("INFO", "Init") + "Download Content Location: " + download_content_dir)
    fuel_content_dir = main_dir + "fuels\\"
    print(prefix("INFO", "Init") + "FUEL Content Location: " + fuel_content_dir)

    # Create directories if they not exist.
    if not os.path.exists(main_dir):
        os.makedirs(main_dir)
        print(prefix("WARN", "FirstStart") + "Main directory didn't existed and has been created.")
        time.sleep(0.5)
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
        print(prefix("WARN", "FirstStart") + "Temporary storage directory didn't existed and has been created.")
        time.sleep(0.5)
    if not os.path.exists(download_content_dir):
        os.makedirs(download_content_dir)
        print(prefix("WARN", "FirstStart") + "Download content directory didn't existed and has been created.")
        time.sleep(0.5)
    if not os.path.exists(fuel_content_dir):
        os.makedirs(fuel_content_dir)
        print(prefix("WARN", "FirstStart") + "FUEL content directory didn't existed and has been created.")
        time.sleep(0.5)

    # URL specific stuff
    releases = "https://api.github.com/repos/NoahOnFyre/FyUTILS/releases"
    print(prefix("INFO", "Init") + "Releases URL: " + releases)

    # System components specific stuff
    cpu = platform.processor()
    print(prefix("INFO", "Init") + "CPU: " + cpu)
    memory_amount = psutil.virtual_memory().total
    print(prefix("INFO", "Init") + "Memory amount: " + str(round(memory_amount/1024/1024)) + "MB")
except Exception as e:
    print(prefix("ERROR", "Init") + "Failed to get system variables!")
    print(traceback.format_exc())
    print(prefix("ERROR", "Init") + "Shutting down...")
    pause("ERROR", "Init")
    sys.exit(2048)

# Update checker
print(prefix("INFO", "Updater") + "Checking for updates...")
try:
    releases_json = requests.get(releases).json()
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            release_download_url = ""
            continue
    update_content = newest_release["body"]
    newest_version = newest_release["tag_name"]
    if version_is_newer(version, newest_version):
        print(prefix("INFO", "Updater") + "A new version of FyUTILS is available!")
        print(prefix("INFO", "Updater") + "Current version identifier: " + version)
        print(prefix("INFO", "Updater") + "Newest version identifier: " + newest_version)
        update_available = True
    else:
        print(prefix("INFO", "Updater") + "No update found!")
        print(prefix("INFO", "Updater") + "Current version identifier: " + version)
        print(prefix("INFO", "Updater") + "Newest version identifier: " + newest_version)
        update_available = False
except Exception as e:
    print(prefix("WARN", "Updater") + "Checking for updates failed. Please check your internet connection.")
    print(prefix("WARN", "Updater") + "You won't receive any updates without internet connection.")
    update_available = False

# Discord RPC initialisation
try:
    print(prefix("INFO", "RichPresence") + "Setting presence ID...")
    presence_id = "1005822803997638696"
    print(prefix("INFO", "RichPresence") + "Presence ID set to: \"" + presence_id + "\".")
    print(prefix("INFO", "RichPresence") + "Initializing discord rich presence...")
    rpc = Presence(presence_id)
    print(prefix("INFO", "RichPresence") + "Connecting to discord...")
    rpc.connect()
    print(prefix("INFO", "RichPresence") + "Discord is connected...")
    update_status("Starting up...")
except:
    print(prefix("WARN", "RichPresence") + "Can't connect with the discord RPC.")
    time.sleep(0.25)

# FUEL initialisation

print(prefix("INFO", "FUEL") + "Initialising FUELS...")
fuels = {}
for file in os.listdir(fuel_content_dir):
    resolve_fuel_information(file)

print(prefix("INFO", "FUEL") + "FUELS initialized")

print(prefix("INFO", "Init") + "Initialisation phase completed!")
update_status("Initialisation phase completed!")

# INIT PHASE END

menu()
try:
    while True:
        print()
        update_status("Idle")
        try:
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
            request_raw = input(accent_color() + "╔═══[" + color() + username + accent_color() + "@" + text_color() + device + accent_color() + "]══(" + color() + "FyUTILS" + accent_color() + "/" + text_color() + version + accent_color() + ")══[" + text_color() + cwd_abbreviation + accent_color() + "]\n" +
                                accent_color() + "╚═══> " + text_color())
            request = request_raw.split(" ")
            cmd = request[0].lower()
            request.__delitem__(0)
            args = request

            executed_commands.append(request_raw)
            print()
        except KeyboardInterrupt:
            try:
                update_status("Shutting down...")
                print("\n" + prefix() + "Shutting down FyUTILS...")
                time.sleep(1)
                sys.exit(0)
            except KeyboardInterrupt:
                continue

        match cmd:
            case "flood":
                if len(args) < 2:
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
                            print(prefix() + "Attacking target: " + color() + target + accent_color() + ":" + color() + str(port) + text_color() + "..." + accent_color() + " - " + text_color() + "Attack: " + color() + str(i + 1) + accent_color(), end="\r")
                        except socket.error:
                            print()
                            print(prefix("WARN") + "Request " + color() + str(i) + text_color() + " failed.", end="\r")
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("WARN") + "Cannot disconnect from target!")

            case "portscan":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                activity_start = time.time()
                update_status("Scanning on " + target)

                try:
                    print(prefix() + "Preparing scan...")
                    for port in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1/1000)
                        result = sock.connect_ex((target, port))
                        print(prefix() + "Scanning Port... " + color() + str(port), end="\r")
                        if result == 0:
                            print(prefix() + "Port " + color() + str(port) + text_color() + " is open!" + " "*50)
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("WARN") + "Cannot disconnect from target!")

            case "sniff" | "traffic":
                update_status("Sniffing network...")
                activity_start = time.time()

                print(prefix() + "Starting network sniffer...")
                sniff(filter="ip", prn=print_packet)
                print(prefix() + "Canceling Action...")
                print(prefix() + "Stopping network sniffer...")
                print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "wire":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                action = args[0]
                update_status("Running WIRE")

                activity_start = time.time()

                if action == "start":
                    print(prefix("INFO", "WIRE") + "Starting WIRE service...")
                    if not wire_started:
                        if exec_code("netsh wlan show drivers") == 1:
                            wire_started = False
                            print(prefix("ERROR", "WIRE") + "WIRE can't be executed on your device.")
                        else:
                            wire_started = True
                            print(prefix("INFO", "WIRE") + "WIRE service started successfully!")
                    else:
                        wire_started = False
                        print(prefix("ERROR", "WIRE") + "WIRE service is already running!")
                        print(prefix("ERROR", "WIRE") + "You can restart it using \"wire restart\".")
                elif action == "connect":
                    if len(args) < 2:
                        print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                        continue
                    if not wire_started:
                        print(prefix("ERROR", "WIRE") + "WIRE service isn't running!")
                        continue
                    target = args[1]
                    execute("netsh wlan connect name=" + target)
                elif action == "stop":
                    if not wire_started:
                        wire_started = True
                        print(prefix("ERROR", "WIRE") + "WIRE service isn't running!")
                    else:
                        wire_started = False
                        print(prefix("INFO", "WIRE") + "WIRE service stopped successfully!")

            case "resolve":
                if len(args) < 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                action = args[0]
                target = args[1]
                activity_start = time.time()
                update_status("Resolving information about " + target)

                if action == "ip":
                    data = json.loads(requests.get("http://ipwho.is/" + socket.gethostbyname(target)).content.decode())
                    print(prefix() + "Resolved information of \"" + data["ip"] + "\"")
                    print(prefix() + "IP: " + data["ip"])
                    print(prefix() + "IP type: " + data["type"])
                    print(prefix() + "Continent: " + data["continent"])
                    print(prefix() + "Country: " + data["country"])
                    print(prefix() + "Region: " + data["region"])
                    print(prefix() + "City: " + data["city"])
                    print(prefix() + "Latitude: " + str(data["latitude"]))
                    print(prefix() + "Longitude: " + str(data["longitude"]))
                    print(prefix() + "Google Maps: " + f"https://www.google.com/maps/@{data['latitude']},{data['longitude']},10z")
                    print(prefix() + "EU country: " + str(data["is_eu"]))
                    print(prefix() + "Postal code: " + data["postal"])
                    print(prefix() + "System number (ASN): " + str(data["connection"]["asn"]))
                    print(prefix() + "Organisation (ORG): " + data["connection"]["org"])
                    print(prefix() + "Internet access provider (ISP): " + data["connection"]["isp"])
                    print(prefix() + "Domain: " + data["connection"]["domain"])
                    print(prefix() + "Timezone: " + data["timezone"]["id"])
                    print(prefix() + "UTC: " + data["timezone"]["utc"])
                elif action == "phone":
                    parsed_number = phonenumbers.parse(target)
                    location = geocoder.description_for_number(parsed_number, "en")
                    carrier = carrier.name_for_number(parsed_number, "en")
                    zone = timezone.time_zones_for_number(parsed_number)
                    print(prefix() + "Resolved information of \"" + target + "\"")
                    print(prefix() + "Location: " + location)
                    print(prefix() + "Carrier: " + carrier)
                    print(prefix() + "Timezone: " + str(zone))
                else:
                    print(prefix("ERROR") + "Action is not supported!")

            case "arp":
                activity_start = time.time()
                update_status("ARP scanning in " + private_ip + "...")

                try:
                    print(prefix() + "Make sure you have WinPcap or Npcap installed!")
                    print(prefix() + "Initialising ARP service...")
                    arp = ARP(pdst=private_ip + "/24")
                    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
                    packet = ether/arp
                    print(prefix() + "Sending ARP packets...")
                    content = srp(packet, timeout=2, verbose=0)[0]
                    clients = []
                    print(prefix() + "Receiving data from " + private_ip + "...")
                    for sent, received in content:
                        clients += [[received.psrc, received.hwsrc]]
                    print(prefix() + "Processing received data...")
                    print(prefix() + "Data received and processed.")
                    client_count = len(clients)
                    for i in range(client_count):
                        print(prefix() + accent_color() + "[" + color() + str(i) + accent_color() + "] " + text_color() + "IP: " + clients[i][0] + " MAC: " + clients[i][1])
                except KeyboardInterrupt:
                    print(prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "vars":
                print(prefix("INFO", "Init") + "Listing up system variables...")
                time.sleep(0.5)
                print(prefix("INFO", "Init") + "Username: " + username)
                print(prefix("INFO", "Init") + "Device: " + device)
                print(prefix("INFO", "Init") + "Hardware ID: " + hwid)
                print(prefix("INFO", "Init") + "Start time: " + str(start_time))
                print(prefix("INFO", "Init") + "Directory: " + current_dir)
                print(prefix("INFO", "Init") + "Version: " + version)
                print(prefix("INFO", "Init") + "ThreadWorkers: " + str(threads))
                print(prefix("INFO", "Init") + "Private IP: " + private_ip)
                print(prefix("INFO", "Init") + "Operating System: " + operating_system)
                print(prefix("INFO", "Init") + "OS version: " + os_version)
                print(prefix("INFO", "Init") + "Python version: " + python_version)
                print(prefix("INFO", "Init") + "User specific directory: " + user_dir)
                print(prefix("INFO", "Init") + "AppData directory: " + appdata_dir)
                print(prefix("INFO", "Init") + "FyUTILS AppData directory: " + main_dir)
                print(prefix("INFO", "Init") + "Temp files directory: " + tmp_dir)
                print(prefix("INFO", "Init") + "Download Content Location: " + download_content_dir)
                print(prefix("INFO", "Init") + "FUEL Content Location: " + fuel_content_dir)
                print(prefix("INFO", "Init") + "Releases URL: " + releases)
                print(prefix("INFO", "Init") + "CPU: " + cpu)
                print(prefix("INFO", "Init") + "Memory amount: " + str(round(memory_amount/1024/1024)) + "MB")

            case "checkport" | "portcheck":
                if len(args) < 2:
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
                        print(prefix() + "Port " + color() + str(port) + text_color() + " is open!")
                    else:
                        print(prefix("WARN") + "Port " + color() + str(port) + text_color() + " is not open!")
                    sock.close()
                except KeyboardInterrupt:
                    print(prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("WARN") + "Cannot disconnect from target!")
                print(prefix() + "Cleaning up...")

            case "ssh":
                if len(args) < 3:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                server = args[0]
                port = int(args[1])
                user = args[2]
                activity_start = time.time()
                update_status("Starting FySSH service...")

                print(prefix() + "Connecting to " + server + ":" + str(port) + " as " + user)
                print(prefix() + "Initialising SSH client...")
                ssh = paramiko.SSHClient()
                print(prefix() + "Loading host keys...")
                ssh.load_system_host_keys()
                print(prefix() + "Adding policy...")
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(prefix() + "Requesting user's password...")
                password = pwinput.pwinput(text_color() + "Enter password" + accent_color() + " > " + text_color(), "*")
                print(prefix() + "Connecting...")
                print()
                try:
                    ssh.connect(server, port=port, username=user, password=password)
                    while True:
                        try:
                            update_ssh_status("Idle")
                            ssh_cmd = input(accent_color() + "╔═══[" + fuel_color() + user + accent_color() + "@" + fuel_color() + server + accent_color() + ":" + fuel_color() + str(port) + accent_color() + "]═══(" + color() + "FySSH" + accent_color() + "/" + text_color() + version + accent_color() + ")" + "\n" + "╚═══" + accent_color() + "> " + text_color())
                            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                            update_ssh_status("Running: " + ssh_cmd)
                            print()
                            for line in ssh_stdout.readlines():
                                print(prefix("INFO", "Remote") + line, end="\r")
                            for line in ssh_stderr.readlines():
                                print(prefix("ERROR", "Remote") + line, end="\r")
                        except KeyboardInterrupt:
                            print("\n" + prefix() + "Canceling Action...")
                            break
                        except Exception as e:
                            print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                            print(prefix("ERROR") + str(e))
                            print()
                except Exception as e:
                    print(prefix("ERROR") + "Can't connect to SSH host. Please make sure, that the requested port is open.")
                    print(prefix("ERROR") + "SSH error: " + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                    print(prefix() + "Cleaning up...")
                    continue

                print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix() + "Disconnecting from " + color() + server + accent_color() + ":" + color() + str(port) + text_color() + "...")
                try:
                    ssh.close()
                except:
                    print(prefix("WARN") + "Cannot disconnect from target!")
                print(prefix() + "Cleaning up...")

            case "fetch":
                if len(args) < 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                filename = args[1]
                activity_start = time.time()
                update_status("Fetching: " + url)

                try:
                    print(prefix() + "Fetching " + url + "...")
                    fetch_content = requests.get(url).content
                    print(prefix() + "Content of " + url + " cached!")
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                    print(prefix() + "Writing content of " + url + " from cache to local storage!")

                    try:
                        open(download_content_dir + "\\" + filename, mode="xb").write(fetch_content)
                        execute("start explorer.exe " + download_content_dir)
                    except Exception as e:
                        print("\n" + prefix("ERROR") + "Could not save content to file.")
                        print(prefix("ERROR") + str(e))
                        print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                        print()
                except KeyboardInterrupt:
                    print()
                    print("\n" + prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()

            case "youtube":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                activity_start = time.time()
                update_status("Downloading: " + url)

                try:
                    youtube = YouTube(url)
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                        print(prefix() + "Media directory created!")
                    print(prefix() + "Download started!")
                    youtube.streams.get_highest_resolution().download(download_content_dir)
                    print(prefix() + f"Download finished in {time.time() - activity_start: 0.2f} seconds!")
                    execute("start explorer.exe " + download_content_dir)
                except KeyboardInterrupt:
                    print()
                    print("\n" + prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()

            case "log" | "crashes":
                update_status("Opening logs...")
                execute("explorer.exe /select,\"" + main_dir + "crash.log" + "\"")

            case "config" | "configuration" | "settings" | "preferences":
                if len(args) < 1:
                    update_status("Editing preferences...")
                    execute("explorer.exe /select,\"" + main_dir + "config.json" + "\"")
                    continue
                action = args[0]
                activity_start = time.time()
                update_status("Editing preferences...")
                if action == "reset":
                    print(prefix() + "Resetting config...")
                    config = open(main_dir + "config.json", mode="w+")
                    config_data = {
                        "color": Fore.LIGHTBLUE_EX,
                        "fuel_color": Fore.LIGHTMAGENTA_EX,
                        "accent_color": Fore.LIGHTBLACK_EX,
                        "text_color": Fore.WHITE,
                        "true_color": Fore.GREEN,
                        "false_color": Fore.RED,
                        "warn_color": Fore.YELLOW,
                        "debug_color": Fore.MAGENTA,
                        "enable_debug": False
                    }
                    json.dump(config_data, config, indent=4)
                    print(prefix() + "Config reset!")
                    config.close()
                else:
                    print(prefix("ERROR") + "Action is not supported!")

            case "streamhunter":
                activity_start = time.time()
                update_status("Searching for videos...")

                print(prefix() + "Searching for videos...")
                while True:
                    try:
                        identifier = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6)).lower()
                        time.sleep(0.5)
                        source = requests.get("https://streamable.com/" + identifier)
                        try:
                            if source.status_code != 404:
                                print(prefix() + "Valid link found! | https://streamable.com/" + identifier)
                        except Exception as e:
                            print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                            print(prefix("ERROR") + str(e))
                            print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                            break
                    except KeyboardInterrupt:
                        print(prefix() + "Canceling Action...")
                        print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                        break

            case "getip":
                update_status("Getting user's IP address...")
                print(prefix() + requests.get("https://api.ipify.org/").content.decode())

            case "fuels":
                print(prefix() + "Active FUELS:")
                for path in fuels.values():
                    print(prefix() + os.path.basename(path).split("/")[-1])

            case "fuel":
                if len(args) < 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                fuel_action = args[0]
                if len(args) == 2:
                    fuel_location = args[1]
                activity_start = time.time()

                if fuel_action == "install":
                    update_status("Installing FUEL...")
                    print(prefix() + "Installation process started!")
                    filename = fuel_location + ".json"
                    print(prefix() + "Using \"" + filename + "\" as target package.")
                    print(prefix() + "Checking FUEL directory...")
                    if os.path.exists(fuel_content_dir + filename):
                        print(prefix("ERROR") + "Package \"" + filename + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package is already installed.")
                        continue
                    print(prefix() + "Installing to: " + fuel_content_dir + "...")
                    print(prefix() + "Checking FUEL in NoahOnFyre/FUELS...")
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
                    print(prefix() + "Fetching FUEL from NoahOnFyre/FUELS...")
                    fuel_file_content = requests.get(fuel_download_url).content
                    print(prefix() + "Writing content to file...")
                    local_fuel_file = open(fuel_content_dir + filename, mode="xb")
                    local_fuel_file.write(fuel_file_content)
                    local_fuel_file.close()
                    local_fuel_file = open(fuel_content_dir + filename, mode="rt")
                    print(prefix() + "FUEL " + fuel_color() + filename + text_color() + " successfully installed to \"" + fuel_content_dir + "\".")
                    print(prefix() + "Adding FUEL to FyUTILS...")
                    local_fuel_file_json = json.load(local_fuel_file)
                    if local_fuel_file_json["properties"]["type"] == "DEFAULT":
                        fuels.update({local_fuel_file_json["properties"]["command_name"]: fuel_content_dir + filename})
                    local_fuel_file.close()
                    print(prefix() + f"Done! Took{time.time() - activity_start: 0.2f}s to install package " + fuel_color() + filename + text_color() + "!")

                elif fuel_action == "add":
                    update_status("Adding FUEL...")
                    print(prefix() + "Installation process started!")
                    filename = os.path.basename(fuel_location).split("/")[-1]
                    print(prefix() + "Checking FUEL directory...")
                    if os.path.exists(fuel_content_dir + filename):
                        print(prefix("ERROR") + "Package \"" + fuel_location + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package is already installed.")
                        continue
                    print(prefix() + "Installing to: " + fuel_content_dir + "...")
                    print(prefix() + "Copying FUEL from " + fuel_location + "...")
                    shutil.copy(fuel_location, fuel_content_dir)
                    local_fuel_file = open(fuel_content_dir + filename)
                    print(prefix() + "FUEL " + fuel_color() + filename + text_color() + " successfully copied to \"" + fuel_content_dir + "\".")
                    print(prefix() + "Adding FUEL to FyUTILS...")
                    local_fuel_file_json = json.load(local_fuel_file)
                    if local_fuel_file_json["properties"]["type"] == "DEFAULT":
                        fuels.update({local_fuel_file_json["properties"]["command_name"]: fuel_content_dir + filename})
                    local_fuel_file.close()
                    print(prefix() + f"Done! Took{time.time() - activity_start: 0.2f}s to install package " + fuel_color() + filename + text_color() + "!")

                elif fuel_action == "run":
                    update_status("Running FUEL...")
                    print(prefix() + "Installation process started!")
                    filename = fuel_location + ".json"
                    print(prefix() + "Using \"" + filename + "\" as target package.")
                    print(prefix() + "Installing to: " + tmp_dir + "...")
                    print(prefix() + "Checking FUEL in NoahOnFyre/FUELS...")
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
                    print(prefix() + "Fetching FUEL from NoahOnFyre/FUELS...")
                    fuel_file_content = requests.get(fuel_download_url).content
                    print(prefix() + "Writing content to file...")
                    local_fuel_file = open(tmp_dir + filename, mode="xb")
                    local_fuel_file.write(fuel_file_content)
                    local_fuel_file.close()
                    local_fuel_file = open(fuel_content_dir + filename, mode="rt")
                    print(prefix() + "FUEL " + fuel_color() + filename + text_color() + " temporarily installed to \"" + fuel_content_dir + "\".")
                    fuel_file = open(tmp_dir + filename, mode="rt")
                    args = input(prefix() + "Enter arguments to run: ").split(" ")
                    json_fuel_file = json.load(fuel_file)
                    if json_fuel_file["head"]["enabled"]:
                        if len(args) != json_fuel_file["head"]["argument_length"]:
                            print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                            continue
                        for entry in range(len(json_fuel_file["head"]["arguments"])):
                            exec(list(json_fuel_file["head"]["arguments"])[entry] + " = args[" + str(entry) + "]")
                        update_status(json_fuel_file["head"]["status"])

                    if json_fuel_file["body"]["enabled"]:
                        exec("\n".join(list(json_fuel_file["body"]["content"])))
                    print(prefix() + "Execution finished!")
                    print(prefix() + "Closing temporary file...")
                    fuel_file.close()
                    print(prefix() + "Deleting temporary file...")
                    os.remove(tmp_dir + filename)
                    print(prefix() + f"Done! Took{time.time() - activity_start: 0.2f}s to run package " + fuel_color() + filename + text_color() + "!")

                elif fuel_action == "remove":
                    update_status("Removing FUEL...")
                    filename = os.path.basename(fuel_location + ".json").split("/")[-1]
                    print(prefix() + "Unregistering " + fuel_content_dir + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        temp = open(fuel_content_dir + filename)
                        fuels.pop(json.load(temp)["properties"]["command_name"])
                        temp.close()
                    else:
                        print(prefix("ERROR") + "Package \"" + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix() + "Deleting " + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        os.remove(fuel_content_dir + filename)
                    else:
                        print(prefix("ERROR") + "Package \"" + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix() + f"Done! Took{time.time() - activity_start: 0.2f}s to remove package " + fuel_color() + filename)
                else:
                    print(prefix("ERROR") + "Action is not supported!")

            case "update":
                update_status("Updating FyUTILS...")

                if update_available:
                    print(prefix("INFO", "Updater") + "Update found!")
                    print(prefix("INFO", "Updater") + "Version Comparison: " + false_color() + version + accent_color() + " => " + true_color() + newest_version + text_color() + "...")
                    shutil.copy(current_dir + "\\main.py", tmp_dir + "\\BACKUP-" + version + ".py")
                    newest_file_content = requests.get(release_download_url).content
                    temp = open(current_dir + "\\main.py", mode="wb")
                    temp.write(newest_file_content)
                    print(prefix("INFO", "Updater") + "Update successfully installed!")
                    print(prefix("INFO", "Updater") + "Restarting FyUTILS...")
                    temp.close()
                    execute("start " + current_dir + "\\main.py")
                    sys.exit(512)
                else:
                    print(prefix("INFO", "Updater") + "You're running the latest version of FyUTILS!")
                    print(prefix("INFO", "Updater") + "Version comparison: " + true_color() + version + accent_color() + " == " + true_color() + newest_version + text_color() + "...")

            case "edit":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                filepath = args[0]
                activity_start = time.time()
                update_status("Editing " + filepath + "...")

                if not os.path.exists(filepath):
                    print(prefix("WARN") + "File not found!")
                    confirmation = input(prefix() + "Do you want to let FyUTILS create a new file? (y/n): ")
                    if confirmation.lower() == "n":
                        continue
                    file = open(filepath, "x+")
                    print(prefix() + "File created successfully.")
                    print(prefix() + "End file editing by entering \"END\".")
                else:
                    file = open(filepath, "w+")
                    print(prefix() + "File opened successfully.")
                    print(prefix() + "End file editing by entering \"END\".")
                ln = ""
                for i in range(1, sys.maxsize):
                    try:
                        line = input(str(i) + ": ")
                        if line == "END":
                            break
                        ln = ln + line + "\n"
                    except KeyboardInterrupt:
                        print("END")
                        print()
                        break
                print(prefix() + "Writing cached content to " + filepath + "...")
                file.writelines(ln)
                print(prefix() + "Saving file to " + filepath + "...")
                print(prefix() + "Closing " + filepath + "...")
                file.close()
                print(prefix() + "File is saved and closed!")
                print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "calc":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                calculation = args[0]
                activity_start = time.time()
                update_status("Calculating " + calculation)

                print(prefix() + calculation + " is " + str(eval(calculation)))

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
                    print(prefix() + "File opened successfully.")
                i = 1
                for line in file.readlines():
                    print(str(i) + ": " + line, end="\r")
                    i += 1
                print(prefix() + "Closing " + filepath + "...")
                file.close()
                print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "ls":
                try:
                    print(prefix() + "Content of " + os.getcwd())
                    for file in os.listdir(os.getcwd()):
                        if file.startswith("."):
                            if os.path.isfile(file):
                                print(prefix() + accent_color() + file)
                            elif os.path.isdir(file):
                                print(prefix() + accent_color() + "/" + file)
                        elif os.path.isfile(file):
                            print(prefix() + file)
                        elif os.path.isdir(file):
                            print(prefix() + true_color() + "/" + file)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print()

            case "shell":
                update_status("Executing system command \"" + request_raw.removeprefix("shell ") + "\"")

                execute(request_raw.removeprefix("shell "))

            case "exit":
                update_status("Shutting down...")
                print(prefix() + "Shutting down FyUTILS...")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(prefix() + "Canceling action")
                    continue
                print("logout")
                sys.exit(0)

            case "cd":
                if len(args) < 1:
                    print(prefix() + os.getcwd())
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
                        cwd_abbreviation = os.getcwd()
                    print(prefix() + cwd_abbreviation)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print()

            case "help":
                if len(args) < 1:
                    update_status("Viewing help...")
                    execute("start https://github.com/NoahOnFyre/FyUTILS#commands")
                    continue
                command = args[0]
                update_status("Viewing " + command + " in help...")
                execute("start https://github.com/NoahOnFyre/FyUTILS#" + command)

            case "raise":
                update_status("Raising exception...")
                raise Exception("Executed by raise command.")

            case "clear" | "rl" | "reload" | "cls":
                update_status("Reloading...")
                execute("cls")
                menu()

            case "restart" | "rs":
                print("logout")
                execute("start " + current_dir + "\\main.py")
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
                    if exec_code(request_raw) == 1:
                        update_status("Executing " + cmd)
                        print(prefix("ERROR") + "Invalid command: \"" + cmd + "\".")
                    else:
                        update_status("Executing " + cmd)
                        execute(request_raw)
except Exception as e:
    execute("title FyUTILS Crash Handler - Crash Log")
    print(prefix("ERROR", "Crash") + "FyUTILS CRASH LOG @ " + datetime.datetime.now().strftime("%H:%M:%S"))
    print(prefix("ERROR", "Crash") + "Error: " + str(e))
    print(prefix("ERROR", "Crash") + "The full crash log has been saved to: " + main_dir + "crash.log")
    print(prefix("ERROR", "Crash") + "When you want to file an issue, please remember to also upload your crash.log file.")
    crash_log()
    pause("ERROR", "Crash")
    sys.exit(1024)
