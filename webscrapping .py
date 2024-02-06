import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html5")
title=soup.find(class_="title is-4 is-size-5-touch").text.replace("\n","")
print(title)
question=soup.find(class_="single_fatwa__question text-justified").text.replace("\n","")
print(question)
answer=soup.find(class_="content").text.replace("\n","")
print(answer)
questionNO=soup.find(class_="level-item has-separator").text.replace("\n","")
print(questionNO)
data=[[url,question,answer,title,questionNO ]]
data
df=pd.DataFrame(data,columns=["url",'question','answer','title','questionNO'])
df