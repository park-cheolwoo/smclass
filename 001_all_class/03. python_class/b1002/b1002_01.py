input_str = input("글자를 입력하세요.")

# 문자가 입력되지 않았을 때
if input_str != "":
    print("입력문자 : ", input_str)
    print("프로그램이 종료됩니다.")
else:
    print("글자를 입력하셔야합니다.")

# and(그리고) or(또는) not(부정) << >> && ||  !

# 문자열 숫자
a = "123"
print(type(a))  # str
print(type(int(a)))  # int
print(type(float(a)))  # float

b = "12.3"
# print(type(int(b))) #error : 소숫점이 있는 문자열숫자는 float으로 변경해야함
print(type(float(b)))  # float

c = 12.3
print(type(int(c)))  # int : 실수는  int타입으로 변경 가능
print(int(c))  # 12

# 문자열연결연산자
s1 = "안녕"
s2 = "하세요"
print(s1 + s2)
print(a + b)  # 문자열연결연산자
# print(a*b) #error : 문자열은 -,*,/ 안됨

# 문자열 *2
print(s1 * 10)  # 문자열반복연산자
print("--" * 30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다."  # 문자열 자체 - 리스트 형태
print(str1[0])
print(str1[6])
print(str1[2:5])  # substring : [시작점:종료점-1]
print(str1[:5])  # 처음부터 숫자 앞까지
print(str1[2:])  # 2부터 끝까지
print(str1[1:10:2])  # [위치:위치:step2]
print(str1[1:10:3])
print(str1[::-1])  # 역재생

# [] - 배열 : 한번 범위가 정해지면 수정이 불가 (C,Java)
# [] - 리스트 : 범위 상관없음
