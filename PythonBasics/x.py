import xml.etree.ElementTree as ET

tree = ET.parse("x.xml")
root = tree.getroot()
# print(root.tag)
for i in root:
    print(i.attrib)
    for j in i:
        print(j.tag + ':' + j.text)
    print('-'*10)
