students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
]

# print(students)  # 한번에 모두 출력

# for s in students:  # 한개씩 가져와서 출력
#     print(s)

# 이름이 유관순인 것을 출력하시오.

# for s in students:  # s : 리스트
#     if s[1] == "유관순":
#         print(s)

# students에 ss 추가
ss = [4, "강감찬", 100, 90, 99]
students.append(ss)

# 값이 2개 이상 저장하려면, 주소값 저장
# 이순신인 데이터를 삭제
# for s in students:
#   if s[1]=="이순신":
#     students.remove(s) #remove
for idx,s in enumerate(students):
  if s[1]=="이순신":
    del students[idx] #del


print(students)
