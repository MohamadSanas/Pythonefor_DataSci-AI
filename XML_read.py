import xml.etree.ElementTree as et
import requests as rq
import pandas as pd


filename="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

response=rq.get(filename)

with open("write_readed_xml.xml","wb") as nf:
    if response.status_code==200:
        nf.write(response.content)

#parse the xml file

tree=et.parse("write_readed_xml.xml")

root=tree.getroot()

columns = ["firstName","LastName","title","division","building","room"]

dataFrame=pd.DataFrame(columns=columns)

for node in root:
    firstName=node.find("firstname").text
    lastName=node.find("lastname").text
    title = node.find("title").text
    division = node.find("division").text
    building = node.find("building").text
    room = node.find("room").text


    row_df=pd.DataFrame([[firstName, lastName, title, division, building, room]],columns=columns)

    dataFrame=pd.concat([dataFrame, row_df],ignore_index=True)


print(dataFrame)

dataFrame.to_csv("new_xml.csv",index=False)