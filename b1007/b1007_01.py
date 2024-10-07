students = []
choice = 0  # 전역변수
stuNo = 0
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no = 1
name = ""
kor = 0
eng = 0
math = 0
total = 0
avg = 0
rank = 0
# 성적처리변수
count = 1
chk = 0
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]


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

    if choice == "1":
        print(" [ 학생성적입력 ] ")
        # 학생성적 직접입력
        while True:
            stuNo = len(students)
            no = stuNo + 1  # 리스트 - 학생 수
            name = input(f"{no}번째 학생 이름을 입력하세요.(0. 취소)>>")
            if name == "0":
                print("성적 입력을 취소합니다.")
                print()
                break
            kor = int(input("국어 점수를 입력하세요."))
            eng = int(input("영어 점수를 입력하세요."))
            math = int(input("수학 점수를 입력하세요."))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            students.append([no, name, kor, eng, math, total, avg, rank])
            print(f"{name} 학생 성적이 저장되었습니다.")

    elif choice == "2":
        print("                     [ 학생성적출력 ] ")
        # 상단 타이틀 출력
        for title in s_title:
            print(f"{title}\t", end="")
        print()
        print("-" * 60)
        # 학생 출력
        for s in students:
            print(
                f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t",
                end="",
            )
            print()

    elif choice == "3":
        print(" [ 학생성적수정 ] ")
        chk = 0
        name = input("수정하고싶은 학생 이름을 입력하세요.")
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                print(" [ 수정하고자 하는 과목 선택 ] ")
                print("1. 국어 점수")
                print("2. 영어 점수")
                print("3. 수학 점수")
                choose = input("과목을 선택하세요 >>")
                if choose == "1":
                    s[2] = int(input("수정할 국어 점수를 입력하세요."))
                if choose == "2":
                    s[3] = int(input("수정할 영어 점수를 입력하세요."))
                if choose == "3":
                    s[4] = int(input("수정할 수학 점수를 입력하세요."))
                s[5] = s[2] + s[3] + s[4]
                s[6] = s[5] / 3
                s[7] = 0
                chk = 1
                print(f"{name} 학생 성적이 수정되었습니다.")
            # 모든 학생 비교가 끝난 후 chk 확인
            if chk == 0:
                print("찾고자 하는 학생이 없습니다. 다시 입력하세요.")

    elif choice == "4":
        print(" [ 학생성적검색 ] ")
        chk = 0
        name = input("찾고자하는 학생 이름을 입력하세요.(0.취소)")
        if name == "0":
            print("성적 검색을 취소합니다.")
            print()
            break
        for s in students:
            if s[1] == name:
                print(f"{name} 학생을 찾았습니다.")
                for title in s_title:
                    print(f"{title}\t", end="")
                print()
                print("-" * 60)
                # 학생 출력
                print(
                    f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t",
                    end="",
                )
                print()
                chk = 1
        # 모든 학생 비교가 끝난 후 chk 확인
        if chk == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")

    elif choice == "5":
        print(" [ 학생성적삭제 ] ")
        chk = 0
        name = input("삭제하고싶은 학생 이름을 입력하세요.")
        for idx, s in enumerate(students):
            if s[1] == name:
                chk = 1
                choose = input(
                    f"{name} 학생 성적을 삭제하시겠습니까?(삭제시 복구 불가)\n1. 삭제 2. 취소"
                )
                if choose == "1":
                    del students[idx]
                    print("{} 학생을 삭제하셨습니다.".format(name))
                elif choose == "2":
                    print("성적 삭제가 취소되었습니다.")
                    break
        if chk == 0:
            print("{} 학생을 찾지 못했습니다. 다시 입력해주세요.".format(name))

    elif choice == "6":
        print(" [ 등수처리 ] ")
        for s in students:
            count = 1
            for st in students:
                if s[5] < st[5]:
                    count += 1
                s[7] = count  # 등수 입력
        print("등수처리가 완료되었습니다.")
        print()

    elif choice == "0":
        print(" [ 프로그램종료 ] ")
        print("프로그램을 종료합니다.")
        break
