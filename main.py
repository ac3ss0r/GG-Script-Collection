from src import gg, sorter, discord
import subprocess, platform

def java_avaliable():
    try:
        subprocess.run(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

action = input("""
              __  __               ____                          
   __ _  __ _|  \/  | __ _ ___ ___|  _ \ __ _ _ __ ___  ___ _ __ 
  / _` |/ _` | |\/| |/ _` / __/ __| |_) / _` | '__/ __|/ _ \ '__|
 | (_| | (_| | |  | | (_| \__ \__ \  __/ (_| | |  \__ \  __/ |   
  \__, |\__, |_|  |_|\__,_|___/___/_|   \__,_|_|  |___/\___|_|   
  |___/ |___/                                                    
  Mass script parsing/deobfuscation tool 
  v1.0 by Acessor

 Select an action:

 1. Mass download scripts from gameguardian.net
 2. Mass download scripts from discord (token required)
 3. Sort, unpack & format downloaded scripts

> """)

if action == "1":
    request = input("Enter the request > ")
    gg.download_all(request)
elif action == "2":
    discord.save_all()
elif action == "3":
    if not "win" in platform.system().lower():
        print("Lua processing is avaliable only for windows.")
        exit(-1)
    if not java_avaliable():
        print("Java not found. Cannot use unluac.jar")
        exit(-1)
    sorter.process_all()
else:
    print("Unknown option, exiting.")