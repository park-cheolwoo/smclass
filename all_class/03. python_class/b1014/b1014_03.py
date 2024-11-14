# 두 수를 입력받아 두 수를 출력하시오.


def plus(num1,num2):
    return num1+num2


print(plus(int(input("첫번째 숫자를 입력하세요.")), int(input("두번째 숫자를 입력하세요."))))


# def plus(n1,n2):
#   result = n1+n2
#   return result

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))
# def plus2(n1,n2):
#   return n1+n2


# 2-50 3-7 5-50 까지 사이의 값을 모두 더해서 출력하시오.

# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end+1):
#     sum +=i
#   return sum

# total = 0


# print("2부터 50까지의 합 : {:,d}".format(num_sum(2,50)))
# print("3부터 7까지의 합 : {:,d}".format(num_sum(3,7)))
# print("5부터 50까지의 합 : {:,d}".format(num_sum(5,50)))
# total = num_sum(2,50)+num_sum(3,7)+num_sum(5,50)

# print("합계 : {:,d}".format(total))


# def num_sum(st, end):
#     sum = 0
#     for i in range(st, end):
#         sum +=i
#     return sum

# # num1 = int(input("첫번째 숫자를 입력하세요."))
# # num2 = int(input("두번째 숫자를 입력하세요."))

# total = num_sum(1, 10) + num_sum(1, 100)
# # 1-10 합과 1-100 합의 총합
# print("합계 : ", total)
# print("프로그램 종료")


# #두수를 입력받아, 그 사이의 숫자 합을 구하시오.
# #st,en
# #함수 사용
# num1 = int((input("첫번째 숫자를 입력하세요.")))
# num2 = int(input("두번째 숫자를 입력하세요."))
# def num_sum1(num1,num2):
#   sum = 0
#   for i in range(num1,num2+1):
#      sum +=i
#   print("합계 : ",sum)

# num_sum1(num1,num2)

# # 1-10까지 합계를 출력하시오.
# num_sum(1, 10)
# # 1-100까지 합계
# num_sum(1, 100)
# # 2-50
# num_sum(2, 50)
# # 100-1000
# num_sum(100, 1000)
