# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from event.models import Attendance
from member.models import Member


# 쿠폰
class Coupon(models.Model):
    couNo = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE,)
    attendance = models.ForeignKey(Attendance,on_delete=models.CASCADE,)
    discount = models.IntegerField()  # 쿠폰 금액
    used_from = models.DateTimeField()
    used_to = models.DateTimeField()
    
    coupon_code = models.IntegerField(default=0) # 소유 쿠폰 코드


    def __str__(self):
        return f"{self.couNo},{self.member}, {self.discount}"


# class Coupon(models.Model):
#   code = models.CharField(max_length=50, unique=True)
#   use_from = models.DateTimeField() # 쿠폰 사용기한 (~부터)
#   use_to = models.DateTimeField() # 쿠폰 사용기한 (~까지)
#   amount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10000)])
#   active = models.BooleanField(null=True)

#   def __str__(self):
#     return self.code


# from member.models import Member
# from event.models import Post, Coupon_publish


# class Coupon(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     used_from = models.DateField()
#     used_to = models.DateField()
#     discount = models.IntegerField()
#     used = models.BooleanField(default=True)
#     publish_pk = models.IntegerField()

#     def __str__(self):
#         return str(self.post)
