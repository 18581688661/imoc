from common.yamlconfig import GetConf
import requests


def login(user):
    username, password = GetConf().get_user_password(user)
    url = GetConf().geturl()
    # print(url)

    data = {
        "user": username,
        "password": password
    }
    res = requests.post(url + "/api/user/login", json=data)
    return res
