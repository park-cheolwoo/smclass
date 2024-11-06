import requests
from bs4 import BeautifulSoup 

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
conts = soup.find("div", {"class": "rankingnews_box_wrap _popularRanking"})
rankLists = conts.find_all("div",{"class":"rankingnews_box"})
print("개수확인 : ",len(rankLists))
text = []

with open("c1021/a.txt","w",encoding='utf8') as f:
      for idx,rankList in enumerate(rankLists):
        rankingnews_name = rankList.find("strong", {"class": "rankingnews_name"})
        print(f"[{idx+1}. 언론사 : {rankingnews_name.text}]")
        f.write(f"[{idx+1}. 언론사 : {rankingnews_name.text}]\n")
        news = rankList.find("ul",{"class","rankingnews_list"})
        newsLists = news.find_all("li")
        # print("랭킹박스 안 뉴스 개수 : ",len(newsLists))
        for i,newsList in enumerate(newsLists):
            print(f"{i+1}. {newsList.find("a").text}")
            f.write(f"{i+1}. {newsList.find("a").text}\n")

  # for idx,rankList in enumerate(rankLists):
  #     rankingnews_name = rankList.find("strong", {"class": "rankingnews_name"})
  #     print(f"[{idx+1}. 언론사 : {rankingnews_name.text}]")
  #     news = rankList.find("ul",{"class","rankingnews_list"})
  #     newsLists = news.find_all("li")
  #     # print("랭킹박스 안 뉴스 개수 : ",len(newsLists))
  #     for i,newsList in enumerate(newsLists):
  #         print(f"{i+1}. {newsList.find("a").text}")

