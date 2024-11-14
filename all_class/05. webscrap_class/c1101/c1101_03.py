import oracledb
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수", "등록일"]

# db 연결함수 -------------------------------------------------------
def connect():
    user = "ora_user"
    password = "1111"
    dsn = "localhost:1521/xe"
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
    except Exception as e:
        print("에러 발생 : ", e)
    return conn


# --------------------------------------------------------------------
# 메인화면 함수 ------------------------------------------------------
# def title_screen(choice):
#     print(" [ 학생성적프로그램 ] ")
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적수정")
#     print("0. 프로그램 종료")
#     choice = input("원하는 번호를 입력하세요. >> ")
#     return choice


# --------------------------------------------------------------------
# 학생성적입력함수------------------------------------------------------
def stu_insert():
    conn = connect()
    cursor = conn.cursor()
    print("[ 학생 성적 입력 ]")
    # sql = "select students_seq.nextval from dual"
    # cursor.execute(sql)
    # row = cursor.fetchone()
    # cursor.close()

    # no = row[0]
    name = input("이름을 입력하세요. >> ")
    kor = int(input("국어 성적을 입력하세요. >> "))
    eng = int(input("영어 성적을 입력하세요. >> "))
    math = int(input("수어 성적을 입력하세요. >> "))
    total = kor+eng+math
    avg = total/3
    s_list = [name,kor,eng,math,total,avg]
    # insert, update, delete의 경우 conn.commit() 해야 반영됨
    sql = "insert into students values(STUDENTS_SEQ.nextval, :1, :2, :3, :4, :5, :6, 0, sysdate)"
    cursor.execute(sql, s_list)
    conn.commit()
    conn.close()
    print(f"{name} 학생 성적이 입력되었습니다.")
    print()

# --------------------------------------------------------------------
# 학생성적출력함수------------------------------------------------------
def stu_output():
    print(" [ 학생 성적 출력 ] ")
    conn = connect()
    cursor = conn.cursor()
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(rows) <1 :
        print("데이터가 없습니다.")
        return
    print(
        f"{s_title[0]}\t{s_title[1]:8s}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{(s_title[6])}\t{s_title[7]}\t{s_title[8]}"
    )
    print()
    print("-" * 80)
    for row in rows:
        print(
            f"{row[0]}\t{row[1]:8s}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}"
        )
    print()

# --------------------------------------------------------------------
# 학생성적검색함수-----------------------------------------------------
def stu_search():
    conn = connect()
    cursor = conn.cursor()
    print(" [ 학생 성적 검색 ] ")
    print("1. 이름으로 검색")
    print("2. 합계순 검색")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == "1":
        print(" [ 이름으로 검색 ] ")
        search = input("찾고자 하는 이름을 입력하세요. >> ")
        search = '%'+search+'%'
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students where name like :search"
    elif choice == "1":
        print(" [ 이름으로 검색 ] ")
        search = input("찾고자 하는 이름을 입력하세요. >> ")
        search = "%" + search + "%"
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students where name like :search"
    cursor.execute(sql, search=search)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(rows) <1 :
        print("데이터가 없습니다.")
        return 
    print(
        f"{s_title[0]}\t{s_title[1]:8s}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{(s_title[6])}\t{s_title[7]}\t{s_title[8]}"
    )
    print()
    print("-" * 80)
    for row in rows:
        print(
            f"{row[0]}\t{row[1]:8s}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}"
        )
    print()
# --------------------------------------------------------------------
# 학생성적수정함수------------------------------------------------------
def stu_update():
    print("  [ 학생 성적 수정 ]  ")
    name = input("수정할 학생 이름을 입력하세요.")
    conn = connect()
    cursor = conn.cursor()
    sql = "select * from students where name =:name"
    cursor.execute(sql, name=name)
    row = cursor.fetchone()
    row = list(row)
    cursor.close()
    if not row : 
        print(f"{name} 학생을 찾지 못했습니다.")
        return
    print(f"{name} 학생을 찾았습니다.")
    print("1. 국어 성적 수정")
    print("2. 영어 성적 수정")
    print("3. 수학 성적 수정")
    choice = int(input("원하는 번호를 입력하세요. >> "))
    if choice == 1:
        print(f"현재 국어 점수 : {row[2]}")
        row[2] = int(input("수정하실 국어 점수를 입력하세요."))
    elif choice == 2:
        print(f"현재 영어 점수 : {row[3]}")
        row[3] = int(input("수정하실 영어 점수를 입력하세요."))
    elif choice == 3:
        print(f"현재 수학 점수 : {row[4]}")
        row[4] = int(input("수정하실 수학 점수를 입력하세요."))
    row[5] = row[2] + row[3] + row[4]
    row[6] = row[5] / 3
    u_list = [row[2], row[3], row[4], row[5], row[6], name]
    cursor = conn.cursor()
    sql = "update students set kor=:1, eng=:2, math=:3, total=:4, avg=:5 where name = :6"
    cursor.execute(sql, u_list)
    conn.commit()
    conn.close()
    print(f"{name} 학생 성적이 수정되었습니다.")
# 학생성적정렬함수 ---------------------------------------------------
def stu_sort():
    conn = connect()
    cursor = conn.cursor()
    print(" [ 학생 성적 정렬 ] ")
    print("1. 이름순차정렬")
    print("2. 이름역순정렬")
    print("3. 합계순차정렬")
    print("4. 합계역순정렬")
    print("5. 등수순차정렬")
    print("6. 등수역순정렬")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == "1":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name"
    elif choice == "2":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name desc"
    elif choice == "3":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total"
    elif choice == "4":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total desc"
    elif choice == "5":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by rank"
    elif choice == "6":
        sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by rank desc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(rows) < 1:
        print("데이터가 없습니다.")
        return
    print(
        f"{s_title[0]}\t{s_title[1]:8s}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{(s_title[6])}\t{s_title[7]}\t{s_title[8]}"
    )
    print()
    print("-" * 80)
    for row in rows:
        print(
            f"{row[0]}\t{row[1]:8s}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}"
        )
    print()
    print("출력이 완료되었습니다.")
# -------------------------------------------------------------------
# 등수처리함수--------------------------------------------------------
def stu_rank():
    conn = connect()
    cursor = conn.cursor()
    print(" [ 등수 처리 ] ")
    sql = 'update students a set rank = (\
           select ranks from(\
           select rank() over(order by total) ranks,no from students) b\
           where a.no = b.no)'
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("등수처리가 완료되었습니다.")
# ---------------------------------------------------------------------
while True:
    print(" [ 학생성적프로그램 ] ")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("4. 학생성적수정")
    print("5. 학생성적정렬")
    print("6. 등수처리")
    print("0. 프로그램 종료")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == "1":
        stu_input()
    elif choice == "2":
        stu_output()
    elif choice == "3":
        stu_search()
    elif choice == "4":
        stu_update()
    elif choice == "5":
        stu_sort()
    elif choice == "6":
        stu_rank()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
