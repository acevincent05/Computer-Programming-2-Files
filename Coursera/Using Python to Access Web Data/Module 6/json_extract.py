import json
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"

response = urllib.request.urlopen(url)
data = response.read().decode()
parsed_data = json.loads(data)

num_list = []

print(data)

for comment in parsed_data['comments']:
    num_list.append(comment['count'])

'''print(sum(num_list))'''
