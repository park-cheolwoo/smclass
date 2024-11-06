import stu_func

while True:
    choice = stu_func.main_print()
    if choice == "1":
        stu_func.stu_insert()
    elif choice == "2":
        stu_func.stu_output()
    elif choice == "3":
        stu_func.stu_select()
    elif choice == "4":
        stu_func.stu_update()
    elif choice == "5":
        stu_func.stu_sort()
    elif choice == "6":
        stu_func.stu_rank()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
