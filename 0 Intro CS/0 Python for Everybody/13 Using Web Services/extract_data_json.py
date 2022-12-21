import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input("Enter url: ")
    if url == "quit":
        quit()
    elif len(url) < 1:
        continue

    print("Retrieving url:", url)
    try:
        url_data = urllib.request.urlopen(url)
        data = url_data.read().decode()
        print("\nThere are", len(data), "characters")
    except:
        print("\n==== Invalid url ====\n", url)
        continue

    print("\n==== Converting data to json ====\n")
    try:
        data_js = json.loads(data)
        print("\n==== data converted ====\n", (json.dumps(data_js, indent=4)))
        print("\nThere are", len(data_js["comments"]), "comments")
    except:
        print("Not a json file")
        continue
    break

sum = 0
for i in data_js["comments"]:
    strnum = i["count"]
    num = int(strnum)
    sum += num

print("\nSum:", sum)
"""
https://py4e-data.dr-chuck.net/comments_42.json
https://py4e-data.dr-chuck.net/comments_1483539.json
"""