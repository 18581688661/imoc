import requests

from trading_autotest.common.yamlconfig import GetConf, gettoken

url=GetConf().geturl()

token= gettoken()

headers={
    "token": token
}


res = requests.get(url + "/api/router/router_list/",headers=headers)

context = res.json()
print(context)