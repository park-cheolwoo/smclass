from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
# -----------------------------------------------
browser = webdriver.Chrome()
browser.get("https://www.naver.com")

# time.sleep(10) # 브라우저 닫히는 시간 지연

# html 위치 찾기 - requests:select
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.find_element(By.ID,"query") # element 요소 찾기
elem.send_keys("네이버 영화") # 검색창에 "네이버 영화" 입력
elem.send_keys(Keys.ENTER) # 엔터키 입력
elem.click() #클릭 
browser.back() # 페이지 뒤로 이동
browser.forward() # 페이지 앞으로 이동
browser.refresh() # 페이지 새로고침
browser.quit() # 브라우저 종료
browser.switch_to.window(browser.window_handles[1]) # 탭 전환
# time.sleep(3)
# elem.click() 
# time.sleep(5)
