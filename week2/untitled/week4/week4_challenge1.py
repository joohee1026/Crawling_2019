import requests
from bs4 import BeautifulSoup

f = open("naver_coala.csv",'w')
f.write("기사 제목, 언론사\n")

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text
        title = title.replace(",","")
        source = source.replace(",","")
        print(title, source)
        f.write(title +','+ source + '\n')

f.close()

