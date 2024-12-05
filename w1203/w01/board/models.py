from django.db import models
from member.models import Member

class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  # id = models.CharField(max_length=100)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  # Board 객체 좋아요 체크 - bno,member
  like_members = models.ManyToManyField(Member,default='',related_name="like_member")
  #ManyToMany >> bno(여러개) + member(여러개) 조합할 수 있는 구조(유사)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  # 계층형 게시판
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  # img 파일업로드
  bfile = models.ImageField(null=True,upload_to='board')
  # bimg = models.FileField(null=True)
  
  def __str__(self):
    return f"{self.bno},{self.btitle},{self.bgroup},{self.bdate}"
