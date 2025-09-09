import pandas as pd
import requests as rq
import json 
from bs4 import BeautifulSoup

url="https://books.toscrape.com/catalogue/page-1.html"
response=rq.get(url)

soup = BeautifulSoup(response.text,"html.parser")

books=[]

for book in soup.select("article.product_pod"):
    title=book.h3.a["title"]
    price=book.select_one(".price_color").text
    books.append({"Title":title,"Price":price})
    
df=pd.DataFrame(books)

print(df)



