import stu_func

while True:
    choice = stu_func.main_print()
    if choice == "1":
        stu_func.stu_insert()
    elif choice == "2":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
        sql = stu_func.stu_output(sql)
    elif choice == "3":
        stu_func.stu_search()
    elif choice == "4":
        stu_func.stu_update()
    elif choice == "5":
        stu_func.stu_sort()
    elif choice == "6":
        stu_func.stu_rank()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
