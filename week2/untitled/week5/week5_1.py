import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})

html = BeautifulSoup(raw.text,"html.parser")
movies = html.select("dl.lst_dsc")

#title, score, genre, director, actor

for m in movies:
    title = m.select_one("dt.tit > a").text
    score = m.select_one("div.star_t1 span.num").text
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    genre_all = genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if float(score) < 8.5:
        continue
    if "액션" not in genre_all.text:
        continue

    print("title: ",title)
    print("score: ",score)
    print("genre: ",end='')
    for g in genre:
        print(g.text, end=' ')
    print("")
    print("director: ",end='')
    for d in director:
        print(d.text,end=' ')
    print("")
    print("actor: ",end='')
    for a in actor:
        print(a.text,end=' ')
    print("\n"+"-"*50)
