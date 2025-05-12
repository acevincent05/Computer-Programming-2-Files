import json
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_2198753.json"

response = urllib.request.urlopen(url)
data = response.read().decode()

num_list = []

'''for comment in data['comments']:
    # comment is a dict; get its 'count'
    num_list.append(comment['count'])'''

print(sum(num_list))
