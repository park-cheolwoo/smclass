subject = ["국어", "영어"]
score = []
sum = 0

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    s_input = input("과목을 추가해주세요. >> ")
    subject.append(s_input)
  elif choice == "0":
    break


for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.")))
  sum += score[i]

for i in range(len(score)):
  print(i)
print("합계 : " ,sum)



# num = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))
# num4 = int(input("과학점수를 입력하세요."))
# num5 = int(input("역사점수를 입력하세요."))
# print("국어 : ", num)
# print("영어 : ", num2)
# print("수학 : ", num3)
# print("과학 : ", num4)
# print("역사 : ", num5)
# print("합계 : ", num + num2 + num3 + num4 + num5)


# a=10
# b=20
# c=30

# # a에 a+b+c의 합을 리턴받아 출력

# def func(x,y,z):
#   x = x+y+z
#   print(x)
#   return x

# a = func(a,b,c)
# print(a)


# a = 10
# b = 20

# def add(a,b): #함수선언
#   return a+b

# sum = add(a,b) # 함수호출
# print("a+b 합계 : ",sum)


# a = 10  # 전역변수


# # 함수선언
# def func(a):
#   print("함수내 a : ",a)
#   a +=50
#   return a
# # 함수호출
# a = func(a)
# print("함수밖 a : ",a)


# subject = ["국어","영어"]
# def output():
#   while True:
#     print(" [과목 생성 프로그램] ")
#     s_input = input("원하는 과목을 입력하세요. >> ")
#     subject.append(s_input)
#     print("과목")
#     print("-"*20)
#     for s in subject:
#       print(s)

# output()
