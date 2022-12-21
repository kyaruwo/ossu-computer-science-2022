import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag.get("href", None))

#output "http://www.dr-chuck.com/page2.htm"

#BeautifulSoup Download link
#https://pypi.org/project/beautifulsoup4/
#pip install beautifulsoup4