import numpy as np
import pandas as pd
import os

from tabulate import tabulate


def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables=pd.read_html(URL)
df = tables[3]

df.columns=range(df.shape[1])

df=df[[0,2]]

df=df.iloc[1:11,:]

df.columns=['Country','GDP (Million USD)']


print(tabulate(df, headers='keys', tablefmt='pretty'))

df['GDP (Million USD)']=df['GDP (Million USD)'].astype(int)

df[['GDP (Million USD)']]=df[['GDP (Million USD)']]/1000
df[['GDP (Million USD)']]=np.round(df[['GDP (Million USD)']],2)
df=df.rename(columns={'GDP (Million USD)' : 'GDP (Billion USD)'})


print(df)

df.to_csv(r'C:\Users\sanas\Desktop\my learn\AI\Python for data science and AI devolopment\Project\bigest_Eonomics_contry.csv', index=False)
#to found the working directory
print(os.getcwd())
