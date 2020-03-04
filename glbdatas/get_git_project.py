from common.gitlab_connect import gitlab_con
from glbdatas.get_git_size import get_size
from concurrent.futures import ThreadPoolExecutor
from common.read_file import readfile

class git_project(gitlab_con):
    def get_project(self,sinces,untils):
        date_str = str(sinces) + "~" + str(untils)
        gl = self.git_connect()
        project_list = gl.projects.list(all=True)
        projectlist = []
        for i in project_list:
            comm = i.commits.list(all=True, since=sinces, until=untils)
            tmplist = [i.id,i.name,i.description,i.path_with_namespace,date_str,len(comm)]
            projectlist.append(tmplist)
        return projectlist

    def get_pjinfo(self,npidlist,sinces,untils):
        date_str = str(sinces) + "~" + str(untils)
        gl = self.git_connect()
        npjlist = []
        with ThreadPoolExecutor(max_workers=50) as t:
            for i in npidlist:
                t.submit(npj, gl,i,sinces,untils,date_str,npjlist)
        return npjlist


def npj(gl,i,sinces,untils,date_str,npjlist):
    conf = readfile()
    headers = {
        "PRIVATE-TOKEN": conf["token"]
    }
    m = gl.projects.get(i, all=True)
    comm = m.commits.list(all=True, since=sinces, until=untils)
    sizes = get_size(conf["path"],headers,i)
    mlt = [l.name for l in m.members.list(all=True)]
    mstr = ",".join(mlt)
    tmplists = ["", "", "", "", "", m.id, m.name, m.path_with_namespace,
                m.description, sizes, mstr, m.created_at,
                m.last_activity_at, date_str, len(comm)]
    npjlist.append(tmplists)



if __name__ == "__main__":
    npidlist = [348]
    a = "2020-02-01"
    b = "2020-02-29"
    y = git_project().get_pjinfo(npidlist,a,b)
    print(y[0])