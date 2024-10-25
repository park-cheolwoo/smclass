from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyautogui
import time
import random
import requests
import csv
# 제목 금액 평점 평가수 찜 정보를 1~5페이지까지 가져와서
# 평점 4.8 이상, 평가수 1000명 이상인 상품을 csv파일로 저장하고 출력
# for i in range(5):
options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument(
    "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.naver.com"
browser.get(url)
time.sleep(5)
elem = browser.find_element(By.ID,"query").send_keys("네이버 쇼핑")
time.sleep(1)
elem = browser.find_element(By.ID, "query").send_keys(Keys.ENTER)
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME, "link_name").click()
time.sleep(3)
browser.switch_to.window(browser.window_handles[1])
time.sleep(5)
elem = browser.find_element(
    By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div'
).click()
time.sleep(1)
elem = browser.find_element(
    By.XPATH,
    '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input',
).send_keys("무선 마우스")
time.sleep(1)
elem = browser.find_element(
    By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input'
).send_keys(Keys.ENTER)
time.sleep(2)
input("엔터키 입력")


