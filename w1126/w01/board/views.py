from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator

def blist(request):
    npage = int(request.GET.get("npage", 1))  # 넘어온 현재 페이지 >> 여기서 npage를 처음 정의
    qs = Board.objects.all().order_by("-bgroup", "bstep")
    # 하단 페이지 처리(넘버링)
    paginator = Paginator(qs, 10)  # 1페이지 10개
    blist = paginator.get_page(npage) # paginator로 자른 page 중 npage의 것을 blist로 가져옴
    context = {"blist": blist, "npage": npage} # npage를 넘겨줌
    return render(request, "blist.html", context)

def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    btitle=request.POST.get('btitle')
    bcontent=request.POST.get('bcontent')
    bfile=request.FILES.get('bfile',"")
    print("파일정보 : ",bfile)
    qs =Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    context = {"w_msg":"1"}
    return render(request,'bwrite.html',context)

def bview(request,bno):
    npage = int(request.GET.get('npage',1))
    qs = Board.objects.filter(bno=bno)
    # prev_qs : bgroup이 크거나 bgroup 안에서 bstep이 작을 때 // 게시판 하단 중 제일 큰 것 상단
    # next_qs : bgroup이 작거나 bgroup 안에서 bstep이 클 때 // 게시판 상단 중 제일 작은 것 하단
    prev_qs = (Board.objects.filter(Q(bgroup__lt=qs[0].bgroup, bstep__lte=qs[0].bstep)| Q(bgroup=qs[0].bgroup, bstep__gt=qs[0].bstep)).order_by("-bgroup", "bstep").first())
    next_qs = Board.objects.filter(Q(bgroup__gt=qs[0].bgroup, bstep__gte=qs[0].bstep)| Q(bgroup=qs[0].bgroup, bstep__lt=qs[0].bstep)).order_by("bgroup","bstep").first()
    print("prev_qs : ",prev_qs)
    print("next_qs : ",next_qs)
    day1 = datetime.replace(datetime.now(), hour=23, minute=59, second=59)
    expires = datetime.strftime(day1, "%a, %d-%b-%Y %H:%M:%S GMT")
    context = {"board": qs[0], "prev_board": prev_qs, "next_board": next_qs, "npage":npage}
    # prev_qs, next_qs 는 first함수로 1개만 지정되어 있음을 유의
    print("날짜 : ", expires)
    response = render(request, "bview.html", context)
    if request.COOKIES.get("cookie_boardNo") is not None:
        cookies = request.COOKIES.get('cookie_boardNo')
        cookies_list = cookies.split("|")
        if str(bno) not in cookies_list:
            response.set_cookie("cookie_boardNo",cookies+f"|{bno}",expires=expires)
            qs[0].bhit += 1
            qs[0].save()
    else:
        response.set_cookie("cookie_boardNo",bno,expires=expires)
        qs[0].bhit +=1
        qs[0].save()
    return response

def bdelete(request,bno):
    Board.objects.get(bno=bno).delete()
    context = {"d_msg":bno}
    return render(request,'bview.html',context)

def bupdate(request,bno):
    if request.method=="GET":
        qs = Board.objects.filter(bno=bno)
        context = {"board":qs[0]}
        return render(request,'bupdate.html',context)
    else:
        bno = request.POST.get("bno")
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.FILES.get("bfile", "")
        qs = Board.objects.get(bno=bno)
        qs.btitle=btitle
        qs.bcontent=bcontent
        if bfile:
          qs.bfile=bfile
        qs.save()
        context = {"u_msg": bno}
        return render(request, "bupdate.html", context)

def breply(request,bno):
    if request.method == "GET":
        qs = Board.objects.filter(bno=bno)
        context = {"board": qs[0]}
        return render(request, "breply.html", context)
    else:
        bno = request.POST.get("bno")
        id = request.session.get("session_id")
        member = Member.objects.get(id=id)
        bgroup = int(request.POST.get("bgroup"))
        bstep = int(request.POST.get("bstep"))
        bindent = int(request.POST.get("bindent"))
        # bgroup 내 모든 step들을 찾아서 +1
        qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        qs.update(bstep=F('bstep')+1)
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.FILES.get("bfile", "")
        Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile,\
                             bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)
        context = {"r_msg": bno}
        return render(request, "breply.html", context)
