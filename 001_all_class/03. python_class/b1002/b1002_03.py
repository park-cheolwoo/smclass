# if - elif - else

# 100 99 98 A+
# 97 96 95 94 A
# 93 92 91 90 A-

# num = int(input("성적을 입력하세요."))
# score = ""

# if 90<=num:
#     score="A"
#     if 98<=num:
#         score = score+"+"
#     elif num<=93:
#         score = score+"-"


# if 98 <= num:
#     score = "A+"
# elif 94 <= num: #이 구절에서 이미 num은 98보다 작으므로 94보다 큰지만 체크해도 됨(다만 큰 수에서 작은 수 순서대로 비교해줘야함)
#     score = "A"
# elif 90 <= num:
#     score = "A-"
# elif 88 <= num:
#     score = "B+"
# elif 84 <= num:
#     score = "B"
# elif 80 <= num:
#     score = "B-"
# elif 78 <= num:
#     score = "C+"
# elif 74 <= num:
#     score = "C"
# elif 70 <= num:
#     score = "C-"
# elif 68 <= num:
#     score = "D+"
# elif 64 <= num:
#     score = "D"
# elif 60 <= num:
#     score = "D-"
# else:
#     score = "F"
# print(score)


# 3,4,5월 - 봄 // 6,7,8월 - 여름 // 9,10,11월 - 가을 // 12,1,2월 - 겨울
# num = int(input("숫자를 입력하세요."))
# if 3<=num<=5:
#     print("봄입니다.")
# elif 6<=num<=8:
#     print("여름입니다.")
# elif 9<=num<=11:
#     print("가을입니다.")
# elif num==12 or 1<=num<=2:
#     print("겨울입니다")
# else:
#     print("숫자를 잘못 입력하셨습니다.")


# 입력한 숫자가 10보다 작거나 100보다 클 때(10, 100 포함) 정답입니다. 오답입니다. 출력
# num = int(input("숫자를 입력하세요."))
# if 10 <= num <= 100:
#     print("정답입니다.")
# else:
#     print("오답입니다.")


# 입력한 숫자가 1보다 크고(1 포함) 10보다 작을 때(10 포함)만 정답입니다. 오답입니다. 출력
# num = int(input("숫자를 입력하세요."))
# if 1 <= num <= 10:  # if num>=1 and num<=10
#     print("정답입니다.")
# else:
#     print("오답입니다.")


# 입력한 숫자가 짝수인지 홀수인지 출력하시오.
# num = int(input("숫자를 입력하세요."))
# if num % 2 == 0:
#     print("입력한 숫자는 짝수입니다.")
# else:
#     print("입력한 숫자는 홀수입니다.")
