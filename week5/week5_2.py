import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent': 'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one("dt.tit a")
    print("=" * 50)
    print("제목:", title.text)

    url = "https://movie.naver.com" + title.attrs["href"]
    # print(url)

    # url(상세페이지)에 접속, html 파싱
    raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    poster = html_each.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    urlretrieve(poster_src,"naver_poster/"+title.text[:2]+".png")