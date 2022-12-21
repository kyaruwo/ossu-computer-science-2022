#import url and json library
import urllib.request, urllib.parse, urllib.error
import json

#googlemaps api
service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

#input loop
while True:
    #ask for input
    address = input("Enter location: ")
    if len(address) < 1:
        break

    #parse and encode the address and add it to the service url
    url = service_url + urllib.parse.urlencode({"address": address})

    #print the url
    print("Retrieving", url)
    #request the data and open it
    url_body = urllib.request.urlopen(url)
    #read and decode the requested data
    data = url_body.read().decode()
    #print the length of characters
    print("Retrieved", len(data), "characters")

    #
    try:
        #convert the data into a dictionary
        js = json.loads(data)
    except:
        #
        js = None

    #check if the data receive is a json file, if "status" keywords is in the data, and if the status is "OK"
    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure to Retrieve ====")
        print(data)
        continue

    #The code below will not be executed because I need a google dev account

    #spit out the data
    print(json.dumps(js, indent=4))

    #some json crawling
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)