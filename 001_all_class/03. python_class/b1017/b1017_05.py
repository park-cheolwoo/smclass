students = []
subjects = ["번호","이름","국어","영어","수학","합계","평균","등수"]
sub = ["no","name","kor","eng","math","total","avg","rank"]

f = open("b1017/stu_data.txt",'r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  s = line.strip().split(",")
  for idx,i in enumerate(s):
    # enumerate >> s = [idx=0,i=1 m idx=1,i="홍길동", .....]
    # [1, '홍길동', 94, 73, 54, 221, 73.6666666667, 1]
    if idx == 1:continue
    elif idx == 6: s[6]=float(i)
    else:s[idx] = int(i)
  students.append(dict(zip(sub,s)))
  print(students)
