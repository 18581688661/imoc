# file = open("D:/jackson/trading_autotest/config/env.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()
import pytest
# with open("D:/jackson/trading_autotest/config/env.yaml", "r",encoding="utf-8") as file:
#     # a = file.read()
#     for i in file.readlines():
#         print(i)
#         print("===========")
#     # a=file.readline()
#     # b=file.readline()
#     # print(a)
#     # print(b)
import requests
import yaml
from common.tools import getprojectpath
from common.tools import sep


# @pytest.fixture(scope="function")
# def gettoken():
#     def _gettoken(user):
#         username, password = GetConf().get_user_password(user)
#         url = GetConf().geturl()
#         # print(url)
#
#         data = {
#             "user": username,
#             "password": password
#         }
#         res = requests.post(url + "/api/user/login", json=data)
#         context = res.json()
#         token = context["data"]["token"]
#         # print(context)
#         # print(type(context))
#         return token
#
#     return _gettoken
    # yield token
    # print(token)


class GetConf:
    def __init__(self):
        with open(getprojectpath() + sep(["config", "env.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_user_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def geturl(self):
        return self.env["url"]

    def get_mysql_conf(self):
        return self.env["mysql"]


if __name__ == '__main__':
    print(GetConf().get_mysql_conf())
