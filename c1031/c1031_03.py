# 오라클 db에서는 타입 결정
# 문자형(숫자만) 타입 + 숫자와 사칙연산 가능
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

import oracledb

def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:print("예외 처리 : ",e)
  return conn

conn = connects()
cursor = conn.cursor()
# chartable : num,num,var,var
# chartable2 : num,num,num,num
sql = "select no,kor,to_char(kor_char,'000000000'),to_char(kor_mark,'999,999,999') from chartable2"
#to_char 는 문자형으로 인식함
# 파이썬에서 사칙연산 >> 파이썬에서 형변환(형변환 1번만 실행), 사칙연산 불필요 >> 오라클에서 형변환(오라클이 더 빠름)
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)
  print(f"두수의 합 : {row[1]+row[2]}") # 오라클에서는 계산이 됨, 파이썬에는 안됨
print("검색 완료")
