import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # url에서 가져온 html을 lxml parser를 통해서 BeautifulSoup 객체로 만듦
cartoons = soup.find_all('a', attrs={'class':'title'}) # 네이버 웹툰 전체 목록 가져오기 class 속성이 title인 모든 a element를 출력
for cartoon in cartoons: 
    print(cartoon.get_text())