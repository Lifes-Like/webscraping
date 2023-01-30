import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/'
browser.get(url) # url로 이동

# 팝업창 닫기
browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()
time.sleep(1)
# 가는 날 선택 클릭
browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
# 다음 달 6,7일 선택
browser.find_elements(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/td[2]/button/b').click()
browser.find_elements(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/td[3]/button/b').click()
time.sleep(1)

while True:
    pass