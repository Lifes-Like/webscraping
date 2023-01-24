import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=799793'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs={'class':'title'})
title = cartoons[0].a.get_text()
link = cartoons[0].a['href']
print(title, f'https://comic.naver.com{link}')


# 만화제목 + 링크 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = cartoon.a['href']
    print(title, f'https://comic.naver.com{link}')

# 평점구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)
print(f'전체점수 : {total_rates}')
print(f'평균점수 : {total_rates / len(cartoons)}')