import requests
from bs4 import BeautifulSoup

# 반복1: 기사번호를 변경시키면서 데이터 수집을 반복하기
# 1 ~ 100까지 10단위로 반복(1, 11, ..., 91)
for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    # 반복2: 기사에 대해서 반복하면 세부 정보 수집하기
    # 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        print(title, source)