import json
import requests
from urllib.parse import urlparse, parse_qs

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"

parsed_url = urlparse(url)

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])