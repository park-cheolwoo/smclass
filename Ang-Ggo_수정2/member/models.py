from django.db import models
from FoodCafe.models import Food, Cafe
from foodBoard.models import fBoard

# 현재 member
# 이름 표시하고 싶으면 verbose_name="아이디" 이렇게 써도 됨
class Member(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # 아이디
    pw = models.CharField(max_length=100)  # 패스워드
    name = models.CharField(max_length=100)  # 사용자명
    nickname = models.CharField(max_length=100)  # 닉네임
    birth = models.DateField(null=True)  # 생년월일
    email = models.EmailField(max_length=100)  # 사용자 이메일
    tel = models.CharField(max_length=20)  # 사용자 전화번호
    addr = models.CharField(max_length=200)  # 사용자 주소
    mDate = models.DateTimeField(auto_now_add=True)  # 가입일
    point = models.IntegerField(default=0)  # 마일리지

    # 약관동의
    agree1 = models.DateTimeField(auto_now_add=True) # 필수약관동의
    agree2 = models.DateTimeField(auto_now_add=True) # 선택약관동의

    def __str__(self):
        return f"{self.id}, {self.name}, {self.mDate}"


# 회원 즐겨찾기
class Star(models.Model):
    sNo = models.AutoField(primary_key=True)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="starred_boards"
    )
    fboard = models.ForeignKey(
        "foodBoard.fBoard", on_delete=models.CASCADE, related_name="starred_by"
    )
    sDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member} - {self.fboard}"


# 회원 예약
class Reservation(models.Model):
    rNo = models.AutoField(primary_key=True)
    res = models.ManyToManyField(Member, default="", related_name="res_members")
    resPeople = models.IntegerField(default=0)
    resMemo = models.TextField(max_length=2000, default="")
    rDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rNo},{self.res}"


# 탈퇴 회원
class delMember(models.Model):
    dNo = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    dDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.dNo},{self.id}"


# 평점
class Rating(models.Model):
    rNo = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    fboard = models.ForeignKey(fBoard, on_delete=models.DO_NOTHING)
    rating = models.CharField(max_length=10)
    rDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rNo},{self.member},{self.fboard},{self.rating}"
