# 숙제 : 아래의 결과값을 출력하는 함수
# 1~10 : 1
# 11~20 : 11
# 21~30 : 21

# ((((Number-1)//10)*10)+1)


stu_data = ['홍길동',100,100,100,99]
stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
  [1,'유관순',100,100,100,99],
 [2,'이순신',100,99,98,99],
 [3,'김구',80,100,90,99]
 ] 


#학생데이터를 1줄로 출력하시오(합계, 평균 추가) (!)
print("                     [ 학생성적 프로그램 ]")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
      stu_title[0],stu_title[1],stu_title[2],
      stu_title[3],stu_title[4],stu_title[5],
      stu_title[6],stu_title[7]))
# print("-"*60)


# for s_t in stu_title:
#   print("{}".format(s_t),end='\t')
# print('\n')
# print("-"*60)


print("-"*60)
for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(
       s[0],s[1],s[2],
       s[3],s[4],s[5],
       s[2]+s[3]+s[4]+s[5],(s[2]+s[3]+s[4]+s[5])/4))
## 학번,이름,국어,영어,수학,과학,합계,평균


# # 이순신의 합계를 출력하시오.
# name = stu_datas[1][0]
# kor = stu_datas[1][1]
# eng = stu_datas[1][2]
# math = stu_datas[1][3]
# si = stu_datas[1][4]
# total = kor+eng+math+si
# avg = total/4
# print("{}의 합계 : {}".format(name,avg))



# name = stu_data[0]
# kor = stu_data[1]
# eng = stu_data[2]
# math = stu_data[3]
# si = stu_data[4]
# total = kor+eng+math+si
# avg = total/4

# print("학생이름 : {}\n국어 : {}\n수학 : {}\n영어 : {}\n과학 : {}\n합계 : {}\n평균 : {}".format(name,kor,eng,math,si,total,avg))







# 원의 넓이 : 반지름*반지름*3.14
# 반지름을 입력받아 원의 넓이를 구하시오.
# r = float(input("반지름의 길이를 입력하세요.(r>0)"))
# print("원의 넓이 : {:.2f}".format(r**2*3.14))
# print(f"원의 넓이 : {(r**2*3.14):.2f}")



# # 1번에 2개의 길이를 입력받아 삼각형의 넓이와 직사각형의 넓이를 구하시오.
# length = input("2개 길이를 입력하세요.")
# print(length.split(" "))
# l_list = length.split(" ")
# print("삼각형의 넓이 : {}".format((float(l_list[0]))*(float(l_list[1]))*0.5))



# r1 = float(input("가로 길이를 입력하세요.(>0)"))
# r2 = float(input("세로 길이를 입력하세요.(>0)"))
# area1 = r1*r2*0.5
# area2 = r1*r2
# print("삼각형의 넓이 : {:.2f}".format(area1))
# print(f"사각형의 넓이 : {area2:.2f}")
# print("삼각형의 넓이 : %.2f" % (area1))









###복합대입연산자 += -= *= /= %= **= //= ###
# a=10
# a+=5;print(a)
# a-=5;print(a)
# a*=5;print(a)
# a/=5;print(a)
# a//=5;print(a)
# a**=5;print(a)
# a%=5;print(a)






###숫자를 문자열로 변환###
# 문자열+숫자 : 불가능
# a=100
# b=10
# print(str(a)+str(b))


###문자형숫자 변환###
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) #정수형 > 정수타입, 실수타입 변경가능
# # print(int(b)) #실수형 > 실수타입 변경가능
# # print(float(c)) #숫자가 아닌 문자는 숫자형 타입으로 변경 불가



# aa=10
# bb=5

# #1줄 선언 방식
# a=10;b=5
# c,d = 10,20
# #1줄 선언 방식
# s1,s2,s3 = 1,2,3


###우선순위###
# print(2+2-2*2/2*2)
# print((2+2)-(((2*2)/2)*2))

###사칙연산 +-*/ 추가연산%**//###
# a=5;b=3 # 1줄형태로 표현시 ;(세미콜론) 넣어주면 됨.
# # /, %, //, **
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)
# print("{},{},{},{}".format((a/b),(a%b),(a//b),(a**b)))