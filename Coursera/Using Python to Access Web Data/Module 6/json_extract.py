import json
import requests

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"

response = requests.json()
data = response.json()

num_list = []

for num in data:
    num_list.append(data['comments']['count'])
