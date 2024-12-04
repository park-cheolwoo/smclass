from django.shortcuts import render

# Create your views here.

def brand(request):
  return render(request,'brand.html')

def mypage(request):
  return render(request,'mypage.html')