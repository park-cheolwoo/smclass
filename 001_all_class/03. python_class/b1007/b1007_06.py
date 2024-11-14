import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.

a_list = [0] * 20 + [1] * 5
random.shuffle(a_list)
# print(a_list)

#[5,5] 2차원 리스트에 a_list의 값을 입력한 후 출력하시오.
b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[i*5+j]) #a_list 5개를 리스트에 추가
  b_list.append(a)
print(b_list)

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*60)
  for i in range(5):
    print(i,end='\t')
    for j in range(5):
      print(b_list[i][j],end="\t")
    print()
          
  num = input("좌표를 입력하세요. ex) 0,0 >>")
  num2 = list(map(int,num.split(",")))
  print(num2)
  print(f"좌표값 : {b_list[num2[0]][num2[1]]}")



# b_list = []
# for i in range(0,len(a_list),5):
#   b_list.append(a_list[i:i+5])
# print(b_list)

# print("\t0\t1\t2\t3\t4")
# print("-"*60)
# for i in range(5):
#   print(i,end="\t")
#   for j in range(5):
#    print(b_list[i][j],end="\t")
#   print()




# 0-20개, 1-5개 생성
# a_list = []
# for i in range(25):
#   if i<20:
#     a_list.append(0)
#   else:
#     a_list.append(1)
