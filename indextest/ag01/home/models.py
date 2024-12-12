from django.db import models


# 검색창 용 클래스
class SearchMapInfo(models.Model):
  sInput = models.CharField(max_length=200) # 입력 검색어
  sLocation = models.CharField(max_length=200,null=True) # 지역 이름
  sMenu = models.CharField(max_length=200,null=True) # 메뉴 e.g. 파스타
  sKeyword = models.CharField(max_length=200,null=True) # 메인키워드 e.g. 크리스마스, 데이트, 한식, 일식 etc
  sName = models.CharField(max_length=200,null=True) # 식당, 카페 이름

  def __str__(self):
    return f"{self.sInput},{self.sLocation},{self.sMenu},{self.sKeyword},{self.sName}"