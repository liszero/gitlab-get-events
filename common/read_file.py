import os,json

def readfile():
    tmppath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(os.path.dirname(tmppath),r"config/config.json")
    with open(filepath,encoding="utf-8") as f:
        config_data = json.load(f)
    return config_data