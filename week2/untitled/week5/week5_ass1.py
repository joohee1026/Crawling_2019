import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import openpyxl

#title, score, genre, director, actor

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['title','score','genre','director','actor'])

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx")
html = BeautifulSoup(raw.text, "html.parser")
movies = html.select("div.desc_boxthumb")

ac = []
di = []

for m in movies:
     try:
        detail = m.select_one("a").attrs["href"]
        raw_e = requests.get(detail)  # detail page raw data
        html_e = BeautifulSoup(raw_e.text, "html.parser")

        title = html_e.select_one("strong.tit_movie").text
        score = html_e.select_one("em.emph_grade").text

        genre = html_e.select("dl.list_movie > dd:nth-of-type(1)")
        director = html_e.select("dl.list_movie > dd:nth-of-type(5) a")
        actor = html_e.select("dl.list_movie > dd:nth-of-type(6) a")

        for g in genre:
            genre = g.text
        di = []
        for d in director:
            director = d.text
            di.append(director)
        ac = []
        for a in actor:
            actor = a.text
            ac.append(actor)

        

        print(title, score, genre, di, ac)
        #sheet.append([title, score, genre, di, ac])

     except:
         print("none")
         continue


wb.save("daummovie.xlsx")


