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
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Packet
from packaging import version as version_parser
from scapy.layers.l2 import ARP, Ether, srp
from scapy.all import sniff
from colorama import Fore, Back, init
from phonenumbers import geocoder, carrier, timezone
from pypresence import Presence
from pytube import YouTube

init(convert=True)
CURRENT_FYUTILS_VERSION = "1.12.2"


def prefix(level: str = "INFO"):
    if level == "INFO":
        return BG_BLUE + " " + BLACK + level + RESET + " " + BG_RESET + " " + RESET
    elif level == "WARN":
        return BG_YELLOW + " " + BLACK + level + RESET + " " + BG_RESET + " " + RESET
    elif level == "ERROR":
        return BG_RED + " " + BLACK + level + RESET + " " + BG_RESET + " " + RED
    elif level == "DEBUG":
        return BG_MAGENTA + " " + BLACK + level + RESET + " " + BG_RESET + " " + RESET
    else:
        return BG_BLUE + " " + BLACK + level + RESET + " " + BG_RESET + " " + RESET


def execute(command: str):
    subprocess.call(command, shell=True)


def exec_silent(command: str):
    subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


def exec_code(command: str):
    return subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


def version_is_newer(current: str, target: str):
    current_version = version_parser.parse(current)
    target_version = version_parser.parse(target)
    return current_version < target_version


def update_status(status: str):
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
        pass


def update_ssh_status(status: str):
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
        pass


def api_request(path: str):
    return requests.get("https://api.github.com" + path, auth=(auth_name, auth_token))


def print_packet(packet: Packet):
    if packet.haslayer(IP):
        packet_src = str(packet[IP].src)
        packet_dst = str(packet[IP].dst)
        address_type = "v4"
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        else:
            protocol = "RAW"
        packet_prefix = GRAY + "[" + BLUE + protocol + GRAY + "/" + RESET + address_type + GRAY + "]" + RESET + " "
        print(prefix() + packet_prefix + packet_src + GRAY + " -> " + BLUE + packet_dst)
    else:
        packet_src = str(packet.src)
        packet_dst = str(packet.dst)
        packet_prefix = GRAY + "[" + BLUE + "RAW" + GRAY + "/" + RESET + "v6" + GRAY + "]" + RESET + " "
        print(prefix() + packet_prefix + packet_src + GRAY + " -> " + BLUE + packet_dst)


def open_file(path: str):
    execute("start " + path)


def get_fuels():
    fuel_list = os.listdir(fuel_content_dir)
    map = {}
    for fuel in fuel_list:
        with open(fuel_content_dir + fuel + "\\cmd.props") as file:
            name = json.load(file)["name"]
        map.update({name: fuel})
    return map


def run_fuel(command_name: str, directory: str, args: list[str]):
    activity_start = time.time()
    args = args
    update_status("Running FUEL \"" + command_name + "\"")
    for fuel in get_fuels().values():
        if not os.listdir(fuel_content_dir + fuel).__contains__("cmd.props"):
            print(prefix("ERROR") + "Package \"" + fuel.replace("+", "/") + "\" is invalid.")
            return
        with open(fuel_content_dir + fuel + "\\cmd.props") as file:
            data = json.load(file)
            name = data["name"]
        if name.lower() == command_name:
            print(prefix() + "Starting " + fuel + "...")
            if os.listdir(fuel_content_dir + fuel).__contains__("core.fuel"):
                with open(fuel_content_dir + fuel + "\\core.fuel", mode="rb") as file:
                    exec(file.read())
            elif os.listdir(fuel_content_dir + fuel).__contains__("main.py"):
                print(prefix("WARN") + "No FUEL main class found!")
                confirmation = input(prefix("WARN") + "Fallback to deprecated main.py? (y/n): ")
                if confirmation.lower() == "n":
                    return
                with open(fuel_content_dir + fuel + "\\main.py", mode="rb") as file:
                    exec(file.read())
            else:
                print(prefix("ERROR") + "No FUEL main class found!")
    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")


def format_boolean(boolean: bool):
    if boolean:
        return GREEN + "Yes"
    elif not boolean:
        return RED + "No"
    else:
        return RED + "Not available"


def format_float(float: float | str):
    f = str(float).split(".")
    return BLUE + f[0] + GRAY + "." + BLUE + f[1] + RESET


def pause(level: str = "INFO"):
    input(prefix(level.upper()) + "Press enter to continue. ")


def download_repo_files(repo_data: list):
    for entry in range(len(repo_data)):
        filename = repo_data[entry]["name"]
        file_type = repo_data[entry]["type"]
        file_size = str(repo_data[entry]["size"]) + " Bytes"
        file_download_url = repo_data[entry]["download_url"]
        if file_type == "dir":
            continue
        print(prefix() + "Fetching " + BLUE + filename + GRAY + " (" + RESET + file_size + GRAY + ")" + RESET + "...")
        file_content = requests.get(file_download_url).content
        with open(directory + filename, "wb") as tmp:
            tmp.write(file_content)


def crash_log():
    execute("title FyUTILS Crash Handler - Crash Log")
    print(prefix("ERROR") + "FyUTILS CRASH LOG @ " + datetime.datetime.now().strftime("%H:%M:%S"))
    print(prefix("ERROR") + "Error: " + str(e))
    print(prefix("ERROR") + "Learn how to file an issue: https://github.com/NoahOnFyre/FyUTILS/issues/40")
    temp = open(main_dir + "crash.log", mode="wb")
    data = f"""FyUTILS Traceback Crash log @ {datetime.datetime.now().strftime("%H:%M:%S")}

================================================================================

Variable stacktrace:
    - User specific:
        └> Username: {username}
        └> Device: {device}
        └> Hardware-ID: {hwid}
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
        
Python traceback:
{traceback.format_exc()}
"""

    temp.write(data.encode())
    temp.close()
    open_file(main_dir + "crash.log")
    pause("ERROR")
    sys.exit(1024)


def menu():
    execute("cls")
    print(BLUE + "  __________               _____  __   ________   ________   ______       ________")
    print(BLUE + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    print(BLUE + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \\ ")
    print(BLUE + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    print(BLUE + "  /_/         _\\__, /      \\____/      /_/        /___/      /_____/      /____/  ")
    print(BLUE + "             ___/  /")
    print(BLUE + "            /_____/ " + " "*5 + GRAY + "v" + RESET + version.replace(".", GRAY + "." + RESET) + GRAY + " | " + RESET + "Made by NoahOnFyre")
    print()
    print(GRAY + "╔" + "═"*119)
    print(GRAY + "║ " + RESET + "Version       " + GRAY + ": " + BLUE + version.replace(".", GRAY + "." + BLUE))
    print(GRAY + "║ " + RESET + "Authenticated " + GRAY + ": " + BLUE + format_boolean(authenticated))
    print(GRAY + "║ " + RESET + "Startup time  " + GRAY + ": " + BLUE + format_float(startup_time) + BLUE + "s")
    if update_available:
        print(GRAY + "╠" + "═"*119)
        print(GRAY + "║ " + RESET + "A new version of FyUTILS is available!")
        print(GRAY + "║ " + RESET + RED + version + GRAY + " => " + GREEN + newest_version + GRAY + " | " + RESET + "Run \"update\" to update your instance.")
    print(GRAY + "╚" + "═"*119)


# INIT PHASE
execute("title FyUTILS - Initialization phase")

# Color initialisation
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
BLACK = Fore.BLACK
WHITE = Fore.WHITE
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

BG_RED = Back.RED
BG_BLUE = Back.BLUE
BG_GREEN = Back.GREEN
BG_YELLOW = Back.YELLOW
BG_MAGENTA = Back.MAGENTA
BG_CYAN = Back.CYAN
BG_BLACK = Back.BLACK
BG_WHITE = Back.WHITE
BG_GRAY = Back.LIGHTBLACK_EX
BG_RESET = Back.RESET

# Variable initialisation
activity_start = time.time()

# Generic stuff
print(prefix() + "Initializing system variables...")
username = os.getlogin()
device = platform.node()
try:
    hwid = str(subprocess.check_output("wmic csproduct get uuid",), "UTF-8").split("\n")[1].strip()
except:
    print(prefix("ERROR") + "Failed to get HWID.")
start_time = time.time()
current_dir = sys.path[0]
version = CURRENT_FYUTILS_VERSION
threads = multiprocessing.cpu_count()
private_ip = socket.gethostbyname(socket.gethostname())
wire_started = False

# OS specific stuff.
operating_system = platform.system()
os_version = platform.version()

# Python specific stuff
python_version = platform.python_version()

# Directory specific stuff
user_dir = str(Path.home())
appdata_dir = user_dir + "\\AppData\\"
main_dir = appdata_dir + "Roaming\\FyUTILS\\"
tmp_dir = main_dir + "tmp\\"
download_content_dir = main_dir + "content\\"
fuel_content_dir = main_dir + "fuels\\"

# Create directories if they not exist.
if not os.path.exists(main_dir):
    os.makedirs(main_dir)
    print(prefix("WARN") + "Main directory didn't existed and has been created.")
    time.sleep(1)
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)
    print(prefix("WARN") + "Temporary storage directory didn't existed and has been created.")
    time.sleep(1)
if not os.path.exists(download_content_dir):
    os.makedirs(download_content_dir)
    print(prefix("WARN") + "Download content directory didn't existed and has been created.")
    time.sleep(1)
if not os.path.exists(fuel_content_dir):
    os.makedirs(fuel_content_dir)
    print(prefix("WARN") + "FUEL content directory didn't existed and has been created.")
    time.sleep(1)

# URL specific stuff
releases = "https://api.github.com/repos/NoahOnFyre/FyUTILS/releases"

# System components specific stuff
cpu = platform.processor()
memory_amount = psutil.virtual_memory().total
print(prefix() + f"Variable initialization took{time.time() - activity_start: 0.2f}s")

# Authentication initialization
activity_start = time.time()
print(prefix() + "Checking for authentication file...")
if os.path.exists(main_dir + "\\" + "auth.json"):
    with open(main_dir + "\\" + "auth.json", "r") as file:
        data = json.load(file)
        auth_name = data["name"]
        auth_token = data["token"]
        authenticated = True
else:
    auth_name = None
    auth_token = None
    authenticated = False
print(prefix() + f"Authentication initialization took{time.time() - activity_start: 0.2f}s")

# Update checker
activity_start = time.time()
print(prefix() + "Checking for updates...")
try:
    releases_json = requests.get(releases, auth=(auth_name, auth_token)).json()
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        release_download_url = ""
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            release_download_url = ""
            continue
    newest_version_note = newest_release["body"]
    newest_version = newest_release["tag_name"]
    if version_is_newer(version, newest_version):
        update_available = True
    else:
        update_available = False
except Exception as e:
    print(prefix("WARN") + "Checking for updates failed. Please check your internet connection.")
    update_available = False
print(prefix() + f"Update checker took{time.time() - activity_start: 0.2f}s")

print(prefix() + "Initialisation phase completed!")
update_status("Initialisation phase completed!")
startup_time = float(f"{time.time() - activity_start: 0.2f}")
print(prefix() + "Initialization took " + format_float(startup_time) + "seconds")

# INIT PHASE END

menu()

# Discord RPC initialization
try:
    presence_id = "1005822803997638696"
    rpc = Presence(presence_id)
    rpc.connect()
    update_status("Starting up...")
except Exception:
    print()
    print(prefix("WARN") + "Can't connect with the discord RPC.")
    time.sleep(0.25)

try:
    while True:
        print()
        update_status("Idle")
        try:
            if os.getcwd() == current_dir:
                cwd_abbreviation = "."
            elif os.getcwd() == "C:\\":
                cwd_abbreviation = "/"
            elif os.getcwd() == user_dir:
                cwd_abbreviation = "~"
            elif os.getcwd() == main_dir.removesuffix("\\"):
                cwd_abbreviation = "@"
            else:
                cwd_abbreviation = os.getcwd()
            request_raw = input(GRAY + "╔═══[" + BLUE + username + GRAY + "@" + RESET + device + GRAY + "]══(" + BLUE + "FyUTILS" + GRAY + "/" + RESET + version + GRAY + ")══[" + RESET + cwd_abbreviation + GRAY + "]\n" +
                                GRAY + "╚═══> " + RESET)
            request = request_raw.split(" ")
            cmd = request[0].lower()
            request.__delitem__(0)
            args = request
            print()
        except KeyboardInterrupt:
            update_status("Shutting down...")
            print("\n")
            print(prefix() + "Shutting down FyUTILS...")
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print(prefix() + "Canceling action")
                continue
            sys.exit(0)

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
                            print(prefix() + "Attacking target: " + BLUE + target + GRAY + ":" + BLUE + str(port) + RESET + "..." + GRAY + " - " + RESET + "Attack: " + BLUE + str(i + 1) + GRAY, end="\r")
                        except socket.error:
                            print()
                            print(prefix("WARN") + "Request " + BLUE + str(i) + RESET + " failed.", end="\r")
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
                except Exception:
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
                        print(prefix() + "Scanning Port... " + BLUE + str(port), end="\r")
                        if result == 0:
                            print(prefix() + "Port " + BLUE + str(port) + RESET + " is open!" + " "*50)
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
                except Exception:
                    print(prefix("WARN") + "Cannot disconnect from target!")

            case "sniff" | "traffic":
                update_status("Sniffing network...")
                activity_start = time.time()

                print(prefix() + "Starting network sniffer...")
                sniff(prn=print_packet)
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
                    print(prefix() + "Starting WIRE service...")
                    if not wire_started:
                        if exec_code("netsh wlan show drivers") == 1:
                            wire_started = False
                            print(prefix("ERROR") + "WIRE can't be executed on your device.")
                        else:
                            wire_started = True
                            print(prefix() + "WIRE service started successfully!")
                    else:
                        wire_started = False
                        print(prefix("ERROR") + "WIRE service is already running!")
                        print(prefix("ERROR") + "You can restart it using \"wire restart\".")
                elif action == "connect":
                    if len(args) < 2:
                        print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                        continue
                    if not wire_started:
                        print(prefix("ERROR") + "WIRE service isn't running!")
                        continue
                    target = args[1]
                    execute("netsh wlan connect name=" + target)
                elif action == "stop":
                    if not wire_started:
                        wire_started = True
                        print(prefix("ERROR") + "WIRE service isn't running!")
                    else:
                        wire_started = False
                        print(prefix() + "WIRE service stopped successfully!")

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
                    print(prefix() + "Latitude: " + format_float(data["latitude"]))
                    print(prefix() + "Longitude: " + format_float(data["longitude"]))
                    print(prefix() + "Google Maps: " + f"https://www.google.com/maps/@{data['latitude']},{data['longitude']},10z")
                    print(prefix() + "EU country: " + format_boolean(data["is_eu"]))
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
                    phone_carrier = carrier.name_for_number(parsed_number, "en")
                    zone = timezone.time_zones_for_number(parsed_number)
                    print(prefix() + "Resolved information of \"" + target + "\"")
                    print(prefix() + "Location: " + location)
                    print(prefix() + "Carrier: " + phone_carrier)
                    print(prefix() + "Timezone: " + str(zone))
                elif action == "socials":
                    found_accounts = []
                    social_account_sites = [
                        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
                        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
                        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
                        {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
                        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
                        {"url": "https://www.github.com/{}", "name": "GitHub"},
                        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
                        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
                        {"url": "https://www.youtube.com/{}", "name": "Youtube"},
                        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
                        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
                        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
                        {"url": "https://www.medium.com/@{}", "name": "Medium"},
                        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
                        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
                        {"url": "https://www.telegram.me/{}", "name": "Telegram"}
                    ]
                    print(prefix("WARN") + "Please consider, that this might output false information, if you're not logged in.")
                    for site in social_account_sites:
                        url = site["url"].format(target)
                        response = requests.get(url)
                        if response.status_code != 404:
                            print(prefix() + target + "'s " + site["name"] + "-Account: " + site["url"].format(target))
                        else:
                            print(prefix("WARN") + "This person has no " + site["name"] + " account!")

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
                        print(prefix() + GRAY + "[" + BLUE + str(i) + GRAY + "] " + RESET + "IP: " + clients[i][0] + " MAC: " + clients[i][1])
                except KeyboardInterrupt:
                    print(prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "vars" | "variables" | "var":
                print(prefix() + "Listing up system variables...")
                time.sleep(0.5)
                print(prefix() + "Username: " + username)
                print(prefix() + "Device: " + device)
                print(prefix() + "Hardware ID: " + hwid)
                print(prefix() + "Start time: " + str(start_time))
                print(prefix() + "Directory: " + current_dir)
                print(prefix() + "Version: " + version)
                print(prefix() + "ThreadWorkers: " + str(threads))
                print(prefix() + "Private IP: " + private_ip)
                print(prefix() + "WIRE started: " + format_boolean(wire_started))
                print(prefix() + "Operating System: " + operating_system)
                print(prefix() + "OS version: " + os_version)
                print(prefix() + "Python version: " + python_version)
                print(prefix() + "User specific directory: " + user_dir)
                print(prefix() + "AppData directory: " + appdata_dir)
                print(prefix() + "FyUTILS AppData directory: " + main_dir)
                print(prefix() + "Temp files directory: " + tmp_dir)
                print(prefix() + "Download Content Location: " + download_content_dir)
                print(prefix() + "FUEL Content Location: " + fuel_content_dir)

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
                        print(prefix() + "Port " + BLUE + str(port) + RESET + " is open!")
                    else:
                        print(prefix("WARN") + "Port " + BLUE + str(port) + RESET + " is not open!")
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
                except Exception:
                    print(prefix("WARN") + "Cannot disconnect from target!")

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
                password = pwinput.pwinput(RESET + "Enter password" + GRAY + " > " + RESET, "*")
                print(prefix() + "Connecting...")
                print()
                try:
                    ssh.connect(server, port=port, username=user, password=password)
                    while True:
                        try:
                            update_ssh_status("Idle")
                            ssh_cmd = input(GRAY + "╔═══[" + MAGENTA + user + GRAY + "@" + MAGENTA + server + GRAY + ":" + MAGENTA + str(port) + GRAY + "]═══(" + BLUE + "FySSH" + GRAY + "/" + RESET + version + GRAY + ")" + "\n" + "╚═══" + GRAY + "> " + RESET)
                            if ssh_cmd == "exit":
                                print("\n" + prefix() + "Canceling Action...")
                                print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                                break
                            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                            update_ssh_status("Running: " + ssh_cmd)
                            print()
                            for line in ssh_stdout.readlines():
                                print(prefix() + line, end="\r")
                            for line in ssh_stderr.readlines():
                                print(prefix("ERROR") + line, end="\r")
                        except KeyboardInterrupt:
                            print("\n" + prefix() + "Canceling Action...")
                            print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                            break
                        except Exception as e:
                            print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                            print(prefix("ERROR") + str(e))
                            print()
                except Exception as e:
                    print(prefix("ERROR") + "Can't connect to SSH host. Please make sure, that the requested port is open.")
                    print(prefix("ERROR") + "SSH error: " + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                    continue

                print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix() + "Disconnecting from " + BLUE + server + GRAY + ":" + BLUE + str(port) + RESET + "...")
                try:
                    ssh.close()
                except Exception:
                    print(prefix("WARN") + "Cannot disconnect from target!")

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
                open_file(main_dir + "crash.log")

            case "dir" | "open":
                if len(args) < 1:
                    execute("explorer.exe " + os.getcwd())
                    continue
                path = args[0]

                match path:
                    case "~":
                        path = user_dir

                    case ".":
                        path = current_dir

                    case "@":
                        path = main_dir

                    case "/":
                        path = "C:\\"

                    case _:
                        path = path
                execute("explorer.exe " + path)

            case "config" | "configuration" | "settings" | "preferences":
                if len(args) < 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                action = args[0]
                activity_start = time.time()
                update_status("Editing preferences...")
                print(prefix() + "The config system is currently maintained.")

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
                for key in get_fuels():
                    print(prefix() + BLUE + get_fuels()[key].split("+")[0] + GRAY + "/" + RESET + get_fuels()[key].split("+")[1] + " " + GRAY + "(" + RESET + key + GRAY + ")")

            case "fuel":
                if len(args) < 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                action = args[0]
                package = args[1]
                activity_start = time.time()

                match action:
                    case "install":
                        print(prefix() + "Checking connection...")
                        print(prefix() + "Decrypting package information...")
                        package_information = package.split("/")
                        repo_author = package_information[0]
                        repo_name = package_information[1]
                        print(prefix() + "Resolving GIT repository...")
                        repo_content_url = "https://api.github.com/repos/" + repo_author + "/" + repo_name + "/contents"
                        repo_data = requests.get(repo_content_url).json()
                        print(prefix() + "Initializing local environment...")
                        directory = fuel_content_dir + repo_author + "+" + repo_name + "\\"
                        print(prefix() + "Creating folder...")
                        os.mkdir(directory)
                        print(prefix() + "Fetching from " + BLUE + repo_author + GRAY + "/" + RESET + repo_name + " ...")
                        download_repo_files(repo_data)
                        for file in os.listdir(directory):
                            if file.removeprefix(directory) == "requirements.txt":
                                print(prefix() + "Installing python dependencies...")
                                print(prefix() + "This may take a while.")
                                exec_silent("pip install -r " + directory + "requirements.txt")
                                print(prefix() + "Requirements successfully installed!")
                        print(prefix() + "Package successfully installed!")

                    case "remove":
                        package_information = package.split("/")
                        repo_author = package_information[0]
                        repo_name = package_information[1]
                        directory = fuel_content_dir + repo_author + "+" + repo_name + "\\"
                        if os.path.exists(directory):
                            shutil.rmtree(directory)
                            print(prefix() + "Package successfully removed!")
                        else:
                            print(prefix("ERROR") + "The package \"" + package + "\" isn't installed!")

            case "update":
                update_status("Updating FyUTILS...")

                if update_available:
                    print(prefix() + "Update found!")
                    print(prefix() + "Version Comparison: " + RED + version + GRAY + " => " + GREEN + newest_version + RESET + "...")
                    shutil.copy(current_dir + "\\main.py", tmp_dir + "\\BACKUP-" + version + ".py")
                    newest_file_content = requests.get(release_download_url).content
                    temp = open(current_dir + "\\main.py", mode="wb")
                    temp.write(newest_file_content)
                    print(prefix() + "Update successfully installed!")
                    print(prefix() + "Restarting FyUTILS...")
                    temp.close()
                    execute("start " + current_dir + "\\main.py")
                    sys.exit(512)
                else:
                    print(prefix() + "You're running the latest version of FyUTILS!")
                    print(prefix() + "Version comparison: " + GREEN + version + GRAY + " == " + GREEN + newest_version + RESET + "...")

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
                                print(prefix() + GRAY + file)
                            elif os.path.isdir(file):
                                print(prefix() + GRAY + "/" + file)
                        elif os.path.isfile(file):
                            print(prefix() + file)
                        elif os.path.isdir(file):
                            print(prefix() + GREEN + "/" + file)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print()

            case "shell":
                update_status("Executing system command \"" + request_raw.removeprefix("shell ") + "\"")

                execute(request_raw.removeprefix("shell"))

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

                    case ".":
                        change_dir = current_dir

                    case "@":
                        change_dir = main_dir

                    case "/":
                        change_dir = "C:\\"

                    case _:
                        change_dir = change_dir

                try:
                    os.chdir(change_dir)
                    print(prefix() + change_dir)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print()

            case "help":
                if len(args) < 1:
                    update_status("Viewing help...")
                    execute("start https://noahonfyre.github.io/FyUTILS#commands")
                    continue
                section = args[0]
                update_status("Viewing " + section + " in help...")
                execute("start https://noahonfyre.github.io/FyUTILS#" + section)

            case "raise":
                update_status("Raising exception...")
                raise Exception("Executed by raise command.")

            case "clear" | "rl" | "reload" | "cls":
                update_status("Reloading...")
                execute("cls")
                menu()

            case "restart" | "rs":
                update_status("Restarting...")
                print("logout")
                execute("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case _:
                for fuel in get_fuels().keys():
                    if fuel.lower() == cmd.lower():
                        run_fuel(cmd, get_fuels()[fuel], args)
                        break
                else:
                    update_status("Executing " + cmd)
                    execute(request_raw)

except Exception as e:
    crash_log()
