from django.shortcuts import render
from board.models import Board
from comment.models import Comment
from member.models import Member
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView, DetailView


## form
def form(request):
  if request.method == "GET":
    return render(request,'form.html')
  else:
    file1 = request.FILES.get('bfile')
    print("file1 : ",file1)
    file_list = request.FILES.getlist('bfile')
    print("파일 : ",file_list)
    return HttpResponse(file_list) 


## 상세보기
# def bview(request,bno):
# id = request.session.get('session_id')
# member = Member.objects.get(id=id)
# qs = Board.objects.filter(bno=bno).first()
# ##
# if qs.like_members.filter(pk=id).exists():
#     result = "1"
# else :
#     result = "0"
# count = qs.like_members.count()


# 하단댓글가져오기
# c_qs = Comment.objects.filter(board=qs).order_by("-cno")
# print("확인 : ",c_qs,c_qs.count)
# context = {"board":qs,"clist":c_qs,"result":result,"count":count}
# return render(request,'bview.html',context)


## 게시판리스트
# def blist(request):
#   qs = Board.objects.all().order_by("-bgroup","bstep")
#   context = {"blist":qs}
#   return render(request,'blist.html',context)

class BoardListView(ListView):
    model=Board
    template_name='blist.html'
    ordering='-bno'


class BoardDetailView(DetailView): # CBV 작성 방법
    model=Board
    template_name='bview.html'


# 좋아요, board,member 3번게시글 aaa, 3번 bbb, 1번 aaa
def likes(request):
  id = request.session.get('session_id')
  member = Member.objects.get(id=id)
  bno = request.POST.get('bno')
  board = Board.objects.get(bno=bno)

  # 저장
  # 좋아요 클릭을 했는지 확인
  if board.like_members.filter(pk=id).exists():
    board.like_members.remove(member)
    result = "remove" # 좋아요 취소
  else:
    board.like_members.add(member)
    result="add" #좋아요 추가

  print("좋아요 개수 확인 : ",board.like_members.count())
  context = {"result":result,"count":board.like_members.count()}
  return JsonResponse(context)
