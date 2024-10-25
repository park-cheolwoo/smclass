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

# options = Options()
# # options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")
# options.add_argument(
#     "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
# )

# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# for i in range(1,5+1):
#     url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#     browser.get(url)
#     time.sleep(2)

#     prev_height = browser.execute_script('return document.body.scrollHeight')
#     while True:
#         browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#         time.sleep(1)
#         curr_height = browser.execute_script("return document.body.scrollHeight")
#         if prev_height == curr_height : break
#         prev_height = curr_height
#     soup = BeautifulSoup(browser.page_source,'lxml')
#     with open(f'c1025/naver/n{i:02d}.html','w', encoding='utf8') as f:
#         f.write(soup.prettify())
#     time.sleep(1)
# browser.quit()


# ---------------------------------------------------------------------------------------
with open('c1025/naver/n01.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')
data = soup.select_one(
    "#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx"
)
pros = data.select("div.adProduct_item__1zC9h") + data.select("div.product_item__MDtDF")

# 광고 상품 4개 --------------------------------------------------------------------------
ad_pros = data.select("div.adProduct_item__1zC9h")
f = open('c1025/nshop.csv','a',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
for i in ad_pros:
    try :
        title = i.select_one("div.adProduct_title__amInq > a").text.strip().replace("\n", "").replace("\t", "").replace(",", "")
        price = int(i.select_one("div.adProduct_price_area__yA7Ad > strong > span.price > span > em").text.strip().replace(",",""))
        rating = float(i.select_one("a > span.adProduct_rating__PaMzh").text.strip())
        num = (
            i.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em")
            .text.replace("\n", "")
            .replace("\t", "")
            .replace(",", "")
            .replace(" ","")
            .strip()
        )

        # num(평가수) 태그가 서로 달라 상대위치로 추출
        c_count = int(
            i.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span")
            .text.replace("\n", "")
            .replace("\t", "")
            .replace(",", "")
            .strip()
        )
        writer.writerow([title, price, rating, num, c_count])
    except:
        print("예외처리") # 평점, 평가수, 찜수 없으면 예외처리
    print(title,price,rating,num,c_count)
# -----------------------------------------------------------------------------------------
# 실제 상품 40개
no_pros = data.select("div.product_item__MDtDF")
for j in no_pros:
    try :
        title = j.select_one("div.product_title__Mmw2K > a").text.strip().replace("\n", "").replace("\t", "").replace(",", "")
        price = int(j.select_one("span.price_num__S2p_v>em").text.strip().replace(",", ""))
        rating = (j.select_one("span.product_grade__IzyU3").text.replace("\n", "").replace(" ", "").strip()[2:])           
        num = (
            j.select_one(
                "a.product_etc__LGVaW.linkAnchor._nlog_click._nlog_impression_element > em"
            )
            .text.replace("\n", "")
            .replace("\t", "")
            .replace(",", "")
            .strip()
        )
        # num(평가수) 태그가 서로 달라 상대위치로 추출
        c_count = int(
            j.select_one("div.product_etc_box__ElfVA > span:nth-child(2) > span")
            .text.replace("\t", "")
            .replace("\n", "")
            .replace(",", "")
            .strip()
        )
        writer.writerow([title, price, rating, num, c_count])
    except:
        print("예외처리") # 평점, 평가수, 찜수 없으면 예외처리
    print(title,price,rating,num,c_count)

f.close()
