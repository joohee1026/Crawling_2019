import requests
from bs4 import BeautifulSoup

## 컨테이너, 제목, 저자
import requests
from bs4 import BeautifulSoup

for n in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(n))
    html = BeautifulSoup(raw.text,"html.parser")
    book = html.select("div.lst_thum_wrap li")
    ## list_thum_wrap에 있는 모든 li들을 배열(리스트)로 저장함

    for bk in book:
        title = bk.select_one("a strong").text
        author = bk.select_one("span.writer").text
        price = bk.select_one("p.price2 strong").text
        print("제목:", title)
        print("저자:", author)
        print("가격:", price)
        print("")

## 스페이스바, 화살표는 컨테이너 단위를 나타냄
## .과 #은 클래스 이름을 나타냄