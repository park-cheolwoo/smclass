from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# 이메일 발송
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 1. 데이터 불러오기
# url = "https://news.naver.com/main/ranking/popularDay.naver"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     "Accepted-Language" : "ko-KR, ko; q=0.9, en-US; q=0.8, en; q=0.7"
# }
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'lxml')
# # print(soup.prettify())
# with open('c1025/news.html','w',encoding='utf8') as f:
#   f.write(soup.prettify())
# ----------------------------------------------------------------
# 2. 언론사, 제목 추출
# with open("c1025/news.html",'r',encoding='utf8') as f:
#   soup = BeautifulSoup(f,'lxml')
# data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div")
# lists = data.select("div.rankingnews_box")
# with open("c1025/news.csv","a",encoding='utf8',newline="") as ff:
#     writer = csv.writer(ff)
#     writer.writerow(
#         [
#             "언론사",
#             "기사1",
#             "기사2",
#             "기사3",
#             "기사4",
#             "기사5",
#         ]
#     )
#     for idx, i in enumerate(lists):
#         title = i.select_one("strong.rankingnews_name").text.strip()
#         conts = i.select("a.list_title")
#         cont_list = []
#         for cont in conts:
#           cont = cont.text.strip().replace(",","")
#           cont_list.append(cont)
#         print(cont_list)
#         writer.writerow([title]+cont_list)
# -------------------------------------------------------------------------
# 3. 메일 보내기

smtpName = "smtp.naver.com"
smtpPort = 587
# 네이버 사이트에서 주는 고정값

sendEmail = "aaaa"
pw = "1111"
recvEmail = "aaaa"

title = "제목 : 오늘 기준 기사 정보를 드립니다."
content = """/
          파일을 확인해주세요.
          감사합니다."""

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

with open("c1025/news.csv", "rb") as f:
    attachment = MIMEApplication(f.read())
    attachment.add_header("Content-Disposition", "attachment", filename="news.csv")
    msg.attach(attachment)


s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, pw)
s.sendmail(sendEmail, recvEmail, msg.as_string(msg))
s.quit()

print("발송 완료")
