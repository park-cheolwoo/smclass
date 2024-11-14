import random

# 랜덤 숫자 생성 - random
# random() : 0 <= x < 1 실수값을 추출

print(random.random())
print(int(random.random() * 10))  # 0~9
print(int((random.random()) * 10)+1)  # 1~10

#랜덤 int 추출 - 1,10까지(10 포함)
print(random.randint(1,10))

#랜덤 범위 추출 - 1,2사이(2 포함 안됨)
print(random.randrange(1,2))

#choice - 리스트에서 랜덤 추출
a = [1,4,5,9]
print(random.choice(a))

#choices - 리스트에서 여러개 랜덤 추출 (중복 가능)
print(random.choices(a,k=2))

#sample - 리스트에서 여러개 랜덤 추출 (중복 불가)
print(random.sample(a,k=2))