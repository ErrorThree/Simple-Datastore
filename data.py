import os
import json


def create(folder, jsonfile, template):
    jsonfile = str(jsonfile)
    template = dict(template)

    if os.path.isfile(f"{folder}/{jsonfile}") or os.path.isfile(jsonfile):
        print("File already exists.")
        return
    elif folder is None:
        f = open(jsonfile, "x")
        f.write(json.dumps(template))
        f.close()
        print("File created.")
        return
    elif os.path.isdir(folder):
        f = open(os.path.join(folder, jsonfile), "x")
        f.write(json.dumps(template))
        f.close()
        print("File within folder created.")
        return
    else:
        os.makedirs(folder)
        f = open(os.path.join(folder, jsonfile), "x")
        f.write(json.dumps(template))
        f.close()
        print("Folder and file created.")
        return


def read(folder, jsonfile):
    jsonfile = str(jsonfile)
    with open(os.path.join(folder, jsonfile), "r") as f:
        data = json.load(f)
    return data


def edit(folder, jsonfile, update):
    update = dict(update)
    file_path = os.path.join(folder, jsonfile)
    with open(file_path, "rt") as f:
        unloadf = json.load(f)
        unloadf.update(update)
    os.remove(file_path)
    with open(file_path, "x") as f:
        f.write(json.dumps(unloadf))
    print("File edited.")
    return
