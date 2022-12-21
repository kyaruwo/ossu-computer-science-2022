import json

data = """
[
    {
        "id" : "001",
        "x" : "0",
        "name" : "inya"
    },
    {
        "id" : "002",
        "x" : "1",
        "name" : "kyaruwo"
    }
]
"""

info = json.loads(data)

print("User count:", len(info))

for i in info:
    print("Name:", i["name"])
    print("userid:", i["id"])
    print("Attribute:", i["x"])