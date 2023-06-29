import os


def getprojectpath():
    projectname = "trading_autotest"
    file_path = os.path.dirname(__file__)
    # print(file_path)
    a = file_path[:file_path.find(projectname) + len(projectname)]
    # print(a)
    return a


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before == True:
        all_path = os.sep + all_path
    if add_sep_after == True:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    # print(getprojectpath())
    print(sep(["config", "env.yaml"], add_sep_before=True))
