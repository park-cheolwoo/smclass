import random

# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다. 출력
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다. 출력
# 맞추면 정답입니다 출력 + 프로그램 종료
# 10번 도전하도록 하시오.


# for문


r_num = random.randint(0, 100)  # 100포함
count = 0
for i in range(10):
    print(f"{i+1}번째 도전입니다.")
    answer = int(input("0부터 100까지의 숫자를 입력하세요."))
    if r_num < answer:
        print("정답은 입력한 숫자보다 작습니다.")
    elif r_num > answer:
        print("정답은 입력한 숫자보다 큽니다.")
    elif answer == r_num:
        print(f"정답입니다. 정답은 {r_num} 입니다.")
        count = 1
        break
if count == 0:
    print(f"10번 도전에 실패하셨습니다. 정답은 {r_num}입니다.")

print("프로그램을 종료합니다.")


# while문


# i = 0  # 초기값
# count=0
# answer = input("0부터 100까지의 숫자를 입력하세요.") #str >> int 타입으로 변경 // while문 밖에 있으면 정답이 1번만 입력됨
# while i < 10:  # 조건식
#     print(f"{i+1}번째 도전입니다.")
#     answer = int(input("0부터 100까지의 숫자를 입력하세요."))
#     # r_num = random.randint(1,100) #while 돌 때마다 랜덤숫자가 변경됨 >> while문 밖에 있어야함
#     if r_num < answer:
#         print("정답은 입력한 숫자보다 작습니다.")
#         i += 1  # 증감식
#     elif r_num > answer:
#         print("정답은 입력한 숫자보다 큽니다.")
#         i += 1
#     elif answer == r_num:
#         print(f"정답입니다. 정답은 {r_num} 입니다.")
#         count = 1
#         break
# #10번 도전해서 실패할 경우
# if count==0:
#     print(f"10번 도전에 실패하셨습니다. 정답번호는 {r_num} 입니다.")

# print("프로그램을 종료합니다.")
