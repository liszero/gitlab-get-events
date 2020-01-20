from concurrent.futures import ThreadPoolExecutor

def get_size(p):
    d = p.repository_tree(all=True)
    if d != []:
        numlist = []
        doself(p,numlist,d)
        sizes = 0
        for i in numlist:
            sizes += i
        return str(sizes/1024/1024)[:4] + "MB"
    else:
        return "0.00MB"

def doself(p,numlist,data):
    for i in data:
        if i["type"] == "blob":
            file_info = p.repository_blob(i["id"],all=True)
            nums = file_info["size"]
            numlist.append(nums)
        elif i["type"] == "tree":
            tmplist = p.repository_tree(path=i["path"],all=True)
            with ThreadPoolExecutor(max_workers=50) as t:
                t.submit(doself, p, numlist, tmplist)
    return numlist
