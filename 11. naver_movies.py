import requests
import re
from bs4 import BeautifulSoup

headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

for year in range(2017,2023):
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={year}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84'
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    images = soup.find_all('div', attrs={'class':'thumb'})

    for idx, image in enumerate(images):
        image_url = image.img['src']
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open(f'movie_{year}_{idx+1}.jpg', 'wb') as f:
            f.write(image_res.content)
            
        if idx >= 4:
            break