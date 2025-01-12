from django.db import models

# Create your models here.
class Food(models.Model):
  fNo = models.AutoField(primary_key=True)
  fName = models.CharField(max_length=100)
  fCategory = models.CharField(max_length=100)
  fLocation = models.CharField(max_length=1000)
  fTel = models.CharField(max_length=100)
  fInfo = models.CharField(max_length=100)
  fDate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.fNo},{self.fCategory},{self.fName}"


class Foodinfo(models.Model):
    ffNo = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE,)
    fPark = models.CharField(max_length=200)
    fSub = models.CharField(max_length=200)
    fMenu = models.CharField(max_length=200)
    fPrice = models.CharField(max_length=200)
    ffDate = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.ffNo},{self.food},{self.ffDate}"


class Cafe(models.Model):
    cNo = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=100)
    cCategory = models.CharField(max_length=100)
    cLocation = models.CharField(max_length=1000)
    cTel = models.CharField(max_length=100)
    cInfo = models.CharField(max_length=100)
    cDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cNo},{self.cCategory},{self.cName}"


class Cafeinfo(models.Model):
    ccNo = models.AutoField(primary_key=True)
    cafe = models.ForeignKey(Cafe,on_delete=models.CASCADE,)
    cPark = models.CharField(max_length=200)
    cSub = models.CharField(max_length=200)
    cMenu = models.CharField(max_length=200)
    cPrice = models.CharField(max_length=200)
    ccDate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.ccNo},{self.cafe},{self.ccDate}"
