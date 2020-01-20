import requests
from common.read_file import readfile

def get_events(events_list,prolist,after,before):
    conf = readfile()
    headers = {
        "PRIVATE-TOKEN":conf["token"]
    }
    for i in range(1,31):
        urls = "%s/projects/%s/events?after=%s&before=%s&per_page=100&page=%s" % (conf["path"],prolist[0],after,before,i)
        r = requests.get(url=urls,headers=headers)
        for j in r.json():
            tmplist = []
            tmplist.append(prolist[1])
            tmplist.append(prolist[2])
            tmplist.append(prolist[3])
            tmplist.append(j["author"]["name"])
            if "push_data" in j.keys():
                tmplist.append(j["action_name"])
                tmplist.append(j["push_data"]["ref_type"])
                tmplist.append(j["push_data"]["ref"])
                tmplist.append(j["push_data"]["commit_title"])
            else:
                tmplist.append(j["action_name"])
                tmplist.append("")
                tmplist.append("")
                tmplist.append("")
            times = j["created_at"]
            times = times.replace("T"," ")
            times = times.replace("Z","")
            tmplist.append(times[:10])
            events_list.append(tmplist)
