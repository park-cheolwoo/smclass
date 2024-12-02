from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://mkt.naver.com/hiddenarchive?tab=detail&itemId=95"
browser.get(url)
time.sleep(20)
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
with open("sample3.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
time.sleep(2)
