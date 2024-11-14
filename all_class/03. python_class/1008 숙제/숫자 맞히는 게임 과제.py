import random

r_num = random.randint(1, 100)  # 1~100까지 무작위 숫자
count = 0  # 정답 체크
a_list = []  # 입력한 정답 리스트

beting = int(input("게임에 참여하시려면 게임 금액을 입력하세요."))

for i in range(1, 10 + 1):
    print(f"{i}번째 도전입니다.")  # i = 1~10
    ans = int(input("1~100 사이의 숫자(정답)를 입력하세요."))
    if ans < r_num:
        print("정답은 입력하신 수보다 큽니다.")
        a_list.append(ans)
    elif ans > r_num:
        print("정답은 입력하신 수보다 작습니다.")
        a_list.append(ans)
    elif ans == r_num:
        count = 1
        print(f"정답입니다. 정답은 {r_num}입니다.")
        print(f"당첨금은 {beting*3}입니다.")


if count == 0:
    print("10번 도전에 실패하셨습니다.")
    print(f"정답은 {r_num}입니다.")
    print(f"입력하신 값은 {a_list}입니다.")
    print(f"게임 금액 {beting} 를 잃으셨습니다.")