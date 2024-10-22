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
soup = BeautifulSoup(res.text, "lxml")
# 제목,금액,평점,평가수,링크주소,이미지주소
# 기준점
# 금액 90만원 이상 평점 4.5 이상 평가수 100명 이상


data = soup.select_one("#productList")
lists = data.select("li")
# print("1. 링크주소 :", "https://www.coupang.com" + lists[0].select_one("a")["href"])
# print("2. 제목 :", lists[0].select_one("div.name").text)
# price = int(lists[0].select_one("strong.price-value").text.replace(",", ""))
# print("3. 금액 :", price)
# rating = float(lists[0].select_one("em.rating").text)
# print("4. 평점 :", rating)
# num = int(lists[0].select_one("span.rating-total-count").text[1:-1])
# print("5. 평가수 :", num)
# # print("5. 평가수 :",lists[0].select_one("span.rating-total-count").text)
# print("6. 이미지 :","https:/"+lists[0].select_one("dt.image>img")['src'][1:])


# cnt = 0
# for i in lists:
#     price = i.select_one("strong.price-value")
#     if not price : price = 0
#     else : price = int(i.select_one("strong.price-value").text.replace(",", ""))
#     rating = i.select_one("em.rating")
#     if not rating: rating = 0
#     else : rating = float(i.select_one("em.rating").text)
#     num = i.select_one("span.rating-total-count")
#     if not num : num = 0.0
#     else : num = int(i.select_one("span.rating-total-count").text[1:-1])
#     print(f"1. 가격 : {price}, 2. 평점 : {rating}, 3. 평가수 : {num}")
#     if price >= 900000 and rating >= 4.5 and num >= 100:
#         print("범위 안에 들어옴")
#         cnt += 1
#     print("-"*70)
# print(cnt)

n_lists = []
cnt = 0
for idx,i in enumerate(lists):
    try:
        # price, rating, num 타입변경
        price = int(i.select_one("strong.price-value").text.replace(",", ""))
        print(f"1. 가격 : {price:,}")
        rating = float(i.select_one("em.rating").text)
        print("2. 평점 : ",rating)
        num = int(i.select_one("span.rating-total-count").text[1:-1])
        print("3. 평가수 : ",num)
        print()
    except Exception as e:
        print(f"{idx+1} 번째 제외,e")
    finally:
        if price >= 900000 and rating >= 4.5 and num >= 100:
            title= i.select_one("div.name").text
            img = f"https:/{lists[0].select_one("dt.image>img")['src'][1:]}"
            n_lists.append(
                { 
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "num" : num,
                    "img" : img
                }
            )
            print("범위 안에 들어옴")
            cnt += 1
        else : continue
    print("-"*70)
# print(n_lists)
# print(cnt)


while True:
    print(" [ 노트북 비교 ] ")
    print("1. 금액정렬")
    print("2. 금액역순정렬")
    print("3. 평점정렬")
    print("4. 평점역순정렬")
    print("5. 출력")
    print("0. 종료")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == "0":
        print("프로그램을 종료합니다.")
        break
    elif choice == "1":
        n_lists.sort(key=lambda x:x['price'])
        print("정렬이 완료되었습니다.")
    elif choice == "2":
        n_lists.sort(key=lambda x:x['price'],reverse=True)
        print("정렬이 완료되었습니다.")
    elif choice == "3":
        n_lists.sort(key=lambda x:x['rating'])
        print("정렬이 완료되었습니다.")
    elif choice == "4":
        n_lists.sort(key=lambda x:x['rating'],reverse=True)
        print("정렬이 완료되었습니다.")
    elif choice == "5":
        print(n_lists)