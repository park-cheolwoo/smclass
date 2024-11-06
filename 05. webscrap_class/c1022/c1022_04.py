# sum = 0
# a = "123,000"
# b = "10,000"
# sum += int(a.replace(",",""))
# sum += int(b.replace(",",""))
# print(sum)

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url,headers=headers)
data = BeautifulSoup(res.text,'lxml')

# trs = data.select_one("tr.type1")
# for i in trs:
#   print(i.text.strip())

# tds = data.select("table>tr")
