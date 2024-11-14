import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
rankingnews_box = soup.find("div", {"class": "rankingnews_box"})
# print(rankingnews_box)


# 1. 뉴스사 제목 출력
rankingnews_head = rankingnews_box.find("strong")
print()
print("-" * 60)
print("타이틀 : ",rankingnews_head.text)

# 2. 뉴스 제목 5개 출력
rankingnews_lists = rankingnews_box.find_all("li")
# print(rankingnews_list)
print("개수 : ",len(rankingnews_lists))
print()
print("-" * 60)
for i,t in enumerate(rankingnews_lists):
    print(f"{i+1}. {t.find("a", {"class": "list_title nclicks('RBP.rnknws')"}).text}")

# for i in rankingnews_list:
#   print(i.find("a",{'class':"list_title nclicks('RBP.rnknws')"}).text)


# find_all :: 끝에 's' 붙이는 것으로 통일