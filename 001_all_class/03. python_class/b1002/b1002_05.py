students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
]

s = [4, "강감찬", 100, 90, 99]

#반복문
for i in range(10): # 0부터 시작해서 10번 반복
  print(i)

for i in range(2,5): #2부터 5 전까지 반복
  print(i)

for i in range(1,10,2): #1부터 10전까지 2씩 띄워서 반복
  print(i)

aArr = [1,2,5,7,8]
for i in aArr: #리스트 값을 1개씩 가져와서 출력
  print(i)

#enumerate : index번호를 추가해서 가져올 수 있음.
for i,data in enumerate(aArr): #리스트 값과 index 번호를 함께 출력
  print(i,":",data)



aStr = "안녕하세요" #문자열의 값을 한개씩 가져와서 출력
for i in aStr:
  print(i)

# #s(리스트)에 합계와 평균을 추가하시오
# total = s[2]+s[3]+s[4]
# avg = total/3
# s.append(total)
# s.append(avg)
# print(s)

# list 추가 - append(뒤에추가) insert(원하는위치) del(위치삭제) remove(value값 삭제)
# a_list = [1, 2, 3]
# a_list.append(10)  # 마지막에 10 추가
# print(a_list)
# a_list.insert(2, 100)  # 2번에 100 추가
# print(a_list)
# del a_list[1]  # 1번 삭제
# print(a_list)
# a_list.remove(100)  # 100이라는 값을 삭제
# print(a_list)

# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈."

# print(len(str)) #글자 길이수

# #뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1:])
# print(str[::-1])
