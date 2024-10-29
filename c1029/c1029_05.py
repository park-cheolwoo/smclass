title = ["e_id", "e_name", "salary"]
a = [196, "Alana Walsh", 3100.0]
aa = [
    (196, "Alana Walsh", 3100.0),
    (125, "Julia Nayer", 3200.0),
    (180, "Winston Taylor", 3200.0),
    (194, "Samuel McCain", 3200.0),
    (138, "Stephen Stiles", 3200.0)
]
a_list = [] 
for i in aa:
    print(dict(zip(title, i)))
    a_list.append(dict(zip(title, i)))
print(a_list)
aa_list = list(map(dict, zip(title, aa)))
print(aa_list)
# select * from employees where emp_name like '%a%'

# name = '홍길동'
# # 문자변수 출력
# print('안녕하세요. 이름은 %s'%name)
# # format 함수
# print('hello my name is {}'.format(name))
# # 문자 f함수
# print(f'hello my name is {name}')


# a=1
# b=2

# a_list = [a,b]
# print(a_list)
# print(type(a_list))
# print(tuple(a_list))


# 튜플을 1개만 지정할 때에는 뒤에 ,를 넣어야 함.
# a_tuple = (a,b)
# print(type(a_tuple))
# # b_tuple = (b) # 타입이 int 타입
# b_list = [b]
# print(type(b_tuple))
# print(type(tuple(b_list)))
