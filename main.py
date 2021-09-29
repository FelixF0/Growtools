# GrowTools a GTPS multitools.
# Made by Kla1das

################################################
# $ If you have any problem, DM me on Discord! #
# $ My Github : https://github.com/kla1das.    #
################################################

# Module
import os
from os import system
import requests
import time
from time import sleep

# Banner
banner = """
           _____                 _____           _     
          |  __ \               |_   _|         | |    
          | |  \/_ __ _____      _| | ___   ___ | |___ 
          | | __| '__/ _ \ \ /\ / / |/ _ \ / _ \| / __|
          | |_\ \ | | (_) \ V  V /| | (_) | (_) | \__ |
           \____/_|  \___/ \_/\_/ \_/\___/ \___/|_|___/
                                             
          =============================================
          [INFO] A multipurpose Growtopia Server Tools
          [CREATOR] Developed and created by : kla1das
          [DISCORD] My Discord : kla1das#3440
          =============================================
          [READER]: For reading server data
          [HOST]: To make a growtopia server host
          [IPFINDER]: To find ip from a encrypted host
          [SERVERDATA]: To create a server data
          =============================================
"""

# Functions
print(banner)
choice = input("[CHOICE] Select : ")

# Definition
def reader():
    print(banner)
    ip = input('[INPUT] IP Address : ')
    print("[LOGS] Reading into the server data, please wait...")

    post = requests.post(f'http://{ip}/growtopia/server_data.php')
    sleep(5)
    print(post.text)
    print("\n[LOGS] Readed!")
    sleep(100)

def host():
    print(banner)
    iphost = input("[INPUT] Server IP : ")
    namehost = input("[INPUT] Filename : ")
    ext = input(f"[INPUT] File extension (.txt) : ")

    fpc = open(f"{namehost}.{ext}", "w")

    fpc.write(iphost + ' growtopia1.com\n' + iphost + ' growtopia2.com')
    fpc.close()
    print(f'[SUCCESS] Host has been created with filename : {namehost}.{ext}\n')
    time.sleep(100)

def serverdata():
    print(banner)
    serverip = input("[INPUT] Server IP : ")
    sport = input("[INPUT] Server Port : ")
    mainmsg = input("[INPUT] Maintenance message : ")
    print("\n")
    sd = open("server_data.php", "w")
    sd.write(
    f"server|{serverip}\nport|{sport}\ntype|1\n#maint|{mainmsg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001"
    )
    sd.close()
    print("[SUCCESS] Server database has been created.")
    time.sleep(100)

def ipfinder():
    print(banner)
    text = input("[INPUT] Host name : ")
    ok = open(text, "r").readlines()

    for i in ok:
        if i[0].startswith("#"):
            pass
        elif not i[0].isdigit():
            pass
        else:
            print(f"[SUCCESS] Decrypted IP : {i}")
            sleep(100)

# Main Functions
if choice == "host":
    os.system("cls")
    host()
elif choice == "ipfinder":
    os.system("cls")
    ipfinder()
elif choice == "serverdata":
    os.system("cls")
    serverdata()
elif choice == "reader":
    os.system("cls")
    reader()
