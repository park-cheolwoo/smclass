product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]
ff = open('b1017/product.txt','w',encoding='utf-8')
for s in product:
  t = list(s.values())
  ff.write(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]}")
print("저장이 완료되었습니다.")
ff.close()
