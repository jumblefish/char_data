import datetime
import xml.etree.ElementTree as et

dt = datetime.datetime.today()
print("start", dt)

tree = et.parse(r"C:\Users\Multivac\Documents\ddi\Saved Characters\Rhogar.dnd4e")
root = tree.getroot()
print("ROOT")
print(root, root.tag, root.attrib)
for child in root: 
    print(child.tag, child.attrib)
print("ROOT[0]")
print(root[0], root[0].tag, root[0].attrib)
for child in root[0]: 
    print(child.tag, child.attrib)
print("ROOT[0][5]")
print(root[0][5], root[0][5].tag, root[0][5].attrib)
for child in root[0][5]: 
    print(child.tag, child.attrib)
    
print("ROOT[0][5][4]")
print(root[0][5][4], root[0][5][4].tag, root[0][5][4].attrib)
for child in root[0][5][4]: 
    print(child.tag, child.attrib)