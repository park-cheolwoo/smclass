subName = ["국어","영어","수학"]
score = {"국어":100, "영어":95, "수학":80}
# print(score)

# print(score['국어'])
# print(score[subName[0]])

for k,v in score.items():
  print(f"{k} : {v}")


for i in subName:
  print(f"{i} : {score[i]}")


# #구구단을 출력하시오.
# def result(num1,num2):
#   for i in range(num1,num2+1): 
#     print(" [ {}단 ] ".format(i))
#     for j in range(1,9+1):   
#       print(f"{i} x {j} = {i*j}")
#     print("-"*60)


# nArr = [9,5,7]

# for a in nArr:
#   result(2,a)
#   print("-"*60)
# #2-5단
# result(2,5)
# #3-9단
# result(3,9)
# #5-8단
# result(5,8)