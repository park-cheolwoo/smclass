# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수 확인
# find - 데이터가 있는 위치 확인, 없으면 -1  find(찾을 문자, 시작idx, 끝idx)
# index - 데이터가 있는 위치 확인, 없으면 에러

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는 위치를 모두 출력하시오.
search = input("과일 이름을 입력하세요.")
print("모든 글자 : ",fruit)

idx = 0
if fruit.count(search) > 0:
    print(f"{search} 글자가 있습니다.")
    for i in range(fruit.count(search)):
        for i in range(idx, len(fruit)):
            print(f"{search} 글자가 있는 위치 : ",fruit.find(search,idx)) #find(찾을 문자, 시작idx, 끝idx)
            idx = fruit.find(search,idx) + 1
            break
else:
    print(f"{search}(이)라는 글자는 없습니다.")


# # 과일 이름을 입력받아 과일 이름이 있으면 있습니다. 과일검색개수 : 없으면 없습니다. 출력
# txt = input("과일 이름을 입력하세요.")
# if txt in fruit:
#     print(f"{txt}라는 이름이 있습니다.")
#     print(f"과일 검색 개수 : {fruit.count(txt)}")
# else:
#     print(f"{txt}라는 이름이 없습니다.")
#     # print(fruit.index(txt)) # 배 가 있는 위치의 index, txt가 리스트 안에 없으면 에러
#     print(fruit.find(txt))  # 배 가 있는 위치의 index, txt가 리스트 안에 없으면 -1 출력

# # count : 문자열 내에 해당 숫자개수 확인
# # print(fruit.count('사과'))


# fruit = ['사과', '배', '딸기', '포도','복숭아','배','사과','배','딸기']
# # count : 리스트에서 개수 확인
# print(fruit.count('배'))
# print(fruit.count('사과'))
# 글자를 입력받아 입력한 과일이 있으면 있어요. 없어요.
# txt = input("과일을 입력하세요.")
# if txt in fruit:
#   print("있어요.")
# else:
#   print("없어요.")


# fruit = "사과, 배,딸기, 포도"
# if '배' in fruit:
#   print("배라는 글자가 있어요.")
# else:
#   print("배라는 글자가 없어요.")


# if '배' in fruit:  #1번의 비교로 있는지 확인
#   print("배가 있어요.")
# else:
#   print("배가 없어요.")
