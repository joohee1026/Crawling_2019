import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['책제목','저자'])

for i in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(i))
    html = BeautifulSoup(raw.text,"html.parser")
    book = html.select("div.lst_thum_wrap li")

    for bk in book:
        title = bk.select_one("a strong").text
        author = bk.select_one("span.writer").text
        sheet.append([title,author])

wb.save("naverbook.xlsx")