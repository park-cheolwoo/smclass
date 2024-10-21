a = ["1", "홍길동", "94", "73", "54", "221", "73.6666666667", "1"]
b = ["20", "57", "51", "65", "173", "57.66666666667", "1"]
t_title = ['no','name','kor','eng','math','total','avg','rank']
students = []

def f_float(value):
  if value.isdigit(): # 정수인지 / 실수 or 문자열인지
    return int(value) # 정수일 때 정수 변환
  else:
    try : return float(value) # 실수일 때 실수로 변환
    except : return value # 문자일 때 문자열 변환


c = []
for idx,value in enumerate(a):
  c.append(f_float(value))


#students 리스트에 딕셔너리로 저장
print(c)
students.append(dict(zip(t_title,c)))
print(students)








# # try-except 구문을 사용해서 정수, 실수 구분.
# def t_float(n):
#     try:
#         int(n)
#         return True
#     except:
#         return False


# # 문자열인지 아닌지 구분
# for idx, i in enumerate(a):
#     if i.isdigit(): # 정수이면 True, 아니면 False
#         print(f"{idx}번째 {type(int(i))}는 숫자입니다.")
#     else:
#         print(f"{idx}번째 {type(float(i))}는 입니다.")


# 정수로 변경
# for i in b:
#     if t_float(i):
#         i = int(i)
#     else:
#         i = float(i)
#     c.append(i)
# print(c)

# b의 리스트 float 변경
# b의 형태가 모두 숫자 -> float

# for i in b:
#   c.append(float(c))
# print(c)
