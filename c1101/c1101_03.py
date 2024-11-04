import oracledb


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
def stu_input():
    print("[ 학생 성적 입력 ]")
    conn = connect()
    cursor = conn.cursor()
    sql = "select students_seq.currval from dual"
    cursor.execute(sql)
    row = cursor.fetchone()
    conn.close()

    no = row
    name = input(f"{no}번째 이름을 입력하세요. >> ")
    kor = int(input("국어 성적을 입력하세요. >> "))
    eng = int(input("영어 성적을 입력하세요. >> "))
    math = int(input("수어 성적을 입력하세요. >> "))
    total = int(kor + eng + math)
    avg = float(total / 3)
    rank = 0
    s_list = [name, kor, eng, math, total, avg, rank]
    
    conn = connect()
    cursor = conn.cursor()
    sql = "insert into students values(STUDENTS_SEQ.nextval, :1, :2, :3, :4, :5, :6, :7, sysdate)"
    cursor.execute(sql, s_list)
    conn.commit()
    conn.close()
    print(f"{name} 학생 성적이 입력되었습니다.")


# --------------------------------------------------------------------
# 학생성적출력함수------------------------------------------------------
def stu_output():
    s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수", "등록일"]
    conn = connect()
    cursor = conn.cursor()
    sql = "select * from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    print(" [ 학생 성적 출력 ] ")
    print(
        f"{s_title[0]}\t{s_title[1]:8s}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{(s_title[6])}\t{s_title[7]}\t"
    )
    print()
    print("-" * 80)
    for row in rows:
        print(
            f"{row[0]}\t{row[1]:8s}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.2f}\t{row[7]}\t"
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
    conn.close()
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
    conn = connect()
    cursor = conn.cursor()
    sql = "update students set kor=:1, eng=:2, math=:3, total=:4, avg=:5 where name = :6"
    try:
        cursor.execute(sql, u_list)
    except Exception as e:
        print("에러 발생", e)
    conn.commit()
    conn.close()
    print(f"{name} 학생 성적이 수정되었습니다.")


while True:
    print(" [ 학생성적프로그램 ] ")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램 종료")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == "1":
        stu_input()
    elif choice == "2":
        stu_output()
    elif choice == "3":
        stu_update()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
