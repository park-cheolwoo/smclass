from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=200,primary_key=True)
  pw = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  nickname = models.CharField(max_length=200)
  birth = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  tel = models.CharField(max_length=200)
  point = models.IntegerField(default=0)
  agree1 = models.DateTimeField(max_length=100,auto_now=True)
  agree2 = models.DateTimeField(max_length=100,auto_now=True)
  mdate = models.DateTimeField(max_length=100,auto_now=True)

  def __str__(self):
    return f"{self.id},{self.name},{self.mdate},{self.point}"