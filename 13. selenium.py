import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() # './chromedriver_mac_arm64/chromedriver.exe'
# 1. 네이버로 이동
browser.get('https://naver.com')
# 2. 로그인 버튼 클릭
elem = browser.find_element(by=By.CLASS_NAME, value='link_login')
elem.click()
# 3. id, pw 입력
browser.find_element(by=By.ID, value='id').send_keys('naver_id')
browser.find_element(by=By.ID, value='pw').send_keys('naver_pw')
# 4. 로그인 버튼 클릭
browser.find_element(by=By.ID, value='log.login').click()
time.sleep(3)
# 5. id를 새로 입력
browser.find_element(by=By.ID, value='id').clear()
browser.find_element(by=By.ID, value='id').send_keys('my_id')
# 6. html 정보 출력
print(browser.page_source)
# 7. 브라우저 종료
browser.quit()
