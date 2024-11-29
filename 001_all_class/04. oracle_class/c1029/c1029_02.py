# 학생성적출력을 하시오.

import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()
sql = 'select * from students'
cursor.execute(sql)
rows = cursor.fetchall()

titles = ["번호","이름","국어","영어","수학","합계",'평균','등록일']
for title in titles:
  print(title,end='\t')
print()
print("-"*80)
for row in rows:
  for i,r in enumerate(row):
    if i ==1:
      print(f"{r:12s}",end='\t')
      continue
    elif i == 6:
      print(f"{r:.2f}",end='\t')
      continue
    elif i == 8:
      print(f"{r.strftime('%y-%m-%d')}",end='\t')
      continue
    else : print(r,end='\t')
  print()
conn.close()