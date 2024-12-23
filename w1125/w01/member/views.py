from django.shortcuts import render,redirect
from member.models import Member
# Create your views here.
def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else: 
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs: # member가 있을 경우
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
      context = {"l_msg":"1"}
    else: # member가 없을 경우
      context = {"l_msg":"0"}

    return render(request,'login.html',context)
  
def logout(request):
  request.session.clear()
  return redirect("/")