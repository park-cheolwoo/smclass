from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from comment.models import Comment
from member.models import Member
from board.models import Board

def cwrite(request):
  id = request.session.get('session_id')
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get('cpw',"")
  ccontent = request.POST.get('ccontent',"")
  print("cpw : ",cpw)
  print("ccontent : ",ccontent)
  qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("list_qs : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)

def cdelete(request):
    cno = request.POST.get("cno", "")
    print("cno : ", cno)
    Comment.objects.filter(cno=cno).delete()
    context = {"result":"success"}
    return JsonResponse(context)


def cupdate(request):
  # id = request.session.get('session_id')
  cno = request.POST.get("cno")
  ccontent = request.POST.get("ccontent")
  qs = Comment.objects.get(cno=cno)
  qs.ccontent = ccontent
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("list_qs : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)