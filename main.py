from concurrent.futures import ThreadPoolExecutor
from glbdatas.get_git_events import get_events
from glbdatas.get_git_project import git_project
from glbdatas.get_git_usersid import git_username
from glbdatas.get_git_groups import git_groups
from common.write_excel import wexcel
import argparse,os,traceback

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--after", "-a", action="store", help="请输入开始时间,例：2006-01-02")
        parser.add_argument("--before", "-b", action="store", help="请输入结束时间,例：2006-01-02")
        args = parser.parse_args()
        if args.after != None and args.before != None:
            curpath = os.path.dirname(os.path.realpath(__file__))
            after = args.after
            before = args.before
            exname = os.path.join(curpath,(after+"_"+before+".xlsx"))
            project_list = git_project().get_project()
            events_list = []
            with ThreadPoolExecutor(max_workers=100) as t:
                for i in project_list:
                    t.submit(get_events,events_list,i,after,before)
            usernamelist = git_username().get_username()
            tmpgitlist = []
            for j in events_list:
                tmpgitlist.append(j[3])
            sitegitlist = list(set(tmpgitlist))
            for i in usernamelist:
                if i not in sitegitlist:
                    tmplist = ["","","",i,"","","","",""]
                    events_list.append(tmplist)
            sheet1 = "gitevents"
            tabname1 = ["项目", "项目描述", "项目路径", "项目操作人", "操作动作",
                        "操作库类型", "操作库", "操作描述", "操作时间"]
            wexcel(exname,sheet1,tabname1,events_list)

            groupsname = os.path.join(curpath,"groups_info.xlsx")
            sheet2 = "gitgroups"
            tabname2 = [ "项目组Id", "项目组名称","项目组路径","项目组描述","项目组成员",
                         "项目Id", "项目名称", "项目路径", "项目描述","项目大小",
                         "项目内成员", "项目创建时间", "项目最后更新时间"]
            groups_list = git_groups().get_groups()
            wexcel(groupsname,sheet2,tabname2,groups_list)

        else:
            parser.print_help()

    except:
        error = traceback.format_exc()
        print(error)

if __name__ == "__main__":
    main()