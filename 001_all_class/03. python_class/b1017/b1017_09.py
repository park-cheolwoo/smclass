import os

f = open("b1017/stu_data.txt",'r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  print(line.strip())

# if os.path.isfile("b1017/stu_data.txt"):
#   print("파일이 있습니다.")
# else: print("파일이 없습니다.")