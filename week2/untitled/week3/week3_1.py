import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
print(raw)
## 변수(기본) - 응답성공여부 // <response[200]>
## 변수.text - 접속한 URL의 소스코드(HTML) // <head></head>...
## 변수.elapsed - 페이지가 응답하는데 걸리는 시간 // 0:00:00.04452

html = BeautifulSoup(raw.text,"html.parser")
## html소스코드에서 태그를 기준으로 파싱

clips =  html.select('div.inner')
## print(clips[0])
## 변수 = BS.select("html선택자")
## BS: html.parser로 파싱된 소스
## 네이버TV 1~3위 영상 clips[0],[1],[2]에 정보가 차례대로 저장됨

title = clips[0].select_one('dt.title')
title = title.text
print(title)
## 제목은 하나밖에 없으므로 첫번째 소스만 선택해주는 select_one함수 사용
## title에서 html 코드를 제외한 제목만 선택하는 .text함수 사용

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text,"html.parser")
clips = html.select("div.inner")

title = clips[0].select_one('dt.title')
chn = clips[0].select_one('dd.chn')
hit = clips[0].select_one('span.hit')
like = clips[0].select_one('span.like')

print(title.text.strip())
print(chn.text.strip())
print(hit.text.strip())
print(like.text.strip())

