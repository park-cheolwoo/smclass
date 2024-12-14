from django.db import models

# 이름 표시하고 싶으면 verbose_name="아이디" 이렇게 써도 됨 
class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True) # 아이디
  pw = models.CharField(max_length=100)  # 패스워드
  name = models.CharField(max_length=100)  # 사용자명
  nickname = models.CharField(max_length=100) # 닉네임
  birth = models.DateField(null=True) # 생년월일
  email = models.EmailField(max_length=100) # 사용자 이메일
  tel = models.CharField(max_length=20) # 사용자 전화번호
  addr = models.CharField(max_length=200) # 사용자 주소
  mDate = models.DateTimeField(auto_now_add=True) # 가입일
  point = models.IntegerField(default=0) # 마일리지

  # 약관동의
  agree1 = models.DateTimeField(auto_now_add=True) # 필수약관동의
  agree2 = models.DateTimeField(auto_now_add=True) # 선택약관동의
  
  # 비밀번호 찾기 - 인증번호 관련
  verification_email = models.EmailField()  # 이메일 인증용
  verification_code = models.CharField(max_length=6) # 인증번호
  created_at = models.DateTimeField(auto_now_add=True)  # 생성 일시

  def __str__(self):
    return f"{self.id}, {self.name}, {self.mDate}"