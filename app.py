from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    #outerData = soup.find_all("div",class_="widget-listing",limit=6)
    #print(outerData)
    TechfinalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        TechfinalNews += '\u2022 '+news+'\n'
    #print(finalNews)
    url = "https://www.businesstoday.in/latest/corporate"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    BuisnessfinalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        BuisnessfinalNews += '\u2022 '+news+'\n'
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
    url = "https://www.businesstoday.in/latest/corporate"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    BuisnessfinalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        BuisnessfinalNews += '\u2022 '+news+'\n'
    url = "https://indianexpress.com/section/sports/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    finalSportNews=""
    #print(soup.find_all("div",class_="second-stories",limit=6))
    news=soup.find_all("h2",class_="title",limit=7)
    for data in news:
        new=(str)(data.a)
        ind=new.index(">")
        new=new[ind+1:len(new)-4]
        finalSportNews+="\u2022"+new+"\n"
    return render_template("index.html",Tech_News=TechfinalNews,Buisness_News=BuisnessfinalNews,Poli_News=finalPoliNews,Sport_News=finalSportNews)