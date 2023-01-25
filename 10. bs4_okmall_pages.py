import requests
import re
from bs4 import BeautifulSoup

headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            ,'Accept-Language':'ko-KR,ko;q=0.3,en-US;q=0.5,en;q=0.3'
        }

for page in range(1, 6):
    print(f'페이지 : {page}')
    url = f'https://www.okmall.com/products/list?search_keyword=%EB%82%98%EC%9D%B4%ED%82%A4&detail_search_keyword=&page={page}'
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all('div', attrs={'class':re.compile('^item_box')})
    for item in items:
        # 여성제품은 제외
        wm_product = item.find('em', attrs={'class':'ic_woman'})
        if wm_product:
            # print('<<< 여 성 제 품 >>>')
            continue

        # 상품명
        name = item.find('p', attrs={'class':'item_title'}).get_text()
        if '골프' in name:
            # print('<<< 골 프 상 품 제 외 >>>')
            continue

        # 가격
        price = item.find('span', attrs={'class':'okmall_price'}).get_text()

        # 평점 (4.5 이상만)
        rate = item.find('span', attrs={'class':'num_score'})
        if rate:
            rate = rate.get_text()
        else:
            rate = '평점 없음'
            # print('<<< 평 점 없 음 >>>')
            continue

        # 찜 갯수 (500개 이상)
        zzim = item.find('span', attrs={'class':'num_zzim'})
        if zzim:
            zzim = zzim.get_text()
        else:
            zzim = 0
            # print('<<< 찜 없 음 >>>')
            continue
        # 링크
        link = item.find('a').attrs['href']

        if float(rate) >= 4.5 and int(zzim) >= 500:
            print(f'''
                    제 품 명 : {name}
                    가 격 : {price}원
                    평 점 : {rate}점
                     찜  : {zzim}개
                    링 크 : https://www.okmall.com{link}
----------------------------------------------------------------------------------------------------------
                    '''
                    )
