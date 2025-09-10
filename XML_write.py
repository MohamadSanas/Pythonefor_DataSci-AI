import xml.etree.cElementTree as ET


employee = ET.Element('employee')

details=ET.SubElement(employee,'details')

first=ET.SubElement(details,'firstName')
second=ET.SubElement(details,'lastName')
third=ET.SubElement(details,'age')

first.text="Mohamad"
second.text="Sanas"
third.text="23"

mydata=ET.ElementTree(employee)

with open("new_sample.xml","wb") as file1:
    mydata.write(file1)
    

    