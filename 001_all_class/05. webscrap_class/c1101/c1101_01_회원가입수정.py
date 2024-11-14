import oracledb
import datetime

# db접속
def connects():
    user = "ora_user"
    password = "1111"
    dsn = "localhost:1521/xe"
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
    except Exception as e:
        print("예외처리 : ", e)
    return conn

## 회원수 확인
def member_count():
    # oracle db - mem 테이블의 count 를 가져오시오.
    conn = connects()
    cursor = conn.cursor()
    # employees 테이블에서 부서번호가 50번인 사원수를 가져오시오
    # sql = "select count(*) no,a.department_id dept,department_name deptname\
    #        from employees a,departments b\
    #        where a.department_id = b.department_id and a.department_id = 50\
    #        group by a.department_id, department_name"
    ## where 절을 먼저 사용(필터링)하는 것이 쿼리 속도 향상에 유리함
    sql = 'select count(*) from mem'
    cursor.execute(sql)
    row = cursor.fetchone()
    conn.close()
    return row

# 회원수 확인값을 리턴하시오
conn = connects()
all_member = member_count()[0]
print(" [ 커뮤니티 ] ")
print(f"현재 회원수 : {all_member}")
print()
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보수정")
choice = input("원하는 번호를 입력하세요. >> ")


if choice == "2":
    id = input("아이디를 입력하세요. >> ")
    pw = input("패스워드를 입력하세요. >> ")
    name = input("이름을 입력하세요. >> ")
    birth = input("생년월일을 입력하세요. (예 : 20020312)>> ")
    nowYear = datetime.datetime.now().year
    age = nowYear - int(birth[:4])
    gender = input("성별을 입력하세요. (Male,Female)>> ")
    hobby = input("취미를 입력하세요. >> ")

    # 리스트 저장할 때 db 저장 순서에 유의
    my_list = [id,pw,name,age,birth,gender,hobby]
    print(my_list)
    
    
    # db에 저장
    conn = connects()
    cursor = conn.cursor()
    sql = 'insert into mem(id,pw,name,age,birth,gender,hobby) values(:1,:2,:3,:4,:5,:6,:7)'
    cursor.execute(sql,my_list)
    conn.commit()
    conn.close()

elif choice == "3":
    conn = connects()
    cursor = conn.cursor()
    id = "aaa"
    sql = 'select * from mem where id=:id'
    cursor.execute(sql,id=id)
    row = cursor.fetchone()
    print(f"현재 아이디 : {id}, 현재 취미 : {row[6]}")
    hobby = input("수정할 hobby를 입력하세요. >> ")
    sql = 'update mem set hobby=:hobby where id=:id'
    cursor.execute(sql,id=id,hobby=hobby)
    conn.commit()
    conn.close()
    print("수정되었습니다.")