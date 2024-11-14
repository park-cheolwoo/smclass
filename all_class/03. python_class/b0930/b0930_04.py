# #name, kor, eng, math, total, avg 출력
# input으로 입력을 받아
# 홍길동,100,100,99,합계,평균 1줄에 출력하시오.(소숫점 둘째자리까지)
# format함수 사용, f함수 사용

name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요.")) 
total = int(kor) + int(eng) + int(math)
avg = total/3
print("이름 : {}, 국어 : {}, 영어 : {}, 수학 : {}, 합계 : {}, 평균 : {:.2f} ".format(name,kor,eng,math,total,avg))
print(f"이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {total}, 평균 : {avg:.2f}")








# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b) #문자 연결 연산자 100200
# print(int(a)+int(b)) #타입 변경
# # name = "홍길동"
# # print(int(name)) #문자를 숫자로 변경 불가능. 문자숫자는 가능
# c = "3.14"
# print(int(float(c))) #실수형으로 변경 후 정수형으로 변경
# # print(int(c)) #문자실수형은 정수로 바로 변경은 불가 
# print(str(c)) #실수형을 문자열로 변경
# d="True"
# print(bool(d)) #문자불형은 불형으로 변경

# #타입 변경 - str,float,int,bool




# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num=100
# print(type(num))

# a_bool = True # True, False : 대문자 입력
# print(type(a_bool))
# 변수 : 문자형, 정수형, 실수형, 논리형(bool)

# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3

# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)