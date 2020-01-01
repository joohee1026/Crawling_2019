import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text,"html.parser")
clips = html.select('dl.cds_info')

## 제목, 채널이름, 재생수, 좋아요

print("-"*30)
for i in range(3, len(clips)):
    title = clips[i].select_one('dt.title')
    chn = clips[i].select_one('dd.chn')
    hit = clips[i].select_one('span.hit')
    like = clips[i].select_one('span.like')
    print("<동영상 순위: %d위>" %(i+1))
    print("제목: "+title.text.strip())
    print("채널명: "+chn.text.strip())
    print("재생수: "+hit.text.strip())
    print("좋아요수: "+like.text.strip())
    print("-"*30)

##답안

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    title = cl.select_one("dt.title")
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)