from django.db import models

# Create your models here.
class fBoard(models.Model):
    bNo = models.AutoField(primary_key=True)
    bTitle = models.CharField(max_length=200, null=False)
    bSubtitle = models.CharField(max_length=200, null=False)
    bContent = models.TextField(max_length=2000, null=False)
    bFile1 = models.ImageField(null=True, upload_to="fBoard")
    bFile2 = models.ImageField(null=True, upload_to="fBoard")
    bFile3 = models.ImageField(null=True, upload_to="fBoard")
    bHit = models.IntegerField(default=0)
    bLike = models.IntegerField(default=0)
    bDate = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    bNo = models.ForeignKey("fBoard",on_delete=models.DO_NOTHING)