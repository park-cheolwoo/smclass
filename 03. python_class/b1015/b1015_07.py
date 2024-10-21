students = [
    {
        "no": 1,
        "name": "홍길동",
        "kor": 100,
        "eng": 100,
        "math": 99,
        "total": 299,
        "avg": 99.67,
        "rank": 0,
    },
    {
        "no": 2,
        "name": "유관순",
        "kor": 80,
        "eng": 80,
        "math": 85,
        "total": 245,
        "avg": 81.67,
        "rank": 0,
    },
    {
        "no": 3,
        "name": "이순신",
        "kor": 90,
        "eng": 90,
        "math": 91,
        "total": 271,
        "avg": 90.33,
        "rank": 0,
    },
    {
        "no": 4,
        "name": "강감찬",
        "kor": 60,
        "eng": 65,
        "math": 67,
        "total": 192,
        "avg": 64.00,
        "rank": 0,
    },
    {
        "no": 5,
        "name": "김구",
        "kor": 100,
        "eng": 100,
        "math": 84,
        "total": 284,
        "avg": 94.67,
        "rank": 0,
    },
]

stu = "6,홍길자,100,100,100,300,100.0,0"
sArr = stu.split(",")







# s="11"
# print(str.isdigit(s)) #문자열이 숫자이면 True, 아니면 False
# ss="a"
# print(str.isdigit(ss))





# 문자열 >> 리스트 >> 타입 변경
for i,s in enumerate(sArr):
    if str.isdigit(s): #int타입 변경이 가능한지?
        sArr[i] = int(s)
sArr[6] = float(sArr[6])

students.append(sArr)
print(students)
# print(sArr)
# stu_1 = "6,홍길자,100,100,100,300,100.0,0"
# key_1 = ["no","name","kor","eng","math","total","avg","rank"]
# sArr = stu_1.split(",")
# print(sArr)

# # 딕셔너리 생성방법
# dict_1 = {"no": int(sArr[0]), "name": sArr[1], "kor": int(sArr[2]), "eng": int(sArr[3]),"kor":int(sArr[2])"kor":int(sArr[2])"kor":int(sArr[2])}
# print(dict_1)
# # zip
# dict_list = dict(zip(key_1,sArr))
# print(dict_list)
