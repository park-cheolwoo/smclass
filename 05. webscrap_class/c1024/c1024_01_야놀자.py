from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import random

# url = "https://www.yanolja.com/"
# # 브라우저 열기
# browser = webdriver.Chrome()
# # 브라우저 최대창
# browser.maximize_window()
# # 야놀자 들어가기
# browser.get(url)

# # 검색창 클릭
# time.sleep(3)
# elem = browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div/header/section/a[2]/div/div'
# ).click()
# time.sleep(1)

# # 날짜 선택
# elem = browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button'
# ).click()
# time.sleep(1)
# elem = browser.find_element(
#     By.XPATH,
#     "/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]",
# ).click()
# time.sleep(1)
# elem = browser.find_element(
#     By.XPATH,
#     "/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]",
# ).click()
# time.sleep(1)
# elem = browser.find_element(
#     By.XPATH,
#     "/html/body/div[4]/div/div/section/section[4]/button",
# ).click()
# time.sleep(1)


# # 강릉 입력
# elem = browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input'
# ).send_keys("강릉 호텔")
# time.sleep(1)
# elem = browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input'
# ).send_keys(Keys.ENTER)
# time.sleep(1)


# # 화면의 호텔검색 내용이 뜰 때까지 대기(최대 30초)
# elem = WebDriverWait(browser, 30).until(
#     lambda x: x.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div[2]')
# )

# # 스크롤
# prev_height = browser.execute_script("return document.body.scrollHeight")
# print("높이 : ", prev_height)
# while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1.5)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     print("현재 높이 : ", curr_height)
#     if prev_height == curr_height:
#         break
#     prev_height = curr_height

# print("스크롤 완료")
# input("Enter키를 입력하면 완료됩니다.")
# time.sleep(2)
# browser.quit()

# soup = BeautifulSoup(browser.page_source, "lxml")
# with open("c1024/yanolja1.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# ------------------------------------------------------------

with open("c1024/yanolja1.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

data = soup.select_one(
    "#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1"
)
hotels = data.select("div.PlaceListItemText_container__fUIgA")
hotel_list = []
except_num = 0
fail_num = 0
for idx, hotel in enumerate(hotels):
    try:
        h_tit = hotel.select_one("strong.PlaceListTitle_text__2511B").text.strip()
        h_rating = float(hotel.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
        h_price = int(
          hotel.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",","")
      )
    except:
        h_tit = "에러"
        h_rating = 0.0
        h_price = 0
        except_num += 1
    finally:
        if h_rating >= 4.8 and h_price <= 170000:
            print(f"{idx+1}. ")
            print(f"호텔명 : {h_tit}")
            print(f"평점 : {h_rating}")
            print(f"가격 : {h_price}")
            hotel_list.append({"idx":idx, "name":h_tit, "rating":h_rating, "price":h_price})
        else: 
            print(f"{idx+1}번 예외")
            fail_num +=1
print(" [ 강릉 호텔 ] ")
print("-"*60)
print(f"1. 조건에 맞는 개수 : {len(hotel_list)}")
print(f"2. 조건에 맞지 않는 개수 : {fail_num}")
print(f"3. 에러 개수 : {except_num}")

print(hotel_list)
hotel_list.sort(key = lambda x:x['price'])
print(hotel_list[:5])