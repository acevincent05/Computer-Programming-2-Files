import json
import requests

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"

response = requests.get(url)
data = response.json()

num_list = []

for comment in data['comments']:
    # comment is a dict; get its 'count'
    num_list.append(comment['count'])

print(sum(num_list))
