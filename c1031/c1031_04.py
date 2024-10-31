# 입력한 달 이상의 입사한 사원을 출력하시오.
import oracledb

user = 'ora_user'
password = "1111"
dsn = "localhost:1521/xe"

conn = oracledb.connect(user=user,password=password,dsn=dsn)
cursor = conn.cursor()

d_day = input("숫자를 입력하세요. >> ")
sql = "select hire_date,substr(hire_date,4,2) from employees where to_number(substr(hire_date,4,2)) > :d_day"
cursor.execute(sql,d_day=d_day)
rows = cursor.fetchall()
for row in rows:
  print(row)
conn.close()
