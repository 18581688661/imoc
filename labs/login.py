import requests
from common.yamlconfig import GetConf

user, password = GetConf().get_user_password()
# print(user)
# print(password)

url = GetConf().geturl()
# print(url)

data = {
    "user": user,
    "password": password
}

res = requests.post(url + "/api/user/login", json=data)
context = res.json()
token=context["data"]["token"]
# print(context)
# print(type(context))
print(res.status_code)
print("================")
print(res.ok)
print("================")
print(res.text)
print(type(res.text))
print("================")
print(res.json())
print(type(res.json()))
print("================")
print(res.elapsed.total_seconds()*1000)
print("================")
print(res.headers)
print("================")
print(res.url)
print("===============")

