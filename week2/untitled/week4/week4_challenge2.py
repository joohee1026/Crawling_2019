import requests
from bs4 import BeautifulSoup
import openpyxl
MAX = 100

try:
    ##파일이 없으면 에러나기 때문에 try except처리 해줌
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
    print("불러오기 성공!")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["검색어","기사제목","언론사"])
    print("새 파일 생성")

keyword = input("수집 키워드: ")

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text
        title = title.replace(",","")
        source = source.replace(",","")
        sheet.append([keyword,title,source])

wb.save("navernews.xlsx")

