import gitlab,re
from common.read_file import readfile

class gitlab_con():
    def __init__(self):
        conf = readfile()
        self.url = re.search("^(.*?)/api",conf["path"]).group(1)
        self.token = conf["token"]


    def git_connect(self):
        gl = gitlab.Gitlab(self.url,private_token=self.token)
        return gl