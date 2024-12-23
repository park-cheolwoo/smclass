# str1 = input("문자를 입력하세요.")
# a=len(str1) #문자의 길이 : leng
# if a==5: 
#   print("a는 5입니다.")
# elif a==4: # elif = else if
#   print("a는 4입니다.")
# elif a==3:
#   print("a는 3입니다.")
# else:
#   print("a는 2 이하 입니다.")

money = int(input("머니를 입력하세요."))
m_l = len(money)
if m_l<5:
  print("오만원의 개수는 {}입니다.".format(money//50000))
  print("만원의 개수는 {}입니다.".format((money%50000)//10000))
  print("오천원의 개수는 {}입니다.".format((money%10000)//5000))
  print("천원의 개수는 {}입니다.".format((money%5000)//1000))
  print("오백원의 개수는 {}입니다.".format((money%1000)//500))
  print("백원의 개수는 {}입니다.".format((money%500)//100))
  print("오십원의 개수는 {}입니다.".format((money%100)//50))
  print("십원의 개수는 {}입니다.".format((money%50)//10))

  
else:
  print("금액이 너무 적습니다.")



#1759870
#9870
#590



# money = 780
# 500 - 1 
# 100 - 2 
# 50 - 1 
# 10 - 3

# print("500원 동전개수 : {}".format(money//500))
# print("100원 동전개수 : {}".format((money%500)//100))
# print("50원 동전개수 : {}".format((money%100)//50))
# print("10원 동전개수 : {}".format((money%50)//10))

# money = 1759870
# 50000 - 35
# 10000 - 0
# 5000 - 1
# 1000 - 4
# 500 - 1
# 100 - 3
# 50 - 1
# 10 - 2

# print("오만원 개수 : {}".format(money//50000))
# print("만원 개수 : {}".format((money%50000)//10000))
# print("오천원 개수 : {}".format((money%10000)//5000))
# print("천원 개수 : {}".format((money%5000)//1000))
# print("오백원 개수 : {}".format((money%1000)//500))
# print("백원 개수 : {}".format((money%500)//100))
# print("오십원 개수 : {}".format((money%100)//50))
# print("십원 개수 : {}".format((money%50)//10))