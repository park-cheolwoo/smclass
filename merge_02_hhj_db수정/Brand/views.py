from django.shortcuts import render

# Create your views here.

def brand(request):
  return render(request,'brand.html')

def update(request):
    return render(request,'mypage_update.html')

def rvwCheck(request):
    return render(request, "mypage_rvwCheck.html")

def resCheck(request):
    return render(request, "mypage_resCheck.html")

def starCheck(request):
    return render(request, "mypage_starCheck.html")

def boardCheck(request):
    return render(request, "mypage_boardCheck.html")
