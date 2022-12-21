import urllib.request, urllib.parse, urllib.error
import json

while True:
    service_url = "https://py4e-data.dr-chuck.net/json?"
    location = input("Enter location: ")

    url = service_url + urllib.parse.urlencode({
        "address": location,
        "key": "42"
    })
    """ line 8 to line 11 can also be written as line 13 to 16
    parms = dict()
    parms["address"] = location
    parms["key"] = 42
    url = serviceurl + urllib.parse.urlencode(parms)
    """

    print("Retrieving", url)
    try:
        url_data = urllib.request.urlopen(url)
        data = url_data.read().decode()
        print("Retrieved", len(data), "characters")
        #print(data)
    except:
        print("\nLocation does not exist!\n")
        continue

    try:
        data_x = json.loads(data)
        print(json.dumps(data_x, indent=4))
        break
    except:
        print("Not a json file")
        continue

#note to self do not forget to look for sub 0
place_id = data_x["results"][0]["place_id"]
print("Place id", place_id)

#South Federal University
#University of Ilorin Kwara State