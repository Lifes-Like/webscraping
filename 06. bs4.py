import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # url에서 가져온 html을 lxml parser를 통해서 BeautifulSoup 객체로 만듦
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element를 출력
print(soup.a.attrs) # a element의 속성 정보를 출력
print(soup.a['href']) # a element의 href 속성 '값' 정보를 출력

print(soup.find('a', attrs={'class':'Nbtn_upload'})) # 해당하는 조건에 부합하는 첫번째 element
print(soup.find(attrs={'class':'Nbtn_upload'})) # class='Nbtn_upload'인 element를 찾아줘

rank1 = soup.find('li', attrs={'class':'rank01'})
# next_sibling
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
# previous_sibling
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
# parent
print(rank1.parent)
# find_next_sibling, find_previous_sibling
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())
rank1 = rank2.find_previous_sibling('li')
print(rank1.a.get_text())
# find_next_siblings, find_previous_siblings
print(rank1.find_next_siblings('li'))

# text=''
webtoon = soup.find('a', text='사신소년-2부 5화 검성')
print(webtoon)