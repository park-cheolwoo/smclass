from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

# Create your views here.
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  return render(request,'blist.html',{"blist":qs})

def bwrite(request):
  if request.method == "GET":
   return render(request,'bwrite.html')
  else : 
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    # no = Board.objects.aggregate(max_no = Max("bno"))
    # no['max_bno']+1
    # 오라클 : sequence.nextval, sequence.currval
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    # bno/bdate - 자동 id/btitle/bcontent/bgroup - 입력 bstep/bindent/bhit - default
    qs.bgroup = qs.bno
    qs.save()
    # messages.success(request,message='게시글이 저장되었습니다.')
    return render(request,"bwrite.html",{"w_msg":"1"})


def bview(request,bno):
    # 1. get
    # qs = Board.objects.get(bno=bno)
    # qs.bhit += 1
    # qs.save()
    # context = {"board":qs}

    # 2. filter
    qs = Board.objects.filter(bno=bno)
    # 조회수 +1 : filter >> update()
    # qs.update() >> 검색된 모든 값에 +1을 적용시킬 수 있음
    qs.update(bhit=F('bhit')+1)
    qs[0].save()
    context = {"board":qs[0]}
    return render(request,'bview.html',context)

def bmodify(request,bno):
  if request.method == "GET":
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request,'bmodify.html',context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect("board:blist")
    return render(request,'bmodify.html',{'u_msg':bno})
  
def bdelete(request,bno):
  print("게시글 번호 : ",bno)
  Board.objects.get(bno=bno).delete()
  return render(request,'bview.html',{"d_msg":bno})

def breply(request,bno):
  if request.method == "GET":
    print("게시글 번호 : ",bno)
    qs = Board.objects.get(bno=bno)
    return render(request,'breply.html',{"board":qs})
  else:
    bgroup = int(request.POST.get("bgroup")) # str타입 >> int타입
    bstep = int(request.POST.get("bstep"))
    bindent = int(request.POST.get("bindent"))
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")

    # 다른 답변달기에 bstep을 1씩 증가시켜줌
    qs=Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)
    
    print("bgroup 정보 : ",bgroup)
    # bgroup : 부모의 bgroup 입력 / bstep : 부모의 bstep보다 +1
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup\
                               ,bstep=bstep+1,bindent=bindent+1)
    
    return render(request,'breply.html',{"r_msg":"1"})