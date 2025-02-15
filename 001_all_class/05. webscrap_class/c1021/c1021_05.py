import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
print(soup.title) # 제일먼저 찾아지는 것을 출력
print(soup.find('title')) # 특정 위치의 태그와 속성을 가지고 찾아줌
print(soup.find('div',{'class':'rankingnews_box_wrap'}))
rankingnews_box_wrap = soup.find("div", {"class": "rankingnews_box_wrap"})
newLists = rankingnews_box_wrap.find_all('div',{'class':'rankingnews_box'})
print("여러개 개수 확인 : ",len(newLists))

for newList in newLists:
  print(newList.find('strong',{'class':'rankingnews_name'}).text)

# # find : 1개 검색
# rankingnews_wrap = soup.find("div", {"class": "rankingnews_box_wrap"})

# # find_all : 여러개 검색
# rankingnews_boxs = rankingnews_wrap.find_all('div',{'class':'rankingnews_box'})
# print(len(rankingnews_boxs))

# rankingnews_boxs_name = rankingnews_boxs.find('strong',{"class":"rankingnews_name"})
# print(rankingnews_boxs_name)
# print(len(soup.find_all("div", {"class": "rankingnews_box"})))
