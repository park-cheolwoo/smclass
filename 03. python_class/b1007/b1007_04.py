import random

# 1~25 사이의 랜덤숫자 생성 출력

# num = random.random()*25+1
# num2 = random.randint(1,25)


# 1~25번까지 랜덤숫자 입력, 중복은 제거하고 출력
# a_list = []
# while len(a_list)<25:
#   for i in range(25):
#     num = random.randint(1,25)
#     if num not in a_list:
#       a_list.append(num)
# print(a_list)
# print(len(a_list))


# 1~25번까지 랜덤 배치 - random.choices()
# 범위 리스트, 25개 추출(중복추출 가능.)
a_list = []
for i in range(25):
    a_list.append(i + 1)
b_list = random.choices(a_list,k=25)
print(b_list)


# 1~25번까지 랜덤 배치 - random.sample()
# 범위 리스트, 25개 추출(중복추출 안됨.)
# b_list = random.sample(a_list, 25)
# print(b_list)
