import requests

url = 'https://lifes-like.tistory.com/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'} # useragent 넣어주면 실제 크롬에서 접속했을때와 동일한 결과

respond = requests.get(url, headers=headers) # url 접속할때, useragent 값을 넘겨준다.
respond.raise_for_status() # 문제 있으면 에러 내뱉고 프로그램 끝냄
with open('lifes-like.html', 'w', encoding='utf8') as f:
    f.write(respond.text)

