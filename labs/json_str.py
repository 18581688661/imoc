import json

data='{"user": "魏巍","password": 123456}'
json_data=json.loads(data)
print(type(json_data))
print(json_data)

str=json.dumps(json_data,ensure_ascii=False)
print(type(str))
print(str)