import oracledb
# sql developer 실행
conn = oracledb.connect(user="ora_user",password='1111',dsn='localhost:1521/xe')
# sql 창이 열림
cursor=conn.cursor()
# sql 구문 작성,실행
sql = 'select * from students'
cursor.execute(sql)
# 데이터 가져오기 - fetchone() : 1개 가져오기, fetchmany() : 정해진 숫자만큼 가져오기, fetchall() : 모든 데이터
rows = cursor.fetchall()
titles = ["번호","이름","국어","영어","수학","합계","평균","등수","등록일"]
for title in titles:
  print(title,end='\t')
print()
print("-"*80)
for row in rows:
    for i, r in enumerate(row):
        if i == 1:
          print(f"{r:12s}",end='\t')  
        elif i == 6:
            print(f"{r:.2f}",end='\t')
            continue
        elif i == 8:
            # strftime() 함수 : 날짜포맷함수 %Y 2024 %y 24
            print(r.strftime('%y-%m-%d'),end='\t')
        else:
            print(r, end="\t")
    print()
# 종료
conn.close()
