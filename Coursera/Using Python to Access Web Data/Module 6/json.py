import json
import requests

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"


info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])