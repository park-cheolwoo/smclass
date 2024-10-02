fruit = []

while True:
    # strip : 앞쪽 여백, 뒤쪽 여백 제거
    # '사  과' -> '사  과'
    # replace(" ","") : 가운데 여백 제거(문자 대체)
    search = input("과일 이름을 입력하세요.(종료 : X)").replace(" ","")
    if search == "x":
        break

    if search in fruit:
        print("같은 과일이 있습니다.")
    else:
        print(f"{search}을(를) 추가합니다.")
        fruit.append(search)
        print(fruit)
# 반복문을 종료할 때 : break
# while True:
#   break

# print("프로그램 종료")

# 무한반복문은 while True 입력
# a=0
# while True: #무한반복
#   print(a)
#   a += 1

# while (a<10):
#   a += 1
#   print(a)

# print("프로그램 종료")
