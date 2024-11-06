import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

music_list = soup.find("li", {"class": "issue_list04"})
print(len(music_list))
music_tit = music_list.find("span", {"class": "title ellipsis"})
print(music_tit.text)


# music_title = music_list.find_all("span",{"class":"title"})
# for i in music_title:
#   print(i.text)

# print(soup)
# music_list = soup.find("ul", {"class": "hot_issue"})
