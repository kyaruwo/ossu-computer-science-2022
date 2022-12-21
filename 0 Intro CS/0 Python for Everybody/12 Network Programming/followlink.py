import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input("Enter count: "))
position = int(input("Enter position: "))

link = None
rep = 0
while rep < count:
    url = link
    if url == None:
        url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    tags = soup('a')
    for tag in tags:
        if i < position:
            link = tag.get('href', None)
            print("Retrieving:", link)
        i += 1
    rep += 1

link_split = link.split("_")
name = link_split[2].split(".")
name = name[0]
print("\nLast Name:", name)
"""
http://py4e-data.dr-chuck.net/known_by_Fikret.html
http://py4e-data.dr-chuck.net/known_by_Viki.html
"""