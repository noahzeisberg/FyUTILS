try:
    import os
    import platform
    import sys
    import time
    import random
    import socket
    import requests
    import string
    import threading
    import paramiko
    import getpass
    import psutil
    import re
    import subprocess
    import winreg
    from datetime import datetime
    from colorama import Fore, init
    from pypresence import Presence
    from concurrent.futures import ThreadPoolExecutor
except:
    os.system("cls")
    print("FyUTILS has detected a problem and has been started in recovery mode.")
    print("If you want to know how you can solve these problems using recovery mode")
    print("paste this link into your browser: https://docs.onfyre.net/FyUTILS/recovery")
    print("")
    while True:
        recovery_cmd = input("RECOVERY >>> ")
        if recovery_cmd == "autofix" or recovery_cmd == "auto":
            print("")
            activity_start = time.time()
            print("Searching for errors...")
            time.sleep(3)
            try:
                import os
                import platform
                import sys
                import time
                import random
                import socket
                import requests
                import string
                import threading
                import paramiko
                import getpass
                import psutil
                import re
                import subprocess
                import winreg
                import whois
                from datetime import datetime
                from colorama import Fore, init
                from pypresence import Presence
                from concurrent.futures import ThreadPoolExecutor
                print("Imports working fine!")
                time.sleep(1)
                print("We can't find a problem in your installation. We recommend you to reinstall FyUTILS from")
                print("the official sources. Here's the URL: https://github.com/NoahOnFyre/FyUTILS/releases/latest")
                print("")
            except:
                print("Error identified! You can fix it using 'inst piplibs' in recovery mode.")
                print("")

        elif recovery_cmd == "inst piplibs":
            activity_start = time.time()
            print("Installing PyPi librarys...")
            time.sleep(3)
            os.system("pip install paramiko")
            os.system("pip install colorama")
            os.system("pip install datetime")
            os.system("pip install pypresence")
            os.system("pip install requests")
            os.system("pip install concurrent")
            os.system("pip install psutil")
            print("")
            print("-"*100)
            print("")
            print(f"Done! Took {time.time()-activity_start:0.2f}s to install PyPi librarys.")
            print("You can exit recovery mode by simply")
            os.system("pause")
            os.system("start " + sys.path.__getitem__(0) + "\\FyUTILS.py")
            sys.exit()

        elif recovery_cmd == "exit":
            print("")
            print("Exiting FyUTILS recovery...")
            time.sleep(1)
            sys.exit()
        else:
            os.system(recovery_cmd)

init(convert=True)


def get_usage(arg):
    try:
        if arg == "CPU":
            return psutil.cpu_percent()
        else:
            return None
    except Exception as e:
        print(e)


def uid_gen(size):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for char in range(size))


def prefix(arg):
    thread_name = threading.current_thread().name
    if arg == "INFO":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.GREEN + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    elif arg == "WARN":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.YELLOW + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    elif arg == "ERROR":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.RED + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    elif arg == "INIT":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTBLUE_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    elif arg == "DEBUG":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTRED_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    elif arg == "SUCCESS":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTGREEN_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    else:
        pre = "FAILED TO LOAD PREFIX (unexpected argument)"
    return pre


def update_status(state):
    try:
        os.system("title FyUTILS " + version + "-" + version_type + " - " + username + "@" + device + " - " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state=state, details=username + "@" + device, small_image="python",
                   large_image="main",
                   buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python", large_text="FyUTILS v" + version + "-" + version_type,
                   start=int(rpc_start_time))
    except:
        None


def update_ssh_status(state):
    try:
        os.system("title FyUTILS " + version + "-" + version_type + " - " + ssh_user + "@" + ssh_server + " - " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state="[FySSH] " + state, details=ssh_user + "@" + ssh_server, small_image="python",
                   large_image="main",
                   buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python", large_text="FyUTILS v" + version + "-" + version_type,
                   start=int(rpc_start_time))
    except:
        None


def add_command_detail(state):
    try:
        os.system(
            "title FyUTILS " + version + "-" + version_type + " - " + username + "@" + device + " - " + "Running: " + cmd + " " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state="Running: " + cmd + " " + state, details=username + "@" + device, small_image="python",
                   large_image="main",
                   buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python", large_text="FyUTILS v" + version + "-" + version_type,
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
    print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
    try:
        if update_available:
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[UPDATE] " + Fore.WHITE + "A new version of FyUTILS is available!")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[UPDATE] " + Fore.WHITE + "Current: " + version + "-" + version_type)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[UPDATE] " + Fore.WHITE + "Target: " + target_version + "-STABLE")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[UPDATE] " + Fore.WHITE + "You can update this instance by running 'update'.")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╠" + "═" * 119)
        else:
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[UPDATE] " + Fore.WHITE + "You're running the latest version of FyUTILS!")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╠" + "═" * 119)
    except:
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "║ " + Fore.RED + "[WARNING] " + Fore.WHITE + "You are running FyUTILS without an internet connection. Many features will be disabled!")
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Username:  " + username)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Device:    " + device)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + version_type)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")


os.system("title Initializing RPC...")
print(prefix("INIT") + "Initializing RPC...")

try:
    rpc = Presence("1005822803997638696")
    rpc.connect()
    rpc_start_time = time.time()
    update_status("Starting up...")
except:
    print(prefix("ERROR") + "Can't connect with the discord RPC.")
    time.sleep(0.5)

#
# Variable initialisation
#

print(prefix("INIT") + "Initializing variables...")
os.system("title Initializing variables...")
time.sleep(0.03)
username = os.getlogin()
device = platform.node()
directory = sys.path.__getitem__(0)
threads = os.cpu_count()
version = "1.5"
version_type = "STABLE"
ssh_version = "1.0"
private_ip = socket.gethostbyname(socket.gethostname())
time.sleep(0.03)

#
# Update checker
#

print(prefix("INIT") + "Checking for updates...")
os.system("title Checking for updates...")
try:
    time.sleep(0.03)
    target_version = requests.get("https://pastebin.com/raw/1bdn1xwc").content.decode().rstrip()
    if float(version) != float(target_version):
        update_available = True
    else:
        update_available = False
except:
    print(prefix("WARN") + "Cannot check for updates! No internet connection.")

#
# Multithreading initialisation
#

print(prefix("INIT") + "Initializing multithreading...")
os.system("title Initializing multithreading...")

executor = ThreadPoolExecutor(max_workers=threads)
# Multithreading will be initialized, but is not used in the code yet.
# For more information see https://github.com/NoahOnFyre/FyUTILS.

print(prefix("INIT") + "Initialization phase passed successfully!")
os.system("title Initialization phase passed successfully!")
try:
    time.sleep(0.5)
except KeyboardInterrupt:
    None
print("")

menu()
while True:
    try:
        update_status("Idle")
        try:
            cmd = input(
                Fore.LIGHTBLACK_EX + "╔═══[" + Fore.LIGHTBLUE_EX + username + Fore.LIGHTBLACK_EX + "@" + Fore.WHITE + device + Fore.LIGHTBLACK_EX + "]═══(" + Fore.LIGHTBLUE_EX + "FyUTILS " + Fore.WHITE + version + Fore.LIGHTBLACK_EX + "-" + Fore.WHITE + version_type + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE).lower()
        except KeyboardInterrupt:
            update_status("Shutting down...")
            print(Fore.WHITE + "Shutting down FyUTILS...")
            time.sleep(1)
            rpc.close()
            sys.exit()
        update_status("Running: " + cmd)

        if cmd == "exit" or cmd == "quit":
            update_status("Shutting down...")
            print("")
            print(Fore.WHITE + "Shutting down FyUTILS...")
            time.sleep(1)
            try:
                rpc.close()
            except:
                sys.exit()
            sys.exit()

        elif cmd == "cm" or cmd == "chmac" or cmd == "changemac":
            print("")
            update_status("Changing MAC address...")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Please make sure, FyUTILS is elevated and you're connected to a network.")
            print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
            print("")
            mac_addresses = list()
            macAddRegex = re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")
            transportName = re.compile("({.+})")
            adapterIndex = re.compile("([0-9]+)")
            getmac_output = subprocess.run("getmac", capture_output=True).stdout.decode().split("\n")
            for macAdd in getmac_output:
                macFind = macAddRegex.search(macAdd)
                transportFind = transportName.search(macAdd)
                if macFind is None or transportFind is None:
                    continue
                mac_addresses.append((macFind.group(0), transportFind.group(0)))
            for index, item in enumerate(mac_addresses):
                print(prefix("INFO") + str(index) + " > MAC Address: " + str(item[0]) + " - Transport Name: " + str(item[1]))
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            mac_selection = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Select from index" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
            target_mac = "0A" + input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Enter target MAC address (length: 12)" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE + "0A")
            print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
            activity_start = time.time()
            print("")
            mac_registry_path = r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"
            with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
                controller_key_folders = [("\\000" + str(item) if item < 10 else "\\00" + str(item)) for item in range(0, 21)]
                for key_folder in controller_key_folders:
                    try:
                        with winreg.OpenKey(hkey, mac_registry_path + key_folder, 0, winreg.KEY_ALL_ACCESS) as regkey:
                            try:
                                reg_counter = 0
                                while True:
                                    reg_name, reg_value, reg_type = winreg.EnumValue(regkey, reg_counter)
                                    reg_counter = reg_counter + 1
                                    if reg_name == "NetCfgInstanceId" and reg_value == mac_addresses[int(mac_selection)][1]:
                                        winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, target_mac)
                                        print(prefix("SUCCESS") + "Successfuly changed transport number")
                                        break
                            except WindowsError:
                                pass

                    except:
                        pass
            print(prefix("INFO") + "Your MAC address has been changed! You need to restart your adapter.")
            print(prefix("INFO") + "We're opening control panel for you...")
            time.sleep(1.5)
            os.system("ncpa.cpl")
            print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
            print(prefix("INFO") + "Cleaning up...\n")

        elif cmd == "rl" or cmd == "reload" or cmd == "clear" or cmd == "cls":
            print("")
            update_status("Reloading...")
            print("")
            menu()

        elif cmd == "@" or cmd == "root" or cmd == "admin" or cmd == "elevate":
            print("")
            update_status("Elevating FyUTILS...")
            print("")

        elif cmd == "update":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                to_get_version = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Select Version" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
            except KeyboardInterrupt:
                continue
            update_status("Updating FyUTILS...")
            print(prefix("INFO") + "Getting " + to_get_version + " FyUTILS version...")
            to_get_version_content = requests.get("https://github.com/NoahOnFyre/FyUTILS/releases/download/" + to_get_version + "-STABLE" + "/FyUTILS.py").content
            if to_get_version_content.decode().rstrip() == "Not Found":
                print(prefix("ERROR") + "Either the selected version of FyUTILS does not exist or")
                print(prefix("ERROR") + "there was an error connecting to the GitHub servers.")
                print(prefix("ERROR") + "Code returned from Server: " + to_get_version_content.decode().rstrip())
            else:
                time.sleep(8)
                open(directory + "\\FyUTILS.py", "wb").write(to_get_version_content)
                print(prefix("INFO") + "FyUTILS has been updated to " + to_get_version + " successfully!")
                print(prefix("INFO") + "Please restart FyUTILS by simply running 'rs'")
            print("")

        elif cmd == "rs" or cmd == "restart" or cmd == "new":
            print("")
            update_status("Restarting...")
            print("")
            os.system("start " + directory + "\\FyUTILS.py")
            sys.exit()

        elif cmd == "whois":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                whois_target = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                activity_start = time.time()
                add_command_detail(whois_target)
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
                try:
                    print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
                    print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "FyUTILS WHOIS Service @ " + whois_target)
                    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + Fore.WHITE + "Canceling Action...")
                except:
                    print(e)
                    print("\n" + prefix("ERROR") + Fore.WHITE + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + Fore.LIGHTBLUE_EX + whois_target + Fore.WHITE + "...")
                try:
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except:
                continue

        elif cmd == "flood" or cmd == "dos":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                floodtarget = input(
                    Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                floodport = int(input(
                    Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target port" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                activity_start = time.time()
                add_command_detail(floodtarget + ":" + str(floodport))
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((floodtarget, floodport))
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
                try:
                    for i in range(sys.maxsize):
                        uid = uid_gen(6)
                        sock.send(random.randbytes(10240))
                        print(prefix("INFO") + "Attacking target: " + Fore.LIGHTBLUE_EX + floodtarget + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTBLUE_EX + str(floodport) + Fore.WHITE + "..." + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "Attack: " + Fore.LIGHTBLUE_EX + str(i + 1) + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "UID: " + Fore.LIGHTBLUE_EX + uid, end='\r')

                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + Fore.WHITE + "Canceling Action...")
                except:
                    print(e)
                    print("\n" + prefix("ERROR") + Fore.WHITE + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + Fore.LIGHTBLUE_EX + floodtarget + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTBLUE_EX + str(floodport) + Fore.WHITE + "...")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except:
                continue

        elif cmd == "ssh" or cmd == "ssh":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                update_ssh_status("Logging in...")
                ssh_server = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Host IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                ssh_port = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Host port (default: 22)" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                if ssh_port == "":
                    ssh_port = 22
                else:
                    ssh_port = int(ssh_port)
                ssh_user = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Login (default: " + username + ")" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                if ssh_user == "":
                    ssh_user = username
                else:
                    ssh_user = ssh_user
                ssh_password = getpass.getpass(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Password" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
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
                        print("")
                        ssh_cmd = input(Fore.LIGHTBLACK_EX + "╔═══[" + Fore.LIGHTMAGENTA_EX + ssh_user + Fore.LIGHTBLACK_EX + "@" + Fore.LIGHTMAGENTA_EX + ssh_server + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTMAGENTA_EX + str(ssh_port) + Fore.LIGHTBLACK_EX + "]═══(" + Fore.LIGHTBLUE_EX + "FySSH " + Fore.WHITE + ssh_version + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE)
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
                print(prefix("INFO") + "Disconnecting from " + Fore.LIGHTBLUE_EX + ssh_server + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTBLUE_EX + str(ssh_port) + Fore.WHITE + "...")
                try:
                    ssh.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")

            except:
                continue

        elif cmd == "display":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                display_target = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Enter URL" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                display_timeout = float(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Timeout" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
                activity_start = time.time()
                update_status("Displaying: " + str(display_target))
                try:
                    while True:
                        display_ping = time.time()
                        requests.get(display_target)
                        print(prefix("SUCCESS") + f"Ping request succeed! - Ping: {time.time() - display_ping : 0.2f}ms")
                        time.sleep(display_timeout)
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

        elif cmd == "fetchurl" or cmd == "fetchhtml":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                htmlUrl = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "URL" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                htmlFile = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "File name" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                activity_start = time.time()
                try:
                    open(directory + "\\" + htmlFile + ".html", "x").write(requests.get(htmlUrl).content.decode())
                    print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "HTML source code saved to: '" + htmlFile + ".html'")
                    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except:
                    print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Failed to save source code to: '" + htmlFile + ".html'")
                    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                    print(prefix("WARN") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                print("")
            except:
                print("")

        elif cmd == "usage" or cmd == "performance" or cmd == "perf":
            print("")
            update_status("Getting system variables...")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[CPU] " + Fore.WHITE + "Usage:  " + str(get_usage("CPU")))
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
            print("")

        elif cmd == "vars" or cmd == "variables" or cmd == "var":
            print("")
            update_status("Getting system variables...")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Username:  " + username)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Device:    " + device)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Filepath:  " + directory)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Threads:   " + str(threads))
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + version_type)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + Fore.LIGHTBLUE_EX + "[VAR] " + Fore.WHITE + "Private:   " + private_ip)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
            print("")

        elif cmd == "portscan" or cmd == "scanport":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                scantarget = input(
                    Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                activity_start = time.time()
                add_command_detail(scantarget)
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
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
                        print(prefix("INFO") + "Scanning Port... " + Fore.LIGHTBLUE_EX + str(scanport), end='\r')
                        if result == 0:
                            print(prefix("SUCCESS") + "Port " + Fore.LIGHTBLUE_EX + str(scanport) + Fore.WHITE + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                except:
                    print("\n" + prefix("ERROR") + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix(
                    "INFO") + "Disconnecting from " + Fore.LIGHTBLUE_EX + scantarget + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTBLUE_EX + str(
                    scanport) + Fore.WHITE + "...")
                try:
                    sock.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")
            except:
                continue

        else:
            os.system(cmd)
            print(Fore.WHITE)

        update_status("Idle")
    except KeyboardInterrupt:
        print("")
