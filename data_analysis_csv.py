import pandas as pd
import requests as rq
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the dataset
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# Function to download CSV
def download(url, filename):
    response = rq.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as nf:
            nf.write(response.content)

# Download the file
download(file_url, "diabetes.csv")

# Load CSV into DataFrame
df = pd.read_csv("diabetes.csv")

# Check shape and type
dimension = df.shape
print("Type of dimension:", type(dimension))
print("DataFrame shape (rows, columns):", dimension)

# Check for missing data
missing_data = df.isnull()
print("\nMissing data in first row:\n", missing_data.head(1))

# Count missing values per column
print("\nMissing values per column:")
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Check data types
print("Data types of each column:\n", df.dtypes)

# Pie chart for Outcome column
labels = 'Not Diabetic', 'Diabetic'
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.title("Diabetes Outcome Distribution")
plt.legend()
plt.show()
