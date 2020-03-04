import requests

def get_size(host,headers,pid):
    urls = "%s/projects/%d?statistics=true" % (host, pid)
    r = requests.get(urls, headers=headers)
    sizes = r.json()["statistics"]["storage_size"]
    return "{:.2f}MB".format(sizes/1024/1024)
