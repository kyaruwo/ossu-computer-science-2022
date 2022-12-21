import json

data = """
{
    "name" : "kyaruwo",
    "phone" : {
        "type" : "intl",
        "number" : "+1 234 567 8910"
    },
    "email" : {
        "hide" : "yes"
    }
}
"""

info = json.loads(data)  #makes a dictionary
print("Name:", info["name"])
print("Phone:", info["phone"]["number"])
print("Phone Type:", info["phone"]["type"])
print("Hide:", info["email"]["hide"])