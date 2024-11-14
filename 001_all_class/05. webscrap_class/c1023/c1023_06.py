from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import random
from bs4 import BeautifulSoup

url = "http://www.naver.com"
# 크롬 브라우저 열기
browser = webdriver.Chrome()
# 네이버 열기
browser.get(url)
# 네이버 로그인창 태그
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
# 로그인 버튼 클릭
elem.click()
time.sleep(random.randint(2,5))


# 자바스크립트 호출방법
# id = "aaaa"
# pw = "1111"
input_js = 'document.getElementById("id").value = "{id}";\
  document.getElementById("pw").value="{pw}";'.format(id="aaaa",pw="1111")
browser.execute_script(input_js)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME, "btn_login")
elem.click()

time.sleep(100)
# # 아이디 버튼 태그
# elem = browser.find_element(By.CLASS_NAME, "input_id")
# # 아이디 값 입력
# elem.send_keys("aaaa") # 본인 아이디 입력
# time.sleep(random.randint(2,5))
# # 비밀번호 버튼 태그
# elem = browser.find_element(By.CLASS_NAME,"input_pw")
# elem.send_keys("1111") # 본인 패스워드 입력
# time.sleep(random.randint(2,5))
# # 로그인 버튼 클릭
# elem = browser.find_element(By.CLASS_NAME, "btn_login")
# elem.click()
