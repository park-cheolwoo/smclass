from django.db import models

from django.db import models
# 이름 표시하고 싶으면 verbose_name="아이디" 이렇게 써도 됨
class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True) # 아이디
  pw = models.CharField(max_length=100)  # 패스워드
  name = models.CharField(max_length=100)  # 사용자명
  nickname = models.CharField(max_length=100) # 닉네임
  birth = models.DateField(null=True) # 생년월일
  email = models.EmailField(max_length=100) # 사용자이메일
  tel = models.CharField(max_length=20) # 사용자 전화번호
  point = models.IntegerField(default=0) # 마일리지
  agree1 = models.DateTimeField(auto_now=True) # 필수약관동의
  agree2 = models.DateTimeField(auto_now=True) # 선택약관동의
  mDate = models.DateTimeField(auto_now=True) # 가입일
  
  def __str__(self):
    return f"{self.id}, {self.name}, {self.mDate}"