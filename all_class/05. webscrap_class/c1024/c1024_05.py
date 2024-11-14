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

# url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1270, 550)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,800)
# time.sleep(1)
# prev_height = browser.execute_script('return articleListArea.scrollHeight')
# print("화면 높이 : ",prev_height)

# while True:
#     pyautogui.scroll(-prev_height)
#     time.sleep(2)
#     curr_height = browser.execute_script("return articleListArea.scrollHeight")
#     if prev_height == curr_height:break
#     prev_height = curr_height
#     print("높이 : ",prev_height)

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html",'w',encoding='utf8') as f:
#     f.write(soup.prettify())

# input("엔터키 입력완료")

# --------------------------------------------------------------------------------------------
# 매매가격이 낮은 5개, 전세가격이 낮은 5개 출력
# print("-"*50)
# all_height = browser.execute_script('return document.body.scrollHeight')
# print("화면 전체 높이 : ",all_height)

# 파일 데이터 열기
with open('c1024/naver.html','r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')
data = soup.select_one("#articleListArea")
houses = data.select("div.price_line") # 매매, 가격을 1세트로 1개씩 가져옴
# print(len(data))


# 전세 / 매매 리스트 구분
houses1_list = [] # 전세
houses2_list = [] # 매매
no1 = 0
no2 = 0

prices = data.select("span.price")

def price_calc(i):
    t = i.text.strip()
    m = t.split("억")
    f_num = int(m[0])*100000000
    if m[1].strip() != "":
        n_num = int(m[1].strip().replace(",", ""))*10000
    else:
        n_num = 0
    price = f_num + n_num
    return price

for i in houses:
    if i.select_one("span.type").text.strip() == "전세":
        houses1_list.append({"no":no1,"sort": "전세", "price":price_calc(i.select_one('span.price'))})
        no1 +=1
        # cnt1 += 1
    elif i.select_one("span.type").text.strip() == "매매":
        houses2_list.append(
            {"no":no2,"sort": "매매", "price": price_calc(i.select_one('span.price'))}
        )
        no2 += 1


print(len(houses1_list),len(houses2_list))

houses1_list.sort(key=lambda x:x['price'])
houses2_list.sort(key=lambda x:x['price'])

for j in range(80):
    print(f"{j+1} 번째 전세 집 : {houses1_list[j]}")
    print(f"{j+1} 번째 매매 집 : {houses2_list[j]}")

    