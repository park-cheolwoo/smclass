from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import F
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.
def blist(request):
  npage = int(request.GET.get('npage',1))
  qs = Board.objects.all().order_by("-bgroup","bstep")
  paginator = Paginator(qs,10)
  blist = paginator.get_page(npage)
  context = {"blist":blist,"npage":npage}
  return render(request,"blist.html",context)

def bwrite(request):
    if request.method == "GET":
        return render(request, "bwrite.html")
    else:
        id = request.session.get("session_id")
        member = Member.objects.get(id=id)
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.FILES.get("bfile", "")
        print("파일 정보 : ", bfile)
        qs = Board.objects.create(
            member=member, btitle=btitle, bcontent=bcontent, bfile=bfile
        )
        qs.bgroup = qs.bno
        qs.save()
        context = {"w_msg": "1"}
        return render(request, "bwrite.html", context)


def bview(request,bno):
    qs = Board.objects.filter(bno=bno)
    # prev_qs : bgroup이 크거나 bgroup 안에서 bstep이 작을 때 // 게시판 하단 중 제일 큰 것 상단
    # next_qs : bgroup이 작거나 bgroup 안에서 bstep이 클 때 // 게시판 상단 중 제일 작은 것 하단
    prev_qs = (Board.objects.filter(Q(bgroup__lt=qs[0].bgroup, bstep__lte=qs[0].bstep)| Q(bgroup=qs[0].bgroup, bstep__gt=qs[0].bstep)).order_by("-bgroup", "bstep").first())
    next_qs = Board.objects.filter(Q(bgroup__gt=qs[0].bgroup, bstep__gte=qs[0].bstep)| Q(bgroup=qs[0].bgroup, bstep__lt=qs[0].bstep)).order_by("bgroup","bstep").first()
    print("prev_qs : ",prev_qs)
    print("next_qs : ",next_qs)
    day1 = datetime.replace(datetime.now(), hour=23, minute=59, second=59)
    expires = datetime.strftime(day1, "%a, %d-%b-%Y %H:%M:%S GMT")
    context = {"board":qs[0], "prev_qs":prev_qs, "next_qs":next_qs}
    response = render(request,'bview.html',context)
    if request.COOKIES.get("board"):
        cookies = request.COOKIES.get("board")
        cookie = cookies.split("|")
        if str(bno) not in cookie:
            qs.update(bhit=F("bhit") + 1)
            response = render(request,'bview.html',context)
            response.set_cookie("board",cookies+f"{bno}|" ,expires=expires)
        else : 
            context = {"board": qs[0], "prev_qs": prev_qs, "next_qs": next_qs}
            response = render(request, "bview.html", context)
    else : 
        context = {"board": qs[0], "prev_qs": prev_qs, "next_qs": next_qs}
        response.set_cookie("board",f"{bno}|" ,expires=expires)

    return response

def bdelete(request,bno):
  Board.objects.get(bno=bno).delete()
  context = {"d_msg":bno}
  return render(request,'bview.html',context)

def bupdate(request,bno):
    if request.method == "GET":
        qs = Board.objects.filter(bno=bno)
        context = {"board": qs[0]}
        return render(request, "bupdate.html", context)
    else:
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.FILES.get("bfile", "")
        qs = Board.objects.filter(bno=bno)
        if qs:
           qs[0].btitle=btitle
           qs[0].bcontent=bcontent
           qs[0].bfile=bfile
           qs[0].save()
           context = {"u_msg":"1"}
        return render(request,'bupdate.html',context)

def breply(request,bno):
   if request.method == "GET":
      qs = Board.objects.filter(bno=bno)
      context = {"board":qs[0]}
      return render(request,'breply.html',context)
   else : 
      id = request.session.get('session_id')
      member = Member.objects.filter(id=id)
      btitle = request.POST.get('btitle')
      bcontent = request.POST.get('bcontent')
      bfile = request.FILES.get('bfile',"")
      bgroup = int(request.POST.get('bgroup'))
      bstep = int(request.POST.get('bstep'))
      bindent = int(request.POST.get('bindent'))
      qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
      qs.update(bstep=F('bstep')+1)
      Board.objects.create(member=member[0],btitle=btitle,bcontent=bcontent,bfile=bfile\
                            ,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)
      context = {"r_msg":"1"}
      return render(request,'breply.html',context)
