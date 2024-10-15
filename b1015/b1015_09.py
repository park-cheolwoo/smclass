# [ 문제 ]
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]

# a와 b를 더해서 [11,22,33,44]를 리스트로 저장(1. 함수로 구현 2. lambda로 구현)


# 0. 리스트 내포

# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# aArr = [i + j for i, j in zip(a, b)]
# print(aArr)

# 1. 함수
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# aArr = []
# def func(a,b):
#   for i,j in zip(a,b):
#     aArr.append(i+j)
# print(func(a,b))

# def func(a):
#   for i in a:
#     aArr.append(i*i)
#   return aArr
# print(func(a))


# 2. lambda
# a = [1,2,3,4]
# b = [10,20,30,40]
# # map(lambda 매개변수1, 매개변수2:리턴값,복합자료형1,복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)


# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2


# a = [1,2,3,4]
# b = [10,20,30,40]


# zip함수 : 2개 리스트 1개로 변경
# a = [1,2,3,4]
# b = [10,20,30,40]

# print(list(zip(a,b))) # 리스트 안에 튜플 타입으로 들어감
# print(dict(zip(a,b)))


# filter(함수, 반복가능한자료형 - 리스트, 튜플, 딕셔너리)


# filter함수 사용
# def func(v):
#     if v % 2 == 0:
#         return True
#     else:
#         return False

# aArr 값 중에 2의 배수인 경우에만 리턴
# aArr = [1, 2, 3, 4]
# bArr = list(filter(func, aArr)) # 결과가 filter 타입이므로 리스트 타입으로 변경해줘야함
# print(bArr)

# 람다식 변경
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)


# 기본적인 함수 사용
# def func(v):
#     if v % 2 == 0:
#         return v


# aArr = [1, 2, 3, 4]
# bArr = []
# for i in aArr:
#     if func(i) != None:
#         bArr.append(func(i))
# print(bArr)

# def function(v):
#     return v*2


# 기본적인 함수 사용
# aArr = [1,2,3,4]
# print(function(2))


# bArr = []
# for i in aArr:
#     bArr.append(function(i))

# print(bArr)

# # 리스트 내포
# aArr = [1, 2, 3, 4]
# print(aArr)
# bArr = [i*2 for i in aArr ]
# print(bArr)

# # map함수 # map(함수, 리스트) >> 리스트의 내용을 1개씩 함수에 전달해서 결과값을 출력
# aArr = [1, 2, 3, 4]
# # bArr = list(map(function,aArr)) #결과가 map 타입이므로 리스트 타입으로 변경해줘야함


# bArr = list(map(lambda x:x*2,aArr)) #lambda 함수는 1줄만 가능
# print(bArr)
