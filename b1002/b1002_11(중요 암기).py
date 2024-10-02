students = [
    [1, "홍길동", 100, 100, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
    [4, "강감찬", 100, 90, 99],
    [5, "김구", 90, 90, 99],
]

#합계, 평균 추가
for s in students:
  total = s[2]+s[3]+s[4]
  avg = total/3
  s.append(total)
  s.append(avg)
print(students)



search = input("찾고자 하는 학생 이름을 입력하세요.")
cnt = 0
for s in students:
  if s[1] == search:
    print("찾는 학생이 있습니다.")
    cnt = 1
    break
  #if-else 구문 사용하면 문구가 5번 출력됨
if cnt ==0 :
  print("찾는 학생이 없습니다.")
#   #찾는 학생이 있으면 찾는 학생 이름이 있습니다.
#   #없으면 찾는 학생이 없습니다.