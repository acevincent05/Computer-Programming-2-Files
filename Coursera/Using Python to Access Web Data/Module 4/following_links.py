# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))


names = []

while count > 0:
    print ("retrieving: {0}".format(url))
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1


print (names[-1])