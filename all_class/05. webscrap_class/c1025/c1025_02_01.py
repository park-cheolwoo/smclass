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

browser = webdriver.Chrome()
browser.maximize_window()
for i in range(1, 6):
    url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
    browser.get(url)
    time.sleep(2)
    # # 화면을 스크롤해서 내리기 반복
    prev_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
        curr_height = browser.execute_script("return document.body.scrollHeight")
        # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
        if prev_height == curr_height:
            break
        # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
        prev_height = curr_height
    print("스크롤 내리기 완료")
    soup = BeautifulSoup(browser.page_source, "lxml")
    with open(f"c1025/navershop{i}.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    time.sleep(2)
