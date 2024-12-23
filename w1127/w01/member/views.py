from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      print("로그인 성공")
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      context = {"l_msg":"1"}
    else:
      print("로그인 실패")
      context = {"l_msg":"0"}
    return render(request,'login.html',context)
  
def logout(request):
  request.session.clear()
  context = {"l_msg":"1"}
  return render(request,'index.html',context)