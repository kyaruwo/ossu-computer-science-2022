import xml.etree.ElementTree as ET

data = """
    <stuff>
        <users>
            <user x="0">
                <id>001</id>
                <name>Ninomae Ina'nis</name>
            </user>
            <user x="10">
                <id>012</id>
                <name>kyaruwo</name>
            </user>
        </users>
    </stuff>
    """

stuff_tree = ET.fromstring(data)

users = stuff_tree.findall("users/user")
print("Users count:", len(users))

for i in users:
    print("Name:", i.find("name").text)
    print("userid:", i.find("id").text)
    print("attribute:", i.get("x"))