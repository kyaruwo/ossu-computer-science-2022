import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input("Enter url: ")
    if url == "quit":
        quit()
    elif len(url) < 1:
        continue

    print("Retrieving", url)
    try:
        url_body = urllib.request.urlopen(url)
        data = url_body.read().decode()
    except:
        print("Invalid url,", url)
        continue
    print("Retrieved", len(data), "characters")
    data_x = ET.fromstring(data)
    break

counts = data_x.findall("comments/comment")
print("comment count:", len(counts))

sum = 0
for i in counts:
    strnum = i.find("count").text
    num = int(strnum)
    sum += num

print("Sum:", sum)

#https://py4e-data.dr-chuck.net/comments_42.xml
#https://py4e-data.dr-chuck.net/comments_1483538.xml