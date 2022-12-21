import xml.etree.ElementTree as ET

data = """
    <person>
        <name>kyaruwo</name>
        <phone type="intl">
            +1 234 567 8910
        </phone>
        <email hide="yes"/>
    </person>
    """

tree = ET.fromstring(data)  #create an object/list named tree

print("Name:", tree.find("name").text)  #find the value of the tag
print("Email Attribute:", tree.find("email").get("hide"))  #get the attribute
print("Phone:", tree.find("phone").text.strip())
print("Phone Type:", tree.find("phone").get("type"))  #get the attribute