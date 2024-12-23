from django.db import models
from member.models import Member

CHOICES = {
      ('추천맛집','추천맛집😋'), # 오른쪽에 있는 것이 화면에 보인다.
      ('감성카페', '감성카페☕'),
      ('취미', '취미🎮'),
      ('웨이팅', '웨이팅👥'),
      ('실시간공유', '실시간공유🗫'),
      ('생활/편의', '생활/편의🧼'),
      ('교통', '교통🚗'),
      ('풍경', '풍경🌴'),
      ('사건사고', '사건사고😈'),
      ('기타', '기타🔍')
  }
class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  # id = models.CharField(max_length=100)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  bgps = models.CharField(max_length=1000)
  bselect = models.CharField(max_length=500,choices=CHOICES)
  like_member = models.ManyToManyField(Member,default='',related_name='like_member')
  # 계층형 게시판
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  # img 파일업로드
  bfile = models.ImageField(null=True,blank=True,upload_to='board')
  # bimg = models.FileField(null=True)
  
  def __str__(self):
    return f"{self.bno},{self.btitle},{self.bgroup},{self.bdate}"
