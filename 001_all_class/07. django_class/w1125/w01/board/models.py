from django.db import models
from member.models import Member

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  # id = models.CharField(max_length=50)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  # img 파일 업로드
  bfile = models.ImageField(null=True,upload_to='board') # 이미지만
  # bimg = models.FileField(null=True) # 모든 파일

  def __str__(self):
    return f"{self.bno},{self.btitle},{self.bgroup},{self.bdate}"