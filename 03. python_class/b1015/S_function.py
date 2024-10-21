# 학생 성적 프로그램 변수
students = []
f = open('students.txt','r',encoding='utf-8')
s_keys = ["no","name","kor","eng","math","total","avg","rank"]
while True:
    line = f.readline()
    if not line :break
    s = line.strip().split(",")
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3])
    s[4] = int(s[4])
    s[5] = int(s[5])
    s[6] = float(s[6])
    s[7] = int(s[7])
    students.append(dict(zip(s_keys,s))) 
f.close()
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]  # 전역변수
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
choice = 0  # 전역변수

# ---------------------------------------------------------------------


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


# ---------------------------------------------------------------------
# 학생 성적 입력 함수 시작
def stu_input(stuNo):
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


# ------------------------------------------------
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


# -----------------------------------------------
# 학생 성적 수정 함수
def stu_update():
    flag = 0
    name = input("찾고자 하는 학생 이름을 입력하세요. >> ")
    sArr = []
    for s in students:
        if s["name"] == name:
            flag = 1
            sArr.append(s)
            print(f"{name} 학생을 찾았습니다.")
            print(" [ 수정 과목 선택 ]")
            print("1. 국어 성적 수정")
            print("2. 영어 성적 수정")
            print("3. 수학 성적 수정")
            choice = input("원하는 번호를 선택하세요. >> ")
            if choice == "1":
                print(f"현재 국어 점수 : {s['kor']}")
                s["kor"] = int(input("수정하실 국어 점수를 입력하세요. >>"))
            if choice == "2":
                print(f"현재 영어 점수 : {s['eng']}")
                s["eng"] = int(input("수정하실 영어 점수를 입력하세요. >>"))
            if choice == "3":
                print(f"현재 수학 점수 : {s['math']}")
                s["math"] = int(input("수정하실 수학 점수를 입력하세요. >>"))
            s["total"] = s["kor"] + s["eng"] + s["math"]
            s["avg"] = s["total"] / 3
            print(f"{name} 학생 성적이 수정되었습니다.")
            stu_output(sArr)
    if flag == 0:
        print(f"{name} 을 포함한 학생을 찾지 못했습니다. 다시 시도해주세요.")


# ----------------------------------------------------------------
# 학생 성적 검색 함수
def stu_search():
    while True:
        flag = 0
        name = input("찾고자 하는 학생 이름을 입력하세요.(0. 이전 화면) >> ")
        sArr = []
        if name == "0":
            print("이전 화면으로 이동합니다.")
            print()
            break
        for s in students:
            if s["name"].find(name) != -1:
                flag = 1
                sArr.append(s)
        print(f"{name} 을 포함한 {len(sArr)} 명의 학생을 찾았습니다.")
        stu_output(sArr)
        if flag == 0:
            print(f"{name} 을 포함한 학생을 찾지 못했습니다. 다시 시도해주세요.")


# ----------------------------------------------------------------
# 학생 성적 삭제 함수
def stu_delete():
    flag = 0
    name = input("찾고자 하는 학생 이름을 입력하세요. >> ")
    sArr = []
    for s in students:
        if s["name"] == name:
            flag = 1
            sArr.append(s)
            print(f"{name} 학생 성적을 삭제하시겠습니까?(삭제시 복구 불가)")
            choice = input("1. 삭제 2. 취소 >> ")
            if choice == "1":
                students.remove(s)
                print(f"{name} 학생 성적이 삭제되었습니다.")
                stu_output(sArr)
            elif choice == "2":
                print("성적 삭제가 취소되었습니다.")
                stu_output(sArr)
    if flag == 0:
        print(f"{name} 학생을 찾지 못했습니다. 다시 시도해주세요.")


# ----------------------------------------------------------------
# 등수 처리 함수
def stu_rank():
    for s in students:
        count = 1
        for t in students:
            if s["total"] < t["total"]:
                count += 1
        s["rank"] = count
    print("등수 처리가 완료되었습니다.")
    stu_output(students)


# ----------------------------------------------------------------
# 학생 정렬 함수
def stu_sort():
    while True:
        print(" [ 학생 정렬 ] ")
        print("1. 학생 이름순 정렬")
        print("2. 학생 이름 역순 정렬")
        print("3. 학생 성적순 정렬")
        print("4. 학생 성적 역순 정렬")
        print("5. 학생 번호순 정렬")
        print("0. 이전 화면")
        choice = input("원하시는 번호를 입력하세요. >> ")
        if choice == "0":
            print("이전 화면으로 이동합니다.")
            print()
            break
        elif choice == "1":
            students.sort(key=lambda x: x["name"])
        elif choice == "2":
            students.sort(key=lambda x: x["name"], reverse=True)
        elif choice == "3":
            students.sort(key=lambda x: x["total"], reverse=True)
        elif choice == "4":
            students.sort(key=lambda x: x["total"])
        elif choice == "5":
            students.sort(key=lambda x: x["no"])
        print("학생 정렬이 완료되었습니다.")
        stu_output(students)
