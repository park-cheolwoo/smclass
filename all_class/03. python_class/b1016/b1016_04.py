member = [
    {
        "id": "aaa",
        "pw": "1111",
        "name": "홍길동",
        "nicName": "길동스",
        "address": "서울시",
        "money": 1000000000,
    },
    {
        "id": "bbb",
        "pw": "2222",
        "name": "유관순",
        "nicName": "관순스",
        "address": "부산시",
        "money": 700000000,
    },
    {
        "id": "ccc",
        "pw": "3333",
        "name": "이순신",
        "nicName": "순신스",
        "address": "경기도",
        "money": 500000000,
    },
    {
        "id": "ddd",
        "pw": "4444",
        "name": "강감찬",
        "nicName": "감찬스",
        "address": "인천시",
        "money": 100000000,
    },
    {
        "id": "admin",
        "pw": "5555",
        "name": "김구",
        "nicName": "김스",
        "address": "대구시",
        "money": 200000000,
    },
]

# member.txt 파일 생성해서 내용 저장
f = open('member.txt','w',encoding='utf-8')
for i in member:
    f.write(f"{i["id"]},{i["pw"]},{i["name"]},{i["nicName"]},{i["address"]},{i["money"]}\n")
f.close()


# students = [
#     {
#         "no": 1,
#         "name": "홍길동",
#         "kor": 100,
#         "eng": 100,
#         "math": 99,
#         "total": 299,
#         "avg": 99.67,
#         "rank": 0,
#     },
#     {
#         "no": 2,
#         "name": "유관순",
#         "kor": 80,
#         "eng": 80,
#         "math": 85,
#         "total": 245,
#         "avg": 81.67,
#         "rank": 0,
#     },
#     {
#         "no": 3,
#         "name": "이순신",
#         "kor": 90,
#         "eng": 90,
#         "math": 91,
#         "total": 271,
#         "avg": 90.33,
#         "rank": 0,
#     },
#     {
#         "no": 4,
#         "name": "강감찬",
#         "kor": 60,
#         "eng": 65,
#         "math": 67,
#         "total": 192,
#         "avg": 64.00,
#         "rank": 0,
#     },
#     {
#         "no": 5,
#         "name": "김구",
#         "kor": 100,
#         "eng": 100,
#         "math": 84,
#         "total": 284,
#         "avg": 94.67,
#         "rank": 0,
#     },
# ]

# f = open("students.txt", "w", encoding="utf-8")
# for i in students:
#     f.write(
#         f"{i['no']},{i['name']},{i['kor']},{i['eng']},{i['math']},{i['total']},{i['avg']},{i['rank']}\n"
#     )
# f.close()
