from django.db import models
from member.models import Member

# Create your models here.
class adminUser(models.Model):
    aNo = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    authority = models.IntegerField()
    mDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.aNo}, {self.id},{self.mDate}"


class Stat(models.Model):
  sNo = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
  action = models.CharField(max_length=200)
  where = models.CharField(max_length=200)
  point = models.IntegerField
  sDate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.sNo}, {self.member},{self.action},{self.where}"
