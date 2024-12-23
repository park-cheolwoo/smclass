from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=50)
  major = models.CharField(max_length=50)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=0)
  gender = models.CharField(max_length=50)
  hobby = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name