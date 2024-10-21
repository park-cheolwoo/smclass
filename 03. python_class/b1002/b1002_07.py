students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
    [4, "강감찬", 100, 90, 99],
    [5, "김구", 90, 90, 99],
]

#이름을 입력받아 같은 이름이 있으면 데이터 삭제 없으면 없습니다 출력
name = input("이름을 입력하세요.")
count = 0
for s in students:
  if s[1] == name:
    students.remove(s)
    print(f"{name}을(를) 삭제합니다.")
    count = 1
    break
if count==0:
  print("찾고자하는 이름이 없습니다.")

print("현재 학생성적 : ",students)

# for idx,s in enumerate(students):
#   if name == s[1]:
#     del students[idx]
# else:
#   print("없습니다.")





# all_list = [[1, "홍길동", 100], [2, "유관순", 200], [3, "이순신", 100]]

# #이름이 유관순인 것을 삭제
# # for s in all_list:
# #   if s[1] == "유관순":
# #     all_list.remove(s)
# for idx,s in enumerate(all_list):
#   if s[1] == "유관순":
#     del all_list[idx]

# print(all_list)

# aArr=[2,3,4,6,7,8,9,10]
# # 50,100 추가하시오
# aArr.append(50);aArr.append(100)
# print(aArr)
# # 2번자리에 30을 추가하시오
# aArr.insert(2,30)
# print(aArr)
# # 숫자 6을 삭제하시오
# aArr.remove(6)
# print(aArr)
# # index 0,3데이터를 삭제하시오
# del aArr[0];del aArr[3]
# print(aArr)