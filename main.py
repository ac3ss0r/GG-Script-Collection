from modules import gg, sorter, discord

print("""              __  __    _    ____ ____  ____                          
   __ _  __ _|  \/  |  / \  / ___/ ___||  _ \ __ _ _ __ ___  ___ _ __ 
  / _` |/ _` | |\/| | / _ \ \___ \___ \| |_) / _` | '__/ __|/ _ \ '__|
 | (_| | (_| | |  | |/ ___ \ ___) |__) |  __/ (_| | |  \__ \  __/ |   
  \__, |\__, |_|  |_/_/   \_\____/____/|_|   \__,_|_|  |___/\___|_|   
  |___/ |___/      
  Mass script parsing/deobfuscation tool 
  v1.0 by Acessor
""")

action = input("""Select an action:

1. Mass download scripts from gameguardian.net
2. Mass download scripts from discord (token required)
3. Sort & format downloaded scripts

> """)

if action == "1":
    gg.download_all(input("Enter the request > "))
elif action == "2":
    discord.save_all()
elif action == "3":
    sorter.process_all()
else:
    print("Unknown option, exiting.")