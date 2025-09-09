
import seaborn
import lxml
import openpyxl
import pandas as pd
import requests

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"


response = requests.get(filename)
with open("addresses.csv", "wb") as f:
    f.write(response.content)

# Read into pandas
df = pd.read_csv("addresses.csv", header=None)

print(df)

print("adding coloumn")
df2=df
df2.columns=['First Name','Last Name','Location','City','State','Area code']
print(df2)

print("selectin a single coloumn")
print(df2["First Name"])

print("select the specific row")
print(df2.loc[2]) #start from 0 to n-1

print("specific row of specific column")
print(df2.loc[[0,2],"Last Name"])

print(df2.iloc[[0,1,2],3])

