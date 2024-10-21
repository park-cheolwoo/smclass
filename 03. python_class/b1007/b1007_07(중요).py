import random

lotto = [0] * 6 + [1] * 3
random.shuffle(lotto)
aa_list = [["로또", "로또", "로또"], ["로또", "로또", "로또"], ["로또", "로또", "로또"]]
a_list = []

for i in range(0, len(lotto), 3):
    a_list.append(lotto[i : i + 3])

# print(a_list)

while True:
    my_money = int(input("얼마를 투자하시겠습니까?"))
    aa_list = [
        ["로또", "로또", "로또"],
        ["로또", "로또", "로또"],
        ["로또", "로또", "로또"],
    ]

    print("        [ i,j 좌표 ] ")
    print("\t0\t1\t2")
    print("-" * 30)
    for i in range(3):
        print(i, "|", end="\t")
        for j in range(3):
            print(aa_list[i][j], end="\t")
        print()

    num = list(map(int, input("좌표를 입력하세요. ex)0.0 >>").split(".")))
    # print("좌표값 : ", a_list[num[0]][num[1]])
    if a_list[num[0]][num[1]] == 0:
        print(f"다음 기회에 - {my_money} 원")
        aa_list[num[0]][num[1]] = "꽝"
    elif a_list[num[0]][num[1]] == 1:
        aa_list[num[0]][num[1]] = "당첨"
        print(f"당첨 - 당첨금 : {my_money*10} 원")
