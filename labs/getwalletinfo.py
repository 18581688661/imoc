import requests

from common.yamlconfig import GetConf, gettoken

url=GetConf().geturl()

token= gettoken()

headers={
    "token": token
}


res = requests.post(url + "/api/wallet/get_wallet_info",headers=headers)

context = res.json()
print(context)