from django.db import models
from board.models import Board
from member.models import Member


class Comment(models.Model):
  cno = models.AutoField(primary_key=True)
  board = models.ForeignKey(Board,on_delete=models.CASCADE) # 부모삭제시, 자식삭제
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
  ccontent = models.TextField(blank=True)
  cdate = models.DateTimeField(auto_now=True)
    
  # 계층형 댓글
  cgroup = models.IntegerField(null=True)
  cstep = models.IntegerField(default=0)
  cindent = models.IntegerField(default=0)
  
  def __str__(self):
    return f"{self.cno},{self.ccontent},{self.cdate}"
  

