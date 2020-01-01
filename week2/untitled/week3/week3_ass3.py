import requests
from bs4 import BeautifulSoup

for i in range(0,50,10):
    raw = requests.get("https://www.google.com/search?q=%EB%B9%84%EA%B5%90%EC%9A%B0%EC%9C%84+%EC%83%81%EB%8C%80%EC%9A%B0%EC%9C%84&newwindow=1&sxsrf=ACYBGNRP_xDFwEO3yIRvEO37dKexTBSDcQ:1571140701186&ei=XbSlXdz_CpWHoAS19ZfYDg&start="+str(i)+"&sa=N&ved=0ahUKEwicooubm57lAhWVA4gKHbX6BesQ8tMDCI8B&cshid=1571140734459610&biw=904&bih=788",
                       headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    search = html.select("div.g div.rc")

    print(search)