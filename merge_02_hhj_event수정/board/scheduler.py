import time
import schedule
from board.views import reward_points_on_first_day

def job():
  reward_points_on_first_day()
  print("포인트 지급 완료")

# 서버 실행시 매일 자정 실행 # test시 시간 변경하여 사용 
schedule.every().day.at("19:51").do(job)


while True:
  schedule.run_pending()
  time.sleep(1)