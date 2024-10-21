# requests 라이브러리 : WEB 페이지 소스를 python으로 들고오는 라이브러리(웹 정보를 요청하는 라이브러리)
# beautifulsoup4 라이브러리 : HTML/XML 파일에서 원하는 데이터를 손쉽게 parsing할 수 있는 라이브러리(HMTL 태그를 str에서 찾는 라이브러리)
# lxml 라이브러리 : css 문법으로 특정 요소를 가져올 수 있는 라이브러리


# 웹스크래핑 세팅
import requests
# res = requests.get("https://www.google.com/") # HTML 소스를 가져옴.
res = requests.get("https://www.naver.com/") # HTML 소스를 가져옴.

# res = requests.get("http://www.melon.com/")  
# # res.raise_for_status() # 에러시 종료(raise : 프로그램 미구현시 임의로 에러 발생)
# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")

# print("응답코드 : ", res.status_code)  # 응답코드 : 200(성공) / 400(클라이언트 에러) / 500(서버 에러)

# print(res.text) # html 소스 출력

# requests로 정보를 가져올 시 
# 제이쿼리, 자바스크립트, 외부페이지(iframe), react, vue... >> 비동기식으로 작동되는 소스는 못가져옴
#

print("총 문자 길이 : ",len(res.text))


# # 웹 소스코드를 파일로 저장
# f = open("c1021/a.html",'w',encoding='utf-8')
# f.write(res.text)
# f.close()

# #f.close()를 안해도 자동으로 닫힘
with open('c1021/naver.html','w',encoding='utf-8') as f:
  f.write(res.text)