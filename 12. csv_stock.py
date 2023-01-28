import requests
import csv
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
filename = 'LargeCap1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
title = 'N\t종목명\t현재가\t전일비\t등락률\t액면가\t시가총액\t상장주식수\t외국인비율\t거래량\tPER\tROE'.split('\t') # \t 기준으로 리스트 만들어주기
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1: # 줄바꿈 때문에 존재하는 의미 없는 tr 스킵
            continue
        data = [column.get_text().strip() for column in columns] # td가 가지고 있는 텍스트 정보
        writer.writerow(data)