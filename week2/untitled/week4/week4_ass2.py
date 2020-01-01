import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['기사제목','기사요약'])

for n in range(1, 4):
    raw = requests.get(
        "https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="
        + str(n))
    html = BeautifulSoup(raw.text, "html.parser")
    article = html.select_one("ul.list_info li")

    for at in article:
        title = at.select_one("a.f_link_b").text
        summary = at.select_one("p.f_eb").text
        title.replace(",", " ")
        summary.replace(",", " ")
        sheet.append([title, summary])

wb.save("daum_articles.xlsx")
