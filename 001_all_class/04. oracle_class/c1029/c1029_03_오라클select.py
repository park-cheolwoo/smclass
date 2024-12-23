import oracledb

# sql developer 실행
conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
# sql 창이 열림
cursor = conn.cursor()
# sql 구문 작성,실행
# no = input("숫자를 입력하세요. >> ")

# no=10,20,30을 검색해서 출력

# no1,no2,no3 = list(input("3개의 숫자를 입력하세요").split(",")) #10,20,30
# sql = 'select * from students where no in (:no1,:no2,:no3)'
# cursor.execute(sql,no1=no1,no2=no2,no3=no3) 

## 리스트로 값 전달
# execute 뒤에는 dict,list,tuple 타입만 가능
sql_list = list(input("3개의 숫자를 입력하세요").split(",")) #10,20,30
sql = 'select * from students where no in (:1,:2,:3)'
cursor.execute(sql,sql_list) 


# execute함수 : 변수를 추가
# sql = "select * from students where no >= :no"
# cursor.execute(sql,no=no)

# 문자열 함수 f 사용
# sql = f"select * from students where No >= {no}"
# cursor.execute(sql)


# 데이터 가져오기 - fetchone() : 1개 가져오기, fetchmany() : 정해진 숫자만큼 가져오기, fetchall() : 모든 데이터
rows = cursor.fetchall()
titles = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수", "등록일"]
for title in titles:
    print(title, end="\t")
print()
print("-" * 80)
for row in rows:
    for i, r in enumerate(row):
        if i == 1:
            print(f"{r:12s}", end="\t")
        elif i == 6:
            print(f"{r:.2f}", end="\t")
            continue
        elif i == 8:
            # strftime() 함수 : 날짜포맷함수 %Y 2024 %y 24
            print(r.strftime("%y-%m-%d"), end="\t")
        else:
            print(r, end="\t")
    print()
# 종료
conn.close()
