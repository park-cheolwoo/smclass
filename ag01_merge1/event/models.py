from django.db import models
from member.models import Member

class Attendance(models.Model):
  aNo = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='attendance_member')
  count = models.IntegerField(default=0) # 출석 count
  aDate = models.DateField(max_length=100) # 출석 버튼 누르는 시각
  aTicket = models.IntegerField(default=0) # 응모권 개수
  usedTicket = models.IntegerField(default=0)  # 사용한 응모권 개수?
  ### aPoint는 member.point로 migrate하면 가능

  coupon_code = models.IntegerField(default=0) # 소유 쿠폰 코드

  def __str__(self):
    return f"{self.member},{self.count},{self.aDate}"




# class Post(models.Model): # 쿠폰 껍데기
#   member = models.ForeignKey(Member,related_name='post',on_delete=models.PROTECT) # 삭제 방지
#   title = models.CharField(max_length=50)
#   content = models.CharField(max_length=60000) # 내용
#   price = models.IntegerField() # 가격

#   def __str__(self):
#         return self.title


# class Coupon_publish(models.Model): # 쿠폰 내용
#   post = models.ForeignKey(Post,related_name='coupon_publish',on_delete=models.CASCADE) # Post 지우면 얘도 삭제
#   used_from = models.DateField()
#   used_to = models.DateField()
#   discount = models.IntegerField()
#   amount = models.IntegerField()

#   def __str__(self):
#      return str(self.post) 


  


  