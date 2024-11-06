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

smtpName = "smtp.naver.com"
smtpPort = 587

# id, pw, 받는사람 이메일주소

sendEmail = "aaaa"
pw = "1111"
recvEmail = "aaaa"

title = "제목 : 파이썬 이메일 보내기 안내"
content = "파일을 첨부합니다" 

# 설정

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

# 파일 첨부
with open("c1025/nshop.csv",'rb') as f:
  attachment = MIMEApplication(f.read())
  attachment.add_header("Content-Disposition",'attatchment',filename = "nshop.csv")
  msg.attach(attachment)

# 서버 이름, 서버 포트 설정
s = smtplib.SMTP(smtpName, smtpPort)
s.starttls() # 보안인증
s.login(sendEmail, pw)
s.sendmail(sendEmail, recvEmail, msg.as_string(msg))
print("msg : ")
print(msg.as_string())
s.quit()

# 메일발송 완료
print("메일을 발송했습니다.")
