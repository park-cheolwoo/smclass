# for문 출력
for k in range(1,10):
    print(f"[ {k} 단 ]", end="\t")
print()
for i in range(2,10):
  # print(f"[ {i} 단 ]")
  for j in range(1,10):
    print(f"{j} X {i} = {j*i}",end="\t")
  print()


# 000
# 001
...
# 998
# 999

# for i in range(1,9+1):
#   print(f"00{i}")
# for j in range(10,99+1):
#   print(f"0{j}")
# for k in range(100,999+1):
#   print(f"{k}")

# a=1
# print(f"{a:03d}")

# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")


# #구구단 입력한 단까지 출력하시오.

# a = int(input("숫자를 입력하세요."))
# for i in range (a,a+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i}X{j}={i*j}")
#   print("-"*20)
