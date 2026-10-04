# craling
import urllib.request

# 1. 웹 페이지 가져오기
URL = "https://music.bugs.co.kr/chart"
response = urllib.request.urlopen(URL)
# print(response.read()
html= response.read()

# 2. 웹 페이지 해석하기
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
titles = soup.select("p.title")
# p: p에서 , . : 클래스가 , title : 타이틀인 데이터 가져와라

lst = []
for title in titles:
    lst.append(title.text.strip("\n"))
for rank, title in enumerate(lst):
    print(rank+1, title)

    