from bs4 import BeautifulSoup
import requests

url = "https://indianexpress.com/section/political-pulse/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
finalPoliNews=""
#print(soup.find_all("div",class_="second-stories",limit=6))

news=soup.find_all("h2",class_="title",limit=7)
for data in news:
    new=(str)(data.a)
    ind=new.index(">")
    new=new[ind+1:len(new)-4]
    finalPoliNews+="\u2022"+new+"\n"
print(finalPoliNews)