import os
import json

def create(folder, jsonfile, template):
    jsonfile = str(jsonfile)
    template = dict(template)

    file_path = os.path.join(folder, jsonfile)
    
    if os.path.exists(file_path):
        print("File already exists.")
        return

    if folder is not None:
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(template, f)
        print("File created.")
        

def read(folder, jsonfile):
    jsonfile = str(jsonfile)
    file_path = os.path.join(folder, jsonfile)
    
    if not os.path.exists(file_path):
        print("File does not exist.")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def edit(folder, jsonfile, update):
    update = dict(update)
    file_path = os.path.join(folder, jsonfile)

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        unloadf = json.load(f)
        unloadf.update(update)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(unloadf, f)
        print("File edited.")
        
