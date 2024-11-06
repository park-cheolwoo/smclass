import random


def random_pw():
    a = random.randint(0, 10000)  # 0-9999 까지
    ran_num = f"{a:04}"  # 0124,5412,0001
    print("랜덤번호 : ", ran_num)
    return ran_num

random_pw()