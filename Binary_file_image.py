from PIL import Image
import requests as rq

fileName= "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

def download (url,file_name):
    response=rq.get(url)
    if response.status_code==200:
        with open(file_name,"wb") as nf:
            nf.write(response.content)
            

download (fileName,"./dog.jpg")