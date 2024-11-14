import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header").text)
# find, find_all = select_one, select (태그를 활용한 검색방법)

# newsbox = soup.select_one("div.rankingnews_box")
# newstit = newsbox.select_one("strong.rankingnews_name")
# print(f"[ 1. 언론사 : {newstit.text} ]")
# newslist = newsbox.select("ul.rankingnews_list>li")
# for idx,i in enumerate(newslist):
#   print(f"{idx+1}. {i.select_one("div.list_content>a").text}")


newsboxes = soup.select("div._officeCard._officeCard12")
print(newsboxes)

