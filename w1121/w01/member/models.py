from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  pw = models.CharField(max_length=100, null=False)
  name = models.CharField(max_length=50)
  nickname = models.CharField(max_length=50)
  tel = models.CharField(max_length=50, default='010-1111-1111')
  gender = models.CharField(max_length=10, default='남자')
  hobby = models.CharField(max_length=10, default='game')
  mdate = models.DateTimeField(auto_now=True)
  # auto_now_add : 입력할 때만 1번만 추가
  # auto_now : 수정할 때마다 시간 입력
  
  def __str__(self):
    return f"{self.id}, {self.name}, {self.nickname}"