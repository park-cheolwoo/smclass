
import oracledb

# db 연결함수 선언
def connections():
  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("예외발생",e)
  return conn

conn = connections()
cursor = conn.cursor()

#월급이 4000~8000 사이의 사원을 모두 출력하시오.
salary_list = list(input("2개의 숫자를 입력하세요.").split(","))
# salary_list = [4000,8000]
sql = 'select employee_id,emp_name,salary from employees where salary between :l and :l order by salary'
cursor.execute(sql,salary_list) 




# employees 테이블에서 이름이 a가 포함되어 있는 이름, 모든 컬럼 출력
# search = input("검색할 단어를 입력하세요. >> ")
# search = '%'+search+'%' 
# sql = f"select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)


# 키워드
# sql = f"select * from employees where employee_id >= :no"
# cursor.execute(sql,no=no)
# 번호 순서
# sql = f"select * from employees where employee_id >= :l"
# cursor.execute(sql,[search])

title = ['employee_id','emp_name','salary']
rows = cursor.fetchall()
a_list = [] # dict 타입으로 변경해서 저장하시오.
for row in rows:
  a_list.append(dict(zip(title,row)))
print(a_list)

# rows = cursor.fetchall()
# for row in rows:
#   for r in row:
#     print(r,end='\t')
#   print()
# conn.close()