import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
datas = soup.select("tbody>tr.lst50")
datas_lists = []
title_list = ["순위", "이미지", "제목", "가수"]


for data in datas:
    data_list = []
    data_list.append(data.select_one("span.rank").text)
    data_list.append(data.select_one("a.image_typeAll>img").attrs["src"])
    data_list.append(data.select_one("div.ellipsis.rank01>span>a").text)
    singers = data.select("div.ellipsis.rank02>a")
    for i in singers:
        data_list.append(i.text)
    print(data_list)
    datas_lists.append(data_list)
with open("c1022/chart.txt", "w", encoding="utf-8") as f:
    f.write(data_list.split(","))
# print(datas_lists)


# print(datas_lists)


# print(datas[0].select_one("span.rank").text)
# print(datas[0].select_one("a.image_typeAll>img").attrs['src'])
# print(datas[0].select_one("div.ellipsis.rank01>span>a").text)
# singers = (datas[0].select("div.ellipsis.rank02>a"))
# for i in singers:
#   print(i.text)

# for data in datas:
#     data_list = []
#     for idx,i in enumerate(data):
#         print(data.select(f"td:nth-child{idx+2}"))

# 순위, 사진 링크주소, 제목, 가수명
