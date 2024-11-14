# students 리스트 타입
students = [
    {
        "no": 1,
        "name": "홍길동",
        "kor": 100,
        "eng": 100,
        "math": 99,
        "total": 299,
        "avg": 99.67,
        "rank": 0,
    },
    {
        "no": 2,
        "name": "유관순",
        "kor": 80,
        "eng": 80,
        "math": 85,
        "total": 245,
        "avg": 81.67,
        "rank": 0,
    },
    {
        "no": 3,
        "name": "이순신",
        "kor": 90,
        "eng": 90,
        "math": 91,
        "total": 271,
        "avg": 90.33,
        "rank": 0,
    },
    {
        "no": 4,
        "name": "강감찬",
        "kor": 60,
        "eng": 65,
        "math": 67,
        "total": 192,
        "avg": 64.00,
        "rank": 0,
    },
    {
        "no": 5,
        "name": "김구",
        "kor": 100,
        "eng": 100,
        "math": 84,
        "total": 284,
        "avg": 94.67,
        "rank": 0,
    },
]
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]  # 전역변수
choice = 0  # 전역변수
flag = 0  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no = 0
name = ""
kor = 0
eng = 0
math = 0
total = 0
avg = 0
rank = 0  # 성적처리변수


# 메뉴 출력 함수 시작
def title_program():
    print("[ 학생성적프로그램 ]")
    print("-" * 60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적검색")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("7. 학생성적정렬")
    print("0. 프로그램 종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
    return choice  # 일반매개변수는 return을 해줘야함


# ------------------------------------------------------------------------------
# 학생 성적 입력 함수 시작
def stu_input(stuNo, students):
    while True:
        print(" [ 학생성적입력 ] ")
        # 학생성적 직접입력
        stuNo = len(students)
        no = stuNo + 1  # 리스트 - 학생 수
        name = input(f"{no}번째 학생 이름을 입력하세요.(0. 이전화면)>>")
        if name == "0":
            print("이전 화면으로 이동합니다.")
            print()
            break
        kor = int(input("국어 점수를 입력하세요."))
        eng = int(input("영어 점수를 입력하세요."))
        math = int(input("수학 점수를 입력하세요."))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        ss = {
            "no": no,
            "name": name,
            "kor": kor,
            "eng": eng,
            "math": math,
            "total": total,
            "avg": avg,
            "rank": rank,
        }
        students.append(ss)
        print(f"{name} 학생 성적이 저장되었습니다.")
    return stuNo


# ------------------------------------------------------------------------------
# 학생 성적 출력 함수 시작
def stu_output(students):
    print(" [ 학생성적출력 ] ")
    print()
    # 상단 출력
    for st in s_title:
        print(st, end="\t")
    print()
    print("-" * 60)

    # 학생 성적 출력
    for s in students:
        print(
            f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t"
        )
    print()


# ------------------------------------------------------------------------------
# 학생 성적 수정 함수 시작
def stu_update(students):
    print(" [ 학생성적수정 ] ")
    flag = 0
    name = input("학생 이름을 입력하세요. >> ")

    # 전체 학생과 비교
    for s in students:
        if name == s["name"]:
            print(f"{name} 학생을 찾았습니다.")
            print(" [ 수정 과목 선택 ] ")
            print("1. 국어 성적 수정")
            print("2. 영어 성적 수정")
            print("3. 수학 성적 수정")
            choice = input("원하시는 번호를 입력하세요. >>")
            if choice == "1":
                print(f"이전 국어점수 : {s['kor']}")
                s["kor"] = int(input("수정하실 국어 점수를 입력하세요."))
            elif choice == "2":
                print(f"이전 영어점수 : {s['eng']}")
                s["eng"] = int(input("수정하실 영어 점수를 입력하세요."))
            elif choice == "3":
                print(f"이전 수학점수 : {s['math']}")
                s["math"] = int(input("수정하실 수학 점수를 입력하세요."))
            s["total"] = s["kor"] + s["eng"] + s["math"]
            s["avg"] = s["total"] / 3
            flag = 1
            print(f"{name} 학생 성적이 수정되었습니다.")

            # 수정된 학생 성적 출력
            stu_output([s])
            # 학생 출력함수 재사용 - students는 리스트 타입, s는 딕셔너리 타입이므로 리스트 타입으로 변경

    if flag == 0:  # 학생이 검색되지 않았을 때
        print(f"{name} 학생을 찾지 못했습니다.")


# ------------------------------------------------------------------------------
# 학생 성적 검색 함수 시작
def stu_select(students):
    while True:
        print(" [ 학생성적검색 ] ")
        flag = 0
        name = input("학생 이름을 입력하세요.(0. 이전화면)>>")
        if name == "0":
            print("이전 화면으로 이동합니다.")
            print()
            break
        sArr = []
        for s in students:
            if s["name"].find(name) != -1:
                # print(f"{idx} 번째,{s["name"]} 학생을 찾았습니다.")
                sArr.append(s)
                flag = 1
        if flag == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
        else:
            print(f"{name} 이름으로 {len(sArr)}명의 학생이 검색되었습니다.")
            stu_output(sArr)


# ------------------------------------------------------------------------------
# 학생 성적 삭제 함수 시작
def stu_delete(students):
    print(" [ 학생성적삭제 ] ")
    flag = 0
    # sArr = []
    name = input("찾고자 하는 학생 이름을 입력하세요. >> ")
    for idx, s in enumerate(students):
        if name == s["name"]:
            flag = 1
            print(f"{name} 학생을 삭제하시겠습니까?(삭제시 복구 불가)")
            choice = input("1. 삭제 2. 취소 >> ")
            if choice == "1":
                # sArr.append(s)
                del students[idx]
                print(f"{name} 학생 성적이 삭제되었습니다.")
            else:
                print("성적 삭제가 취소되었습니다.")
            break
    if flag == 0:
        print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
    else:
        stu_output([s])


# ------------------------------------------------------------------------------
# 학생 등수 처리 함수 시작
def stu_rank(students):
    print(" [ 등수처리 ] ")
    for s in students:
        rank_num = 1
        for i in students:
            if s["total"] < i["total"]:
                rank_num += 1
        s["rank"] = rank_num
    print("등수 처리가 완료되었습니다.")
    stu_output(students)


# ------------------------------------------------------------------------------
# 학생 정렬 함수 시작
def stu_sort(students):
    while True:
        print(" [ 학생성적정렬 ] ")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("0. 이전페이지 이동")
        print("-" * 40)
        choice = input("원하는 번호를 입력하세요. >> ")

        if choice == "1":
            students.sort(key=lambda x: x["name"])
        elif choice == "2":
            students.sort(key=lambda x: x["name"], reverse=True)
        elif choice == "3":
            students.sort(key=lambda x: x["total"])
        elif choice == "4":
            students.sort(key=lambda x: x["total"], reverse=True)
        elif choice == "5":
            students.sort(key=lambda x: x["no"])
        elif choice == "0":
            print("이전 페이지로 이동합니다.")
            break
        print("정렬이 완료되었습니다.")
        stu_output(students)


# ------------------------------------------------------------------------------

# 학생성적프로그램
while True:
    choice = title_program()  # 함수 호출 - 메뉴출력

    if choice == "0":  # 종료
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":  # 입력
        stuNo = stu_input(stuNo, students)  # 학생 성적 입력 함수 호출

    elif choice == "2":  # 출력
        stu_output(students)  # 학생 성적 출력 함수 호출

    elif choice == "3":  # 수정
        stu_update(students)  # 학생 성적 수정 함수 호출

    elif choice == "4":  # 검색
        stu_select(students)  # 학생 성적 검색 함수 호출

    elif choice == "5":  # 삭제
        stu_delete(students)  # 학생 성적 삭제 함수 호출

    elif choice == "6":  # 등수
        stu_rank(students)

    elif choice == "7":  # 정렬
        stu_sort(students)
