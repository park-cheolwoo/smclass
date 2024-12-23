# 2차원 리스트
# for문을 2번 작성해서 1~25 5,5 리스트 생성

a_list = []
for i in range(0, 4 + 1):
    a = []
    for j in range(1, 5 + 1):
        a.append(5 * i + j)
    a_list.append(a)
print(a_list)


# a_list = [] #a_list[0],a_list[1],...
# for i in range(9):
#   a_list.append(i+1)

# b_list = []
# for i in range(9):
#   b = []
#   if (a_list[i]%4)==0:
#     b.append(a_list[i])
#   elif (a_list[i]%4)==1:


# 3,3리스트 [1,2,3],[4,5,6],[7,8,9]

# a_list = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# 1~9까지 1차원 리스트 추가하시오
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)

# 1~9까지 2차원 리스트 추가하시오
# b_list = []
# for i in range(0,3):
#   a = []
#   for j in range(0,3):
#    a.append(3*i+j+1)
#   b_list.append(a)
# print(b_list)


# a_list =[
#   [1,2],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# #2차원 리스트 -> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)
