import random

a_list = [0] * 20 + [1] * 5
aa_list = [
    ["로또", "로또", "로또", "로또", "로또"],
    ["로또", "로또", "로또", "로또", "로또"],
    ["로또", "로또", "로또", "로또", "로또"],
    ["로또", "로또", "로또", "로또", "로또"],
    ["로또", "로또", "로또", "로또", "로또"]
]
random.shuffle(a_list)
lotto = []
for i in range(0, len(a_list), 5):
    lotto.append(a_list[i : i + 5])

while True:
    my_money = int(input("얼마를 배팅하시겠습니까?"))
    aa_list = [
        ["로또", "로또", "로또", "로또", "로또"],
        ["로또", "로또", "로또", "로또", "로또"],
        ["로또", "로또", "로또", "로또", "로또"],
        ["로또", "로또", "로또", "로또", "로또"],
        ["로또", "로또", "로또", "로또", "로또"],
    ]
    # print(lotto)

    print("\t0\t1\t2\t3\t4")
    print("-" * 45)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(aa_list[i][j],end="\t")
        print()
    print("-"*45)
    input1 = list(map(int,input("좌표를 입력하세요. ex)0.0 >>").split(".")))

    if lotto[input1[0]][input1[1]] ==0:
        print(f"다음 기회에 - {my_money} 원")
    elif lotto[input1[0]][input1[1]] == 1:
        print(f"당첨 - 당첨금 : {my_money*10} 원")
