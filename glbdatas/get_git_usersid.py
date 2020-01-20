from common.gitlab_connect import gitlab_con

class git_username(gitlab_con):
    def get_username(self):
        gl = self.git_connect()
        users_list = gl.users.list(all=True)
        user_name_list = []
        for i in users_list:
            user_name_list.append(i.name)
        return user_name_list