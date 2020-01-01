import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={'User-Agent':'Mozilla/5.0'})

html = BeautifulSoup(raw.text,"html.parser")
movies = html.select("td.overview-top")
#title, score, director, actor

for m in movies:
    title = m.select_one("h4 a")
    url = "https://www.imdb.com/"+title.attrs["href"]

    raw_each = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html_each = BeautifulSoup(raw_each.text, "html.parser")

    posters = html_each.select_one("div.poster img")
    posters_src = posters.attrs["src"]
    urlretrieve(posters_src, "challenge_posters/"+title.text[:3]+".png")