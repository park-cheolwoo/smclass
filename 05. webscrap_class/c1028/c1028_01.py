import oracledb

# oracle 연결 - sql developer연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결확인
print(conn.version)

# sql 실행창 오픈
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)

# 1개의 검색된 데이터 내용 호출
# count1 = cursor.fetchone()
# print("개수 : ",count1)

# 여려개 검색된 데이터 내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()
# for row in rows:
#   print(row)

# print(rows[0][0],rows[0][1],rows[0][2],rows[0][3],rows[0][4],rows[0][5],rows[0][6],rows[0][7])


print(" [ 멤버 출력 ] ")
st_title = ["아이디","비밀번호","이름","이메일","전화번호","성별","취미","가입일"]
print(
    f"{st_title[0]}\t{st_title[1]}\t{st_title[2]}\t{st_title[3]}\t{st_title[4]}\t{st_title[5]}\t{st_title[6]}\t{st_title[7]}\t"
)
print()
print("-"*90)
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}")
print()

conn.close()
