import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
# print(soup.prettify())

# product = soup.find("li", {"id": "thisClick_2190613796"})
# pname = product.find("p")
# print(pname.text)

cate = soup.find("div", {"id": "bestPrdList"}).find("ul",{"class":"cfix"})
lists = cate.find_all("li")
for idx,list in enumerate(lists):
  print(f"{idx+1}번째 상품 : {list.find("p").text}")

# pnames = products.find_all("div",{"class":"pname"})
# for pname in pnames:
#   print(pname.find("p"))
