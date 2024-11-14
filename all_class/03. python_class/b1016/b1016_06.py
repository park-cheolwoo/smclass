import os

# os.path.exists() : 현재 폴더가 존재하는지 확인
# mkdir : 현재 폴더만 생성
# makedirs : 현재 폴더, 하위 폴더까지 생성

# 폴더가 없을 시 폴더 생성
if not os.path.exists("c:/ddd"):
  os.makedirs("C:/ddd")
f = open('c:/ddd/c.txt','w',encoding='utf-8')
f.write("안녕하세요.")
f.close()