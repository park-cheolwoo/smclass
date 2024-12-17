from django.db import models
# from member.models import Member

CHOICES = {
    (0,"바로 입장"),
    (10,"10분 이내"),
    (30,"30분 이내"),
    (45,"30분~1시간"),
    (60, "1시간 이상"),
    (120, "2시간 이상"),
}


class fBoard(models.Model):
    member = models.ForeignKey('member.Member',on_delete=models.DO_NOTHING, related_name="fBoard_member")
    like_members = models.ManyToManyField("member.Member", related_name="fboard_like_members")
    bNo = models.AutoField(primary_key=True)
    bLocation = models.CharField(max_length=1000)
    bTime = models.CharField(max_length=200, choices=CHOICES)
    bTitle = models.CharField(max_length=200, null=False)
    bSubtitle = models.CharField(max_length=200, null=False)
    bContent = models.TextField(null=False)
    bFile1 = models.ImageField(null=False, upload_to="fBoard")
    bFile2 = models.ImageField(null=True, upload_to="fBoard")
    bFile3 = models.ImageField(null=True, upload_to="fBoard")
    bHit = models.IntegerField(default=0)
    bLike = models.IntegerField(default=0)
    bDate = models.DateTimeField(auto_now=True)
