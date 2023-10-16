import os
import json


def create(folder, jsonfile, template):
    jsonfile = str(jsonfile)
    template = dict(template)
    if os.path.isfile(f"{folder}/{jsonfile}") or os.path.isfile(f"{jsonfile}"):
        print("File already exists.")
        return
    elif folder == None:
        f = open(f"{jsonfile}", "x")
        f.write(json.dumps(template))
        f.close()
        print("File created.")
        return
    elif os.path.isdir(folder):
        f = open(f"{folder}/{jsonfile}", "x")
        f.write(json.dumps(template))
        f.close()
        print("File with in Folder created.")
        return
    else:
        os.makedirs(folder)
        f = open(f"{folder}/{jsonfile}", "x")
        f.write(json.dumps(template))
        f.close()
        print("Folder and File created.")
        return


def read(folder, jsonfile):
    jsonfile = str(jsonfile)
    f = open(f"{folder}/{jsonfile}", "r")
    data = json.loads(f.read())
    f.close()
    return data


def edit(folder, jsonfile, update):
    update = dict(update)
    f = open(f"{folder}/{jsonfile}", "rt").read()
    unloadf = json.loads(f)
    unloadf.update(update)
    os.remove(f"{folder}/{jsonfile}")
    f = open(f"{folder}/{jsonfile}", "x")
    f.write(json.dumps(unloadf))
    f.close()
    print("File edited.")
    return
