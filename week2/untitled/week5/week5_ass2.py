import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000",
                   headers={'User-Agent': 'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")
shopping = html.select("li._itemSection")

# name, manufacturer, brand, date, like, price

i = 1
for s in shopping:
    try:
        url = s.select_one("p.cont a").attrs["href"]
        shop_e = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_e = BeautifulSoup(shop_e.text, "html.parser")
        shopeach = html_e.select_one("div.summary_info")  # container
        name = shopeach.select_one("div.h_area h2")
        manu = shopeach.select_one("span:nth-of-type(1) em")
        brand = shopeach.select_one("span:nth-of-type(2) em")
        date = shopeach.select_one("span:nth-of-type(3) em")
        like = shopeach.select_one("span em.cnt")
        price = html_e.select_one("div.price_area em")
        print(i, name.text.strip(), manu.text, brand.text, date.text, like.text, price.text)
        print("-" * 50)
        i = i + 1
    except:
        print("error")
        print("shopeach:", shopeach)
        print("name:", name)
        continue


