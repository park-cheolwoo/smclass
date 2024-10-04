students = []
no = 1
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]


while True:
    count = 0
    print("[ 학생 성적 프로그램 ]")
    print("-" * 60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 검색")
    print("5. 학생 성적 삭제")
    print("6. 등수 처리")
    print("0. 프로그램 종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요.(종료 : 0)>>")


# 여기서부터 시작

    if choice == "0":
        print(" [ 프로그램 종료 ] ")
        print("프로그램을 종료합니다.")
        break

    if choice == "1":
        while True:
            name = input(f"{no}번째 학생 이름을 입력하세요.(상위이동 : 0)")
            if name == "0":
                break
            kor = int(input("국어 점수를 입력하세요."))
            eng = int(input("영어 점수를 입력하세요."))
            math = int(input("수학 점수를 입력하세요."))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            s = [no, name, kor, eng, math, total, avg, rank]
            students.append(s)
            print(
                f"번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {total}, 평균 : {avg:.2f}, 등수 : {rank}"
            )
            no += 1

    if choice == "2":
        print(" [ 학생 성적 출력 ] ")
        for s in s_title:
            print(s, end="\t")
            print()
            print("-" * 60)
        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")

    if choice == "3":
        name = input("찾고자 하는 학생 이름을 입력하세요.")
        for s in students:
            if name == s[1]:
                print(f"{name} 학생을 찾았습니다.")
                print("[1. 국어 점수 수정]")
                print("[2. 영어 점수 수정]")
                print("[3. 수학 점수 수정]")
                print("[0. 수정 취소]")
                choose = input("원하시는 번호를 선택하세요.>>")
                if choose == "1":
                    print(f"현재 국어 점수 : {s[2]}")
                    s[2] = int(input("수정할 국어 점수를 입력하세요."))
                elif choose == "2":
                    print(f"현재 영어 점수 : {s[3]}")
                    s[3] = int(input("수정할 영어 점수를 입력하세요."))
                elif choose == "3":
                    print(f"현재 수학 점수 : {s[4]}")
                    s[4] = int(input("수정할 수학 점수를 입력하세요."))
                elif choose == "0":
                    print("수정이 취소되었습니다.")
                    break

                print("수정이 완료되었습니다.")
                s[5] = s[2] + s[3] + s[4]
                s[6] = total / 3
                count = 1
        if count == 0:
            print("찾고자 하는 학생 이름이 없습니다.")

    if choice == "4":
        name = input("찾고자 하는 학생 이름을 입력하세요.")
        for s in students:
            if name == s[1]:
                print(f"{name} 학생을 찾았습니다.")
                for st in s_title:
                    print(st, end="\t")
                print()
                print("-" * 60)

                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}"
                )
                count = 1
        if count == 0:
            print("찾고자 하는 학생 이름이 없습니다.")

    if choice == "5":
        name = input("삭제시키고자 하는 학생 이름을 입력하세요.")
        for s in students:
            if name == s[1]:
                students.remove(s)
                print(f"{name} 학생을 삭제하였습니다.")
                count = 1
        if count == 0:
            print("찾고자 하는 학생 이름이 없습니다.")