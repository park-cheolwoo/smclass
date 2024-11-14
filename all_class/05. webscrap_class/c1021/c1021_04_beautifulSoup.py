import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url,headers=headers)
# res.raise_for_status()
# with open('c1021/1.html','w',encoding='utf-8') as f:
#   f.write(res.text)


# soup.prettify() 정보 저장
# html, css 정보를 가진 소스로 변경
soup = BeautifulSoup(res.text,"lxml") # str -> html 태그, css 태그 사용될 수 있는 형태로 변경


# print(soup.find("div",attrs = {"id":"header"}))
print(soup.find("div",{"id":"header"})) # div태그 id='header'
print(soup.find("h2", {"class": "rankingnews_tit"}).text) # h2태그 class = 'rankingnews_tit'의 text를 출력
print(soup.find_all("div")) # 모든 div 태그 검색
print(len(soup.find_all("div"))) # 모든 div 태그 개수 출력
print(type(soup.find_all('div'))) # ResultSet : 객체의 리스트 형태

# # 태그 출력, 태그 문자열 출력
# print(soup.title) # html 태그를 출력
# print(soup.title.text) # html 태그 안 문자열을 출력
# # print("없는 태그 : ",soup.titletitletitle) # 없는 태그 입력시 None 출력
# # print("없는 태그 : ",soup.titletitle.text) # 없는 태그 문자열 출력시 에러
# print(soup.a) # 여러 a 태그 중 첫번째 거만 가져옴
# print(soup.a.next.text) # next >> 다음 태그를 가져옴

# # 태그 속성 출력
# print(soup.a.attrs) # attrs >> 태그의 속성값을 가져옴 : 딕셔너리 형태
# print(soup.a['href']) # href의 속성값만 가져옴
# # with open('c1021/2.html','w',encoding='utf8') as f:
# #   # soup.prettify() : 소스가 정리되어 저장됨.
# #   f.write(soup.prettify())

# print("완료")
# # print(res.text)
