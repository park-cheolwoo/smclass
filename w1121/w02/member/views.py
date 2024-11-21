from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        qs = Member.objects.filter(id=id, pw=pw)
        if qs:
            request.session["session_id"] = id
            request.session["session_nickname"] = qs[0].nickname
            print("로그인 성공")
            msg = "1"
        else:
            print("로그인 실패")
            msg = "0"
        return render(request, "login.html",{"msg":msg})

def join01(request):
    if request.method == "GET":
        return render(request, "join01.html")
    
def join02(request):
  if request.method == "GET":
      return render(request, "join02.html")
