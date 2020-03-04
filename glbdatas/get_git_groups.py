from common.gitlab_connect import gitlab_con
from glbdatas.get_git_size import get_size
from concurrent.futures import ThreadPoolExecutor
from common.read_file import readfile

class git_groups(gitlab_con):
    def get_groups(self):
        gl = self.git_connect()
        groupslist = gl.groups.list(all=True,visibility="private")
        galllist = []
        with ThreadPoolExecutor(max_workers=100) as t:
            for i in groupslist:
                t.submit(get_all_list, gl, galllist, i)
        lastlist = []
        for eachlist in galllist:
            tmplist = eachlist[8:] + eachlist[:4] + eachlist[6:8] + eachlist[4:6]
            lastlist.append(tmplist)
        return lastlist

def get_all_list(gl,galllist,i):
    conf = readfile()
    headers = {
        "PRIVATE-TOKEN": conf["token"]
    }
    glist = [i.id, i.name, i.full_path, i.description]
    p = gl.groups.get(i.id, all=True)
    pmlist = []
    for pm in p.members.list(all=True):
        pmlist.append(pm.name)
    pmstr = ",".join(pmlist)
    glist.append(pmstr)
    for j in p.projects.list(all=True,visibility="private"):
        tmplist = [j.id, j.name, j.path_with_namespace, j.description, j.created_at, j.last_activity_at]
        m = gl.projects.get(j.id, all=True)
        sizes = get_size(conf["path"],headers,j.id)
        mlt = [l.name for l in m.members.list(all=True)]
        mstr = ",".join(mlt)
        tmplist.append(sizes)
        tmplist.append(mstr)
        tmplist.extend(glist)
        galllist.append(tmplist)