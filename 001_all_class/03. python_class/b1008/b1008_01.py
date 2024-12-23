students = []
no = 1
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
cnt = 0
kor = 0
eng = 0
math = 0

while True:
    print(" [ 학생성적 프로그램 ] ")
    print("-" * 60)
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("4.학생성적검색")
    print("5.학생성적삭제")
    print("6.등수처리")
    print("0.프로그램종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요.>>")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    if choice == "1":
        print(" [ 학생성적입력 ] ")
        while True:
            name = input("학생 이름을 입력하세요. (상위이동:0) >>")
            if name == "0":
                break
            kor = int(input("국어 성적을 입력하세요."))
            eng = int(input("영어 성적을 입력하세요."))
            math = int(input("수학 성적을 입력하세요."))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            s = [no, name, kor, eng, math, total, avg, rank]
            students.append(s)
            print(f"{name} 학생 성적이 입력되었습니다.")
            no += 1

    if choice == "2":
        print(" [학생 성적 출력] ")
        for st in s_title:
            print(st, end="\t")
        print()
        print("-" * 60)
        for s in students:
            print(
                f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
            )
        print()

    if choice == "3":
        cnt = 0
        print(" [ 학생성적수정 ] ")
        name = input("학생 이름을 입력하세요.")
        for s in students:
            if s[1] == name:
                cnt = 1
                print(f"{name} 학생을 찾았습니다.")
                print("1. 국어 성적 수정")
                print("2. 영어 성적 수정")
                print("3. 수학 성적 수정")
                choose = input("원하시는 번호를 입력하세요. >>")
                if choose == "1":
                    s[2] = int(input("수정하실 국어 점수를 입력하세요."))
                if choose == "2":
                    s[3] = int(input("수정하실 영어 점수를 입력하세요."))
                if choose == "3":
                    s[4] = int(input("수정하실 수학 점수를 입력하세요."))
                s[5] = s[2] + s[3] + s[4]
                s[6] = s[5] / 3
                print(f"{name} 학생 성적이 수정되었습니다.")

        if cnt == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요.")

    if choice == "4":
        cnt = 0
        name = input("학생 이름을 입력하세요.")
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                for st in s_title:
                    print(st, end="\t")
                print()
                print("-" * 60)
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t"
                )
                cnt = 1
        if cnt == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요.")

    if choice == "5":
        cnt = 0
        print(" [ 학생성적삭제 ] ")
        name = input("학생 이름을 입력하세요.")
        for idx, s in enumerate(students):
            if s[1] == name:
                cnt = 1
                yes = input(
                    f"{name} 학생 성적을 삭제하시겠습니까?(삭제시 복구 불가)(예:1, 아니오:0)"
                )
                if yes == "1":
                    del students[idx]
                    print(f"{name} 학생 성적이 삭제되었습니다.")
                elif yes == "0":
                    print("성적 삭제가 취소되었습니다.")
        if cnt == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요.")

    if choice == "6":
        print(" [ 등수처리 ] ")
        print("등수 처리를 시작합니다.")
        for s in students:
            count = 1
            for i in students:
                if s[5] < i[5]:
                    count += 1
            s[7] = count
        print("등수 처리가 완료되었습니다.")
