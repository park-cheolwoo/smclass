from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 콘솔로그 출력 안하게
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 제어 메시지 제거
options.add_experimental_option("useAutomationExtension", False)  # 자동화 확장기능 비활성화
options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 탐지 회피
service = Service()

browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()
browser.get('https://wikidocs.net/177133')
