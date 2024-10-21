students = []
no = 1
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]


while True:
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

    if choice == "0":
        print(" [ 프로그램 종료 ] ")
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        print(" [ 학생 성적 입력 ] ")
        while True:
            name = input(f"{no}번째 이름을 입력하세요.(상위이동 : 0)")
            if name == "0":
                break
            kor = int(input("국어 점수를 입력하세요."))
            eng = int(input("영어 점수를 입력하세요."))
            math = int(input("수학 점수를 입력하세요."))
            total = kor + eng + math
            avg = total / 3
            rank = 0

            s = [no, name, kor, eng, math, total, avg, rank]
            print(s)
            students.append(s)
            no += 1

    elif choice == "2":
        print(" [ 학생 성적 출력 ] ")
        print()
        for s in s_title:
            print(s, end="\t")
        print()
        print("-" * 60)
        for i in students:
            print(
                f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]:.2f}\t{i[7]}\t"
            )

    elif choice == "3":
        # 수정은 검색과 비슷한 방식
        print(" [ 학생 성적 수정 ] ")
        # 홍길동, 유관순, 이순신
        # 유관순 학생 성적
        name = input("수정하고자 하는  학생 이름을 입력하세요.")
        count = 0
        # students 10명
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                print("[1. 국어 점수 수정]")
                print("[2. 영어 점수 수정]")
                print("[3. 수학 점수 수정]")
                print("[0. 과목 수정 취소]")
                choice = input("원하는 번호를 입력하세요.>>")
                if choice == "1":
                    print(f"현재 국어점수 : {s[2]}")
                    s[2] = int(input("변경 국어점수 입력 : "))
                elif choice == "2":
                    print(f"현재 영어점수 : {s[3]}")
                    s[3] = int(input("변경 영어점수 입력 : "))
                elif choice == "3":
                    print(f"현재 수학점수 : {s[4]}")
                    s[4] = int(input("변경 수학점수 입력 : "))
                elif choice == "0":
                    print("성적 수정을 취소합니다.")
                    count = 1

                # 점수가 수정되어도 합계, 평균이 다시 계산되지 않음
                if choice !=0:
                  s[5] = s[2] + s[3] + s[4]
                  s[6] = s[5] / 3
                  print(f"{name} 학생의 성적이 변경되었습니다.")

                count = 1
        # 학생이 없을 경우
        if count == 0:
            print("수정하고자 하는 학생 이름이 없습니다.")
            print()

    elif choice == "4":
        print(" [ 학생 성적 검색 ] ")
        name = input("찾고자 하는 학생 이름을 입력하세요.")
        count = 0
        # students 10명
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
                print()
                count = 1
                break
        if count == 0:
            print("찾고자 하는 학생 이름이 없습니다.")
            print()
