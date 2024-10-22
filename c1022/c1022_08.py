import os
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text, "lxml")

# 1. 제목 2. 금액 3. 평점 4. 평가수 5. 이미지 주소

data = soup.select_one("ul#productList")
product_lists = data.select("dd.descriptions") # 1~12번까지 추출해야함
product_lists2 = data.select("li.search-product")  # 1~12번까지 추출해야함
pro_lists = []

for i in range(0,11+1):
    if not os.path.exists("c1022/coopang"):
        os.makedirs("c1022/coopang")
    with open(f"c1022/coopang/{i}.jpg",'wb') as f:
        pro_list = []
        product_link = product_lists2[i].select_one("a")['href']
        product_name = product_lists[i].select_one("div.name").text  # 상품명
        product_price = product_lists[i].select_one("strong.price-value").text  # 금액
        product_star = product_lists[i].select_one("em.rating") # 평점
        if not product_star:
            product_star = "none"
        else:product_star = int(product_star.text)
        product_count = product_lists[i].select_one("span.rating-total-count") #괄호를 없애는 태그 # 평가수
        if not product_count:
            product_count = "none"
        else:product_count = int(product_count.text[1:-1])
        product_link = product_lists2[i].select_one("img")['src'] # 링크
        # if not product_link:continue
        # img = requests.get(f"http:{product_link}")
        # f.write(img.content)
        print(f"링크 : http:{product_link}, 상품명 : {product_name}, 가격 : {product_price}, 평점 : {product_star}, 평가수 : {product_count}, 이미지 링크 : http:{product_link}")
