import pandas as pd
import requests

# URL of the Excel file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

# Download the file
response = requests.get(url)
with open("file_example_XLSX_10.xlsx", "wb") as f:
    f.write(response.content)

# Read the Excel file into a DataFrame
df = pd.read_excel("file_example_XLSX_10.xlsx")


