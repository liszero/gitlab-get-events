from common.gitlab_connect import gitlab_con

class git_project(gitlab_con):
    def get_project(self):
        gl = self.git_connect()
        project_list = gl.projects.list(all=True)
        projectlist = []
        for i in project_list:
            tmplist = [i.id,i.name,i.description,i.path_with_namespace]
            projectlist.append(tmplist)
        return projectlist


