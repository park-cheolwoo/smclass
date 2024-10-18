import random


fruit = {
    "바나나": "banana",
    "오렌지": "orange",
    "체리": "cherry",
    "파인애플": "pineapple",
    "코코넛": "coconut",
}
fName = list(fruit.keys())
# fName = ["바나나","오렌지","체리","파인애플","코코넛"]
print(fName)


#fName 랜덤순서로 영문퀴즈 시작
re_fName = random.sample(fName,5)
# print(re_fName)
# for i in re_fName:
#   search = input(f"{i}의 영문을 입력하세요.")
#   if fruit[i] == search:
#     print("정답")
#   else:
#     print("오답")

# 바나나를 입력하면 영어로 banana 출력


#fName 순서대로 영문퀴즈 시작
# print("[영단어 맞추기]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요.")
#   if fruit[key] == search:
#     print("정답")
#   else:
#     print("오답")