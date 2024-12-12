from django.shortcuts import render
from member.models import Member

# 로그인 페이지 입장, 로그인
def login(request):
  if request.method == "GET": # url 들어가는거가 get 방식
    return render(request, 'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    
    if qs: # 로그인 성공
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname

      context = {"lmsg":"1"}
      return render(request, 'login.html',context)
    else: # 실패
      context = {"lmsg":"0"}
      return render(request, 'login.html',context)
    

# 로그아웃 
def logout(request):
  request.session.clear() # = 모든 세션 삭제, del request.session['session_id'] = 1개 삭제
  context = {"lmsg":"1"}
  return render(request, 'index.html',context)