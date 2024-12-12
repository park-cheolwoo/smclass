from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers 
from member.models import Member
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib import messages
import random


def mlist(request):
  return render(request, 'index.html')


### 회원가입 - step01. 약관동의
def join01(request):
  return render(request, "join01.html")

### 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")


### 로그인 - 아이디/패스워드 일치 확인
def loginChk(request):
  id = request.POST.get("id", "")
  pw = request.POST.get("pw", "")

  ## db확인
  qs = Member.objects.filter(id=id, pw=pw)
  print(f"[ 아이디/패스워드 확인 ]\n아이디 : {id}\n패스워드 : {pw}")

  # 아이디패스워드일치
  if qs:
    request.session['session_id'] = qs[0].id
    request.session['session_nickname'] = qs[0].nickname
    list_qs = list(qs.values()) # 아이디 패스워드 묶어서 list_qs에 저장
    context = {"result":"success", "member":list_qs} # member라는 이름으로 list_qs 보내기
  else:
    context = {"result":"fail"}

  return JsonResponse(context)


### 로그인페이지
def login(request):
  return render(request, "login.html")