# 두 수를 입력받아 두 수까지 합계를 구하시오.

# 1. if문 사용
# sum = 0
# num1 = int(input("첫번째 숫자를 입력하세요."))
# num2 = int(input("두번째 숫자를 입력하세요."))
# max_num=num2;min_num=num1
# if num1>num2:
#     max_num=num1;min_num=num2
# for i in range(min_num, max_num + 1):
#         sum += i
# print(f"합계 : {sum}")

# 2. min,max함수 사용
# sum = 0
# num1 = int(input("첫번째 숫자를 입력하세요."))
# num2 = int(input("두번째 숫자를 입력하세요."))
# # max_num = max(num1,num2)
# # min_num = min(num1,num2)
# for i in range(min(num1,num2), max(num1,num2) + 1):
#     sum += i
# print(f"합계 : {sum}")

# 3. if문 사용
sum = 0
num1 = int(input("첫번째 숫자를 입력하세요."))
num2 = int(input("두번째 숫자를 입력하세요."))
num3=0
if num1 > num2:
    num1, num2 = num2, num1  # 파이썬만 가능 - 두개 변수 치환
    num3 = num1
    num1 = num2
    num2 = num3

for i in range(num1, num2 + 1):
    sum += i
print(f"합계 : {sum}")


# # 1,3,5,7,9,... 99 총 합계
# sum=0
# for i in range(1,100+1,2):
#   sum +=i
# print(f"합계 : {sum}")


# # 1에서 100까지 숫자의 합을 구하시오.
# sum = 0
# for i in range(0,100+1):
#   sum += i
# print(f"합계 : {sum}")


# for i in range(3):
#   print(f"{i}:안녕하세요.")

# for _ in range(3):
#   print("안녕하세요.")


# 1-1번출력 2-2번출력 3-3번출력
# for i in [1,2,3]:
#   print("안녕하세요.\n"*i,end="")
#   print("-"*30)


# for i in [1,2,3]:
#   print("안녕하세요.")


# for문 사용해서
# *
# **
# ***
# ****
# *****
# for i in range(1,5+1):
#       print("*"*i)

# *****
# ****
# ***
# **
# *

# for i in range(5,1-1,-1): # -1씩 감소
#   print("*"*i)


# 구구단 1,3,5,7,9단만 출력
# for i in range(1, 9 + 1, 2):  # (시작값,끝값+1,증가값)
#     print(f"[{i} 단]")
#     for j in range(1, 9 + 1):
#         print(f"{i}X{j}={i*j}")
#     print("-" * 10)

# 1,3,5,7,9 까지 출력하시오.
# for i in range(10):
#   if i%2==1:
#    print(i)

# 구구단을 출력하시오.
# for i in range(1,9+1):
#   print(f"[{i} 단]")
#   for j in range(1,9+1):
#     print(f"{i}X{j}={i*j}")
#   print("-"*10)

# for i in range(1,5+1):
#   n = 2*i-1
#   for j in range(1,9+1):
#     print(f"{n}X{j}={n*j}")
#   print("-"*10)

# #1부터 10까지 for문 사용 출력
# for i in range(1,10+1):
#   print(i)
