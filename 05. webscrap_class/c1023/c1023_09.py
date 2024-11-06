from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import random
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 07번 매크로 다시 입력해보기

url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 첫번째 화면
time.sleep(2)

# 1. 출발지(김포)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]'
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input'
).send_keys("김포")
time.sleep(1)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a'
).click()
time.sleep(1)

# 2. 목적지(제주)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]'
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input'
).send_keys("제주")
time.sleep(1)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a'
).click()
time.sleep(1)

# 3. 가는 날(11/6)
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]'
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button',
).click()
time.sleep(1)

# 4. 오는 날(11/9)

elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button',
).click()
time.sleep(1)

# 5. 인원 추가(성인 2명)
elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button',
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]',
).click()
time.sleep(1)

# 6. 항공권 검색
elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]',
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH,
    '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]',
).click()
time.sleep(1)

# 7. 검색 후 대기
# time.sleep(10)

# 에러 발생
elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 8. 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)  # 다른정보가 추가될때까지 대기
    # 높이 확인 - 2000
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height # 무한루프 탈출?

# 9. 파일 저장
soup = BeautifulSoup(browser.page_source,'lxml')
with open("c1023/flight1.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())
print("저장 완료")
browser.quit()

# --------------------------------------------------------------------------------------


# # 10. 파일 읽은 후 조건 검색
# with open("c1023/flight1.html",'r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')
# data = soup.select_one("div.domestic_Flight__8bR_b")

# time.sleep(100)
