# a=((1,2),(3,4),(5,6))
# print(a[0])
# print(a[0][1])



# #문자열 > 튜플 타입 > 리스트 타입으로 변경 가능
# a_str = "abcde"
# # print(a_str)
# # print(a_str[1])
# a_tu = tuple(a_str)
# list(a_tu)
# print(list(a_tu))


# a='우유'
# b='커피'
# c=''
# print(a)
# print(b)

# #파이썬 a,b 치환
# a,b = b,a
# print(a)
# print(b)


# #기본적인 a,b 치환
# c = a
# a = b
# b = c
# print(a)
# print(b)


# aArr = [[1,2],[[1,2],[3,4]],[3,4],[5,6],[7,8]]
# a_list = [1,2,3,4,5,6,7,8]

# b_list = []
# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       if type(j) == list:
#         for k in j:
#           b_list.append(k)
#       else:
#         b_list.append(j)
# print(b_list)


# t = (1,2,3,4)
# print(type(t))


# t = [3,5,1,2]
# t.sort() #t리스트에 반영
# print(t) #t변경됨

# t[1:3] #t가 변경되지 않음
# t.extend([3,7]) #t에 반영됨
# print(t+[3,7]) #t에 반영되지 않음
# print(t)


# # 튜플 - 리스트 타입과 같음, 순서가 있음
# t = (1, 2, 3, 4)
# print(t)
# print(t[0])
# # t[0]=100 # 튜플은 수정 불가
# # t.append(100) # 튜플은 추가 불가
# print(len(t))
# print(t[0])
# #for문 가능
# for i in t:
#   print(i)

# #더하기 연산자로 추가 가능
# t=t+(3,5)
# print(t)
# #곱하기 연산자 가능
# tt=(1,2,3)
# tt *=2
# print(tt)

# tArr = [1, 2, 3, 4]
# tArr[0] = 100
# print(tArr)
