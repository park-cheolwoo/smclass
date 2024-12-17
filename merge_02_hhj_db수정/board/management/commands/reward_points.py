from django.core.management.base import BaseCommand
from board.views import reward_points_on_first_day

class Command(BaseCommand):
  help='매달 1일에 상위 5개 게시글 작성자에게 포인트 지급'

  def handle(self, *args, **options):
    reward_points_on_first_day()
    # return super().handle(*args, **options)
    self.stdout.write(self.style.SUCCESS('포인트 지급 완료'))