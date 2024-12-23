from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from django.core import serializers

# Create your views here.
def login(request):
  if request.method == "GET":
    return render(request,'login.html')

def logout(request):
  request.session.clear() # 세션 지우기 # del request.session.get('session_id') # 1개만 지우기
  context = {"outmsg":"1"}
  return render(request,'index.html',context)


def loginChk(request):
    # @csrf_exempt # 예외처리
    id = request.POST.get("id","")
    pw = request.POST.get("pw","")
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
        request.session['session_id'] = id
        request.session['session_nicName'] = qs[0].nicName
        qs_list = list(qs.values())
        context = {"result":"success","member":qs_list}
    else:
        context = {"result":"fail"}
    return JsonResponse(context)

    # qs = Member.objects.get(id=id,pw=pw)
    # json_qs = serializers.serialize('json',[qs]) # json 타입변경

def step03(request):
   return render(request,'step03.html')

def idChk(request):
    id = request.POST.get("id", "")
    qs = Member.objects.filter(id=id)
    print("qs :", qs)
    if not qs:
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)
