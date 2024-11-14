from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd

# # 웹 스크래핑
# for i in range(4):
#     browser = webdriver.Chrome()
#     url = f"https://search.daum.net/search?w=tot&q={i+2020}년영화순위&DA=MOR&rtmaxcoll=MOR"
#     browser.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(browser.page_source, "lxml")
#     with open(f"movie{i+2020}.html", "w", encoding="utf8") as f:
#         f.write(soup.prettify())
#     browser.close()
# print("저장완료")

# # 데이터 추출
# for i in range(4):
#     with open(f"movie{i+2020}.html", "r", encoding="utf8") as f:
#         soup = BeautifulSoup(f, "lxml")
#         data = soup.select_one(
#             "#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul"
#         )
#         movies = data.select("li")
#     with open(f"movie{i+2020}.csv", "a", encoding="utf-8-sig", newline="") as ff:
#         writer = csv.writer(ff)
#         writer.writerow(["이미지링크", "제목", "관객수", "날짜"])
#         for movie in movies:
#             img = movie.select_one("a.thumb_bf img")["src"]
#             # print(img)
#             title = movie.select_one("strong.tit-g").text.strip()
#             # print(title)
#             num = movie.select_one("p.conts-desc").text.strip().replace(",", "")[3:-2]
#             # print(num)
#             date = movie.select_one("span.conts-subdesc").text.strip()
#             # print(date)
#             writer.writerow([img, title, num, date])

# # 데이터 불러오기
# df1 = pd.read_csv("movie2020.csv", encoding="utf-8-sig")
# df2 = pd.read_csv("movie2021.csv", encoding="utf-8-sig")
# df3 = pd.read_csv("movie2022.csv", encoding="utf-8-sig")
# df4 = pd.read_csv("movie2023.csv", encoding="utf-8-sig")
# df = pd.concat([df1, df2, df3, df4])
# # df 분석
# df["관객수"].max()  # 최대값
# df["관객수"].min()  # 최소값
# df["관객수"].mean()  # 평균
# df["관객수"].nlargest(5)  # 최대 5개
# df["관객수"].nsmallest(5)  # 최소 5개


# --------------------------------------------------------------------
# selenium 라이브러리 가져오기
for i in range(2020,2024):
  url = f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
  browser = webdriver.Chrome()
  # 이동하려는 주소 입력
  browser.get(url)
  time.sleep(3)
  soup = BeautifulSoup(browser.page_source, "lxml")
  # 파일 저장하기
  with open(f"d1107/screen{i}.html", "w", encoding="utf-8") as f:
      f.write(soup.prettify())
  browser.close()
print("프로그램 완료")

