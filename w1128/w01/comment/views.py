from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from comment.models import Comment
from member.models import Member
from board.models import Board
from django.core import serializers
# Create your views here.
def cwrite(request):
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno")
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get("cpw","")
  ccontent = request.POST.get("ccontent","")
  print(cpw,ccontent) # 성공
  qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
  json_qs = serializers.serialize("json",[qs])
  context={"comment":json_qs,"result":"success"}
  return JsonResponse(context)