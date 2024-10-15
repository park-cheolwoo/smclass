# import S_function
from S_function import *

# 학생 성적 처리 변수
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]  # 전역변수
flag = 0  # 성적처리
no = 0
name = ""
kor = 0
eng = 0
math = 0
total = 0
avg = 0
rank = 0  # 성적처리변수
# ----------------------------------------------------------------

# 프로그램 시작
choice = title_program()
if choice == "1":
    stuNo = stu_input(stuNo, students)
elif choice == "2":
    stu_output(students)
elif choice == "3":
    stu_update(students)
elif choice == "4":
    stu_search(students)
elif choice == "5":
    stu_delete(students)
elif choice == "6":
    stu_rank(students)
elif choice == "7":
    stu_sort(students)
elif choice == "0":
    print("프로그램을 종료합니다.")
# ----------------------------------------------------------------
