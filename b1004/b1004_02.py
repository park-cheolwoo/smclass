import random

# 랜덤 숫자 : 1-100
r_num = random.randint(1,100)

#10번 도전에서 입력한 숫자가 더 크면 "작은 수를 입력하셔야합니다."
#입력한 숫자보다 더 작으면 "큰 수를 입력하셔야합니다."
#10번 도전에서 맞히지 못하면 "10번 도전에 실패했습니다. 랜덤숫자 : "
#도전에 성공했습니다. 랜덤숫자 : 

count = 0
for i in range(10):
  ans = int(input("1부터 100까지의 숫자를 입력하세요."))
  if r_num < ans:
    print("작은 수를 입력하셔야 합니다.")
  elif r_num > ans :
    print("큰 수를 입력하셔야 합니다.")
  else:
    print(f"정답입니다. 랜덤숫자 : {r_num}")
    count = 1
    break
if count == 0:
  print(f"10번 도전에 실패하셨습니다. 랜덤숫자 : {r_num}")