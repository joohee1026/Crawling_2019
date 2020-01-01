import requests
from bs4 import BeautifulSoup

# 기사 제목, 기사 요약

for n in range(1, 4):
    raw = requests.get(
        "https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="
        + str(n))
    html = BeautifulSoup(raw.text, "html.parser")
    article = html.select_one("ul.list_info li")

    for at in article:
        title = at.select_one("a.f_link_b").text
        summary = at.select_one("p.f_eb").text
        print("제목:",title)
        print("요약:",summary)
        print(" ")

## 답

for n in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        print(title)
        print(summary)
        # 기사별로 구분을 위해 구분선 삽입
        print("="*50)