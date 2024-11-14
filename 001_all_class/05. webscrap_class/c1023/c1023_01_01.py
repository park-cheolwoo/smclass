# 30개 주식정보를 csv 파일로 저장
import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#데이터 기준
data = soup.select_one("#contentarea > div.box_type_l > table")
#제목
st_list = [s.text for s in data.select("th")]

#값
stocks = data.select("tr")
# print(stocks[2])
sto_list = [
    s.text.strip() for s in stocks
]

print(sto_list[2])
# with open("aa.csv",'w',encoding='utf-8-sig',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(st_list)
#     for idx,i in enumerate(sto_list):
#       if len(i) <= 1 : sto_list.remove(i)
#       else :   writer.writerow(i)




