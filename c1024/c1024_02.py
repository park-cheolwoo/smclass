from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random
import requests

# 노트북 검색 사이트 1,2,3 페이지 중에서
# 만족도 95% 이상이면서 평가수가 100 이상이면서 금액 1500000(150만) 이하 검색하시오

# 페이지 검색 후 저장하기
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)


for i in range(3):
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
    browser.get(url)
    # # 1) 페이지 로딩
    elem = WebDriverWait(browser, 10).until(
        lambda x: x.find_element(By.XPATH, '//*[@id="region__content-body"]')
    )
    time.sleep(random.randint(2,3))
    # 2) 저장
    with open(f"c1024/gmarket/g{i+1:02d}.html", "w", encoding="utf8") as f:
        soup = BeautifulSoup(browser.page_source, "lxml")
        f.write(soup.prettify())
    browser.get_screenshot_as_file(f"c1024/gmarket/g{i+1:02d}.png")
    print(f"{i+1} 번 완료")
    browser.quit()

for j in range(3):
    with open(f"c1024/gmarket/g{j+1}.html",'r',encoding='utf8') as f:
        