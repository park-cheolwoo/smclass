# 매개변수가 일반변수일 경우 return하지 않으면 변수값 변동이 없음
# hh = 100

# def add(hh):
#   hh = hh+100

# add(hh)
# print(hh)

# -----------------------------------------------------------------
# # 복합변수
# hong = [1,2,3,4,5]

# # 매개변수가 복합변수(리스트, 딕셔너리)일 경우, return 없어도 값이 변경되어 전달됨.
# def add(h):
#   for i in range (len(h)):
#     h[i] = h[i]+100

# add(hong)
# print(hong)

# ----------------------------------------------------------------------
#전역변수인 경우 함수에서 변경시 외부에서도 (return 없이) 같이 변경됨
#함수 외부에서도 사용 가능
#지역변수는 return 없이는 값이 함수 밖으로 나오지 못함
def calc():
  global sum
  sum = 200

sum = 10
print(sum)
calc() #함수에서 sum을 200으로 변경함
print(sum) #결과값은 sum이 200이 됨 


# kim = []

# kim = hong #얕은 복사
# kim[0] = 100
# print(hong)


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5=[s1,s2,s3,s4]
#   return s5

# s5 = calc(10,5)
# print(s5)
# print(s5)
# print(s5)
# print(s5)

# print("프로그램 종료")


# # 함수 내에 선언된 변수는 외부에서 사용할 수 없음.
# def calc(v1, v2):
#     global sum # 전역변수
#     # sum = 0  # 지역변수
#     for i in range (v1,v2+1):
#        sum +=i
#     return sum

# sum = 100 #외부의 변수를 사용해서 계산을 하고 싶을 경우
# sum = calc(1,10)
# print(sum)

# print(1,2,3,sep=",",end="\t") #가변매개변수
# print("안녕")


# def calc(n1 = 10, n2=20): #키워드매개변수 - n1의 값이 없으면 n1의 default는 10
#   print(n1)
#   print(n2)
# calc() #매개변수가 없으면 기본값으로 출력됨
# calc(20) #n1=20, 20 #키가 없으면 무조건 1번째로 전달이 됨
# calc(20) #키가 없으면 무조건 1번째로 전달됨
# calc(n2=100) #키가 있으면 키값으로 전달됨


# def calc(n1,n2): #기본매개변수 - 매개변수의 개수가 동일해야 작동(다르면 에러)
#   print(n1,n2)
# calc(n1,n2)


# def calc(*n): # 가변매개변수 - 매개변수의 개수를 맞춰줄 필요 없음
#   print(n)
#   print(len(n))
# calc()


# numStr = input("숫자를 입력하세요.(1,2,3)")
# num,num2,num3 = list(map(int,numStr.split(",")))

# def calc(num,num2,num3):
#   print(f"세수 더하기 : {num+num2+num3}")
#   print(f"세수 빼기 : {num-num2-num3}")
#   print(f"세수 곱하기 : {num*num2*num3}")
#   print(f"세수 나누기 : {num/num2/num3}")

# calc(num,num2,num3)


# numStr = input("숫자를 입력하세요.(1,2,3)")
# numStr2 = list(map(int,numStr.split(",")))
# numStr3 = [i for i in numStr2]


# def calc(numStr2):
#   s1 = 0
#   s2 = 1
#   for i in range(len(numStr2)):
#     s1+=numStr2[i]
#     s2*=numStr2[i]
#   print(f"더하기 : {s1}")
#   print(f"곱하기 : {s2}")

# calc(numStr2)

# calc(num,num2,num3)


# numStr = input("숫자를 입력하세요.(12,5)")
# numStr2 = numStr.split(",")
# num = int(numStr2[0])
# num2 = int(numStr2[1])
# def calc(num,num2):
#   print(f"두수 더하기 : {num+num2}")
#   print(f"두수 빼기 : {num-num2}")
#   print(f"두수 곱하기 : {num*num2}")
#   print(f"두수 나누기 : {num/num2}")

# calc(num,num2)


# 함수 사용
# def calc(num,num2):
#     print(f"두수 더하기 : {num+num2}")
#     print(f"두수 빼기 : {num-num2}")
#     print(f"두수 곱하기 : {num*num2}")
#     print(f"두수 나누기 : {num/num2:.2f}")

# num=[10,20,30]
# num2=[5,7,3]
# for i in range(3):
#   calc(num[i],num2[i])


# #for문을 활용한 계산
# num=[10,20,30]
# num2=[5,7,3]

# for i in range(3):
#   print(f"두수 더하기 : {num[i]+num2[i]}")
#   print(f"두수 빼기 : {num[i]-num2[i]}")
#   print(f"두수 곱하기 : {num[i]*num2[i]}")
#   print(f"두수 나누기 : {num[i]/num2[i]:.2f}")
#   i+=1
