import datetime
today = datetime.datetime.now()
print(today)
print(today.strftime("%y-%m-%d"))
now_date = today.strftime("%Y-%m-%d")
print(now_date)
now_datetime = today.strftime("%y-%m-%d %H:%M:%S")
print(now_datetime)