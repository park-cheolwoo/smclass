# 숫자 맞히기 연습
import random

r_num = random.randint(1, 100)
count = 0

# for문


# for i in range(10):
#     print(f"{i+1}번째 도전입니다.")
#     ans = int(input("정답을 입력하세요."))
#     if r_num < ans:
#         print("정답은 입력하신 값보다 작습니다.")
#     elif r_num > ans:
#         print("정답은 입력하신 값보다 큽니다.")
#     else:
#         print(f"정답입니다. 정답은 {r_num}입니다.")
#         count = 1
#         break
# if count == 0:
#     print(f"10번 도전에 실패하셨습니다. 정답은 {r_num}입니다.")
# print("프로그램을 종료합니다.")


# while문

i = 0
while i < 10:
    print(f"{i+1}번째 도전입니다.")
    ans = int(input("정답을 입력하세요."))
    if r_num < ans:
        print("정답은 입력하신 값보다 작습니다.")
        i += 1
    elif r_num > ans:
        print("정답은 입력하신 값보다 큽니다.")
        i += 1
    else:
        print(f"정답입니다. 정답은 {r_num}입니다.")
        count = 1
        break

if count == 0:
    print(f"10번 도전에 실패하셨습니다. 정답은 {r_num}입니다.")
print("프로그램을 종료합니다.")
