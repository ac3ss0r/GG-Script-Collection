from os import listdir, remove, makedirs
from os.path import join, exists, isdir
from shutil import copy2
from subprocess import run, DEVNULL, STDOUT
import modules.config as config
import re

# data contains any of list
def has_any(data : bytes, sigs : list):
    for sig in sigs:
        if sig.encode() in data:
            return True
    return False

# raw bytes (non-utf8) detection
def is_raw(data: bytes):
    try:
        data.decode("utf-8")
    except:
        return True

# parse version using regexp
def get_ver(file : str):
    match = re.search(config.sorting_pattern, file) # check filename
    if match:
        return match.group(0)
    else:
        with open(file, "rb") as file:
            data = file.read()
            if not is_raw(data):
                data = data.decode() # check file data
                match = re.search(config.sorting_pattern, data)
                if match:
                    return match.group(0)
    return None

# detect lua obfuscation
def get_obf(data : bytes):
    if is_raw(data):
        return "Lua Compiler"
    elif has_any(data, ["LuaObfuscator.com", "LOL!"]):
        return "LuaObfuscator.com"
    elif has_any(data, ["XOR encrypt"]):
        return "Simple XOR encrypt"
    lines = data.count("\n".encode())
    if has_any(data, ["load("]) or \
       lines > 0 and len(data) / lines > 250:
        return "Unknown"
    
# check if file is lua source by sigs
def is_lua(data : bytes):
    return has_any(data, ["tonumber", "gg.", "LuaR", "TYPE_BYTE", "table.", "loadstring"])

# detect ban scripts by sigs
def get_safety(data : bytes):
    index, markers = 0, ["🟢 (Should be fine)","🟡 (Is obfuscated)","🔴 (Most likely a ban script)"]
    if has_any(data, ["'280'", "'999'"]) or\
       "gg.TYPE_FLOAT".encode() in data and "gg.REGION_ANONYMOUS".encode() in data\
       and "gg.editAll".encode() in data:
        return markers[2] # is a ban script
    if get_obf(data):
        index+=1
    return markers[index]

# script formatting/sorting. TODO: implement deobfuscation
def process_dir(path: str):
    for filename in listdir(path):
        filepath = join(path, filename)
        if isdir(filepath) or not ".lua" in filename:
            continue
        with open(filepath, "rb") as file:
            data = file.read()
            if not is_lua(data):
                file.close()
                print(f"{filename} is not a lua source file, deleting...")
                remove(filepath)
                continue
            if not is_raw(data):
                run(f"stylua . \"{filepath}\"", stdout=DEVNULL, stderr=STDOUT)
            version, obf, safety = get_ver(filepath), get_obf(data), get_safety(data)
            print(f"{filename} processed. Version: {version}, Obfuscator: {obf}")

def process_all():
    for directory in listdir("saved"):
        dirpath = join("saved", directory)
        if not isdir(dirpath):
            continue
        process_dir(dirpath)