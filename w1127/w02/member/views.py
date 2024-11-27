from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from member.models import Member

# Create your views here.
def login(request):
  return render(request,'login.html')

def loginChk(request):
    # @csrf_exempt # csrf_token 예외처리 함수
    id=request.POST.get('id',"")
    pw=request.POST.get('pw',"")
    print("html에서 넘어온 데이터 : ",id,pw)

    # filter 검색 - list타입으로 보내야함
    qs = list(Member.objects.filter(id=id,pw=pw).values())
    # 객체는 list타입으로 보내지 않으면 에러
    if qs:
        context={'member':qs,"result":"success"}
    else:
        context={"result":"fail"}
    return JsonResponse(context)

    # # get 검색 - json타입으로 보내야함
    # qs = list(Member.objects.get(id=id, pw=pw))
    # json_qs = serializers.serialize('json',qs)
    # # 객체는 list타입으로 보내지 않으면 에러
    # if qs:
    #     context = {"member": json_qs, "result": "success"}
    # else:
    #     context = {"result": "fail"}
    # return JsonResponse(context)

    # 변수로 보내는 방법
    # qs = Member.objects.filter(id=id,pw=pw)
    # if qs:
    #   context={"id":qs[0].id,"nicName":qs[0].nicName,"result":"success"}
    # else:
    #   context={"result":"fail"}
    # return JsonResponse(context)
