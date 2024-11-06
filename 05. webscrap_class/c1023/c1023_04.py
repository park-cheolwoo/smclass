# 다음사이트에서 검색창에 '주식 정보'를 입력해서 페이지 이동을 하시오.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

# browser = webdriver.Chrome()
# browser.get("https://www.daum.net")
# elem = browser.find_element(By.ID,"q")
# elem.send_keys("주식 정보")
# time.sleep(3)
# elem.send_keys(Keys.ENTER)

# browser.get("https://www.naver.com")
# elem = browser.find_element(By.CLASS_NAME, "search_input")
# elem.send_keys("주식 정보")
# time.sleep(3)
# elem.send_keys(Keys.ENTER)


# time.sleep(100)


# ---------------------------------------
# import time
# import random

# # a = [0]*100
# # for i in range(100):
# #   a[i] = i

# a = [i for i in range(100)]
# # print(a)

# # print(random.randint(1, 3))

# for i in a:
#     print(i)
#     time.sleep(random.uniform(1, 3))
