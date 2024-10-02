fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")  # 리스트
# print(fruits)
# print(len(fruits))

# 리스트 인 경우 검색해서 해당되는 index를 출력하시오.
# 배 에 해당되는 index 번호를 출력하시오.
search = input("과일 이름을 입력하세요.")

# idx=0
# for idx, s in enumerate(fruits):
#     if s == search:
#         print(f"{search}의 위치 : {idx}")
# -------------------- 텍스트 vs 리스트 비교 -----------------------------------
# idx = 0
# if fruit.count(search) > 0:
#     print(f"{search} 글자가 있습니다.")
#     for i in range(fruit.count(search)):
#         for i in range(idx, len(fruit)):
#             print(
#                 f"{search} 글자가 있는 위치 : ", fruit.find(search, idx)
#             )
#             idx = fruit.find(search, idx) + 1
#             break
# else:
#     print(f"{search}(이)라는 글자는 없습니다.")


# else:
#     print(f"{search} 이름이 없습니다.")


# print(fruit.find("배", 0)) #3
# print(fruit.find("배", fruit.find("배", 0) + 1)) #15
# print(fruit.find("배", (fruit.find("배", fruit.find("배", 0) + 1))+1)) #20

# print(fruit.find("딸기",0))
# print(fruit.find("딸기",(fruit.find("딸기", 0)+1)))
