import datetime

today = datetime.datetime.now()  # var today = new Date();
print(today.year, "년")
print(today.month, "월")
print(today.day, "일")  # day : 요일(자바스크립트) 일(파이썬)
print(today.hour, "시")
print(today.minute, "분")
print(today.second, "초")

print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        today.year, today.month, today.day, today.hour, today.minute, today.second
    )
)

if today.hour >=12:
  print("오후")
else:
  print("오전")


# from datetime import datetime
# today = datetime.now()
