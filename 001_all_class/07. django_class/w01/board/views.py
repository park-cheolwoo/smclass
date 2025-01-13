from django.shortcuts import render
from board.models import Board
from comment.models import Comment

def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")

  context = {"blist":qs}
  return render(request,'blist.html',context)

def bview(request,bno):
    qs = Board.objects.filter(bno=bno)
    clist = Comment.objects.filter(board=qs[0]).order_by("-cno")
    print("확인 : ",clist)
    print("확인 : ",clist.count)
    context = {"board": qs[0],"clist":clist}
    return render(request, "bview.html", context)
