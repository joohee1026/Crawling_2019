import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={'User-Agent':'Mozilla/5.0'})

html = BeautifulSoup(raw.text,"html.parser")
movies = html.select("td.overview-top")
#title, score, director, actor

for m in movies:
    title = m.select_one("h4 a")
    director = m.select("div.txt-block span a")
    actor = m.select("td.overview-top div:nth-of-type(4) a")
    genre_all = m.select("p.cert-runtime-genre")
    for g in genre_all:
        genre_all = g.text
    if "Action" not in genre_all:
        continue
    print(title.text)
    print("director: ",end="")
    for d in director:
        director = d.text
        print(director)
    print("actor: ",end="")
    for a in actor:
        actor = a.text
        print(actor)
    print("-"*50)

