
def calc():
  a += 10
  print(a)

a=10 #전역변수
calc()


#----------------------------------------------------------------------------


# 함수 - 매개변수(일반변수, 복합변수)
# 함수 - 복합변수 - return 없이 함수밖 값 사용(10%)

# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] +=100  
  
# hArr = [1,2,3,4,5] #복합변수 - 주소값이 저장됨
# calc(hArr)
# print(hArr)




#------------------------------------------------------------------------------
# 함수 - 일반매개변수 - return 없이 값이 함수 밖으로 나올 수 없음(90%)

# def calc(h):
#     h += 100
#     return h


# h = 20
# calc()  # 호출만 하고 일반변수에 값을 넣어주지 않으면 값이 변경되지 않음
# # h = calc(h)
# print(h)


#------------------------------------------------------------------------------

# def calc():
#     global h # 전역변수
#     h += 100


# h = 20
# calc()  # 함수 호출 후 h에 값을 할당할 필요 없음
# # h = calc(h)
# print(h)