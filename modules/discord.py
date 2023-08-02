from os import path, makedirs
from os.path import exists, splitext, isdir
from os.path import basename
from time import sleep
import modules.config as config
import requests

"""
Script for automatic downloading files from discord servers
made by github.com/ac3ss0r
"""

downloaded = 0

def webhook_send(msg: str, file: str, data: bytes):
    requests.post(config.discord_webhook, data={"content": msg}, files={"file": (file, data)})

"""
discord is pretty goofy and agressive in terms in rate limiting
so this method was made. even if you have perfect connection
sometimes discord API will fail, so this is required 
"""
def safe_get(url: str, headers: dict = {}, params: dict = {}):
    response, sleepTime = None, 1
    while not response or not response.status_code == 200:
        try:
            response = requests.get(url, headers=headers, params=params)
            if not response.status_code == 200:
                print(f"Got {response.status_code}. Retrying in {sleepTime}s...")
                sleep(sleepTime)
                sleepTime += 2
        except Exception as e:
            print(f"Request error: {e}. Retrying...")
            continue
    return response


def get_guilds():
    response = safe_get(
        "https://discord.com/api/v9/users/@me/guilds",
        headers={"Authorization": config.discord_token},
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get guilds: {response.status_code}")


def download_file(url, save_path):
    response = safe_get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to save file: {response.status_code}")


def search_msgs(guild_id: int, max_id: int = None, rate: int = 3):
    response = safe_get(
        f"https://discord.com/api/v9/guilds/{guild_id}/messages/search",
        headers={"Authorization": config.discord_token},
        params={"has": "file", "max_id": max_id},
    )
    return response.json()


def guild_matches(guild):
    if "token" in guild["name"].lower():
        return False
    for server in config.server_filters:
        if server.lower() in guild["name"].lower():
            return True
    return False


def save_all():
    global downloaded
    if not exists("saved"):
        makedirs("saved")
    for guild in get_guilds():
        if not guild_matches(guild):
            continue
        msgs = search_msgs(guild["id"])
        count, total, last_id = 0, msgs["total_results"], msgs["messages"][0][0]["id"]
        print(f"Processing server {guild['name']}")
        while count < (total - 20): # skip the last page 
            msgs = search_msgs(guild["id"], last_id)["messages"]
            for msgl in msgs:
                if not isinstance(msgl, list) or len(msgl) == 0:
                    continue
                for msg in msgl:
                    last_id = msg["id"]
                    for attachment in msg["attachments"]:
                        if splitext(attachment["url"])[1] in config.extensions:
                            try:
                                processed = path.join(
                                    "saved",
                                    basename(attachment["url"])
                                    .replace(".txt", "")
                                    .replace(".lua", "")
                                    + ".lua.txt",
                                )
                                if exists(processed):
                                    print(f"Skipping existing file {processed}...")
                                    continue
                                download_file(attachment["url"], processed)
                                print(f"Saved {attachment['url']}")
                                downloaded += 1
                                sleep(0.5)
                            except:
                                continue
                print(f"Saved files: {downloaded}, Processed messages: {count}/{total}")
                count += len(msgl)
            sleep(0.5)
        print(f"Processed {guild['name']}, total messages: {count}")
