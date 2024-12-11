from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 옵션 설정
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 주소 파일 읽기
with open("도로명주소.txt", "r", encoding="utf8") as f:
    addresses = f.readlines()

# 최신 크롬 드라이버 설치 및 웹 드라이버 생성
browser = webdriver.Chrome(options=options)
browser.minimize_window()


# 파일을 한 번만 열고 데이터를 씀
with open("test123.txt", "w", encoding="utf8") as f:
    cnt = 0
    for i in range(len(addresses)):
        # 각 주소에 대해 URL 생성
        search_keyword = addresses[i].strip()
        print("검색 : ", search_keyword)
        url = f"https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword={search_keyword}&dsgubuntext=&dscity1text=&dscounty1text=&dsemd1text=&dsri1text=&dssan1text=&dsrd_nm1text=&aotYn=N"

        # 웹 페이지 열기
        browser.get(url)
        time.sleep(1.5)  # 잠깐 대기
        soup = BeautifulSoup(browser.page_source, "lxml")
        try : 
            data_element = soup.select_one("#list1 > div.subejct_2 > span.roadNameText")
            data = data_element.text
        except:  
            print("데이터가 없습니다. 다음 검색으로 넘어갑니다.")
            data = "데이터가 없습니다. 다음 검색으로 넘어갑니다."
        finally :  
            print(f"데이터 {cnt+1}/{len(addresses)} : ", data )
            f.write(data + "\n")
        cnt = cnt +1
# 드라이버 사용 후 종료
browser.quit()

print("프로그램 종료")


# Created TensorFlow Lite XNNPACK delegate for CPU : 정보로그 (에러 아님)
