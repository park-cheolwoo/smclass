# naver 파일 웹 스크래핑, 리솜리조트 파일저장

import requests

# url = "https://www.naver.com"
# url = "https://www.resom.co.kr/resom/main/main.asp"
# url = "https://www.coupang.com/"


# for문을 활용한 웹 스크래핑
# url = [
#     "http://www.coupang.com/"
#     # "http://www.naver.com",
#     # "https://www.resom.co.kr/resom/main/main.asp",
#     # "http://www.daum.net/",
# ]
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
# }

# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   with open(f'c1021/{i+1}.html','w',encoding='utf-8') as f:
#       f.write(res.text)

# print("프로그램 종료")

# res2 = requests.get("https://www.resom.co.kr/resom/main/main.asp")
# with open('c1021/resom.html','w',encoding='utf-8') as f:
#     f.write(res2.text)

url = "http://www.coopang.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)

with open("c1021/coopang.html",'w',encoding='utf-8') as f:
  f.write(res.text)