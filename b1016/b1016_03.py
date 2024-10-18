# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0}
#             ]
students = []
stu_key = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]
f = open("a.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    s = line.strip().split(",")
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3])
    s[4] = int(s[4])
    s[5] = int(s[5])
    s[6] = float(s[6])
    s[7] = int(s[7])
    # for i,v in enumerate(s):
    #     if i == 1: continue
    #     elif i == 6: v = float(v)
    #     else: v = int(v)
    students.append(dict(zip(stu_key, s)))
f.close()
print(students)


# a = ["홍길동","유관순","이순신"]
# b = [100,90,80]

# c=zip(a,b)
# print(dict(c))
