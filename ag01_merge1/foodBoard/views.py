from django.shortcuts import render,redirect
from foodBoard.models import fBoard
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import Q
from member.models import Star
from django.http.response import JsonResponse

def foodList(request):
    if request.method == "GET":
        id = request.session.get("session_id")
        bLocation = request.GET.get("bLocation", "")
        npage = int(request.GET.get("npage", 1))

        # 조건 1: bLocation 필터링
        qs = fBoard.objects.all()
        if bLocation != "":
            qs = qs.filter(bLocation__icontains=bLocation)

        # 조건 2: 회원의 즐겨찾기 여부 확인
        member = None
        if id:
            member = Member.objects.filter(id=id).first()

        # 즐겨찾기 O인 게시글 정렬
        if member:
            star_qs = qs.filter(starred_by__member=member).order_by("-bDate")
            non_star_qs = qs.exclude(starred_by__member=member).order_by("-bDate")
        else:
            star_qs = fBoard.objects.none()
            non_star_qs = qs.order_by("-bDate")

        # 조건 3: 두 쿼리셋 합치기
        combined_qs = list(star_qs) + list(non_star_qs)

        # 페이징 처리
        paginator = Paginator(combined_qs, 8)
        flist = paginator.get_page(npage)

        # 각 게시글별 즐겨찾기 여부 확인 및 context에 추가
        for f in flist:
            if member:
                f.star = Star.objects.filter(member=member, fboard=f).exists()
                f.is_liked = f.like_members.filter(id=member.id).exists()
            else:
                f.star = False
                f.is_liked = False
            f.like_count = f.like_members.count()
            
        context = {"flist": flist, "npage": npage}
        return render(request, "foodList.html", context)

    else:
        npage = int(request.POST.get("npage", 1))
        foodOption = request.POST.get("foodOption", "")
        foodKeyword = request.POST.get("foodKeyword")

        # 필터링 조건에 따른 쿼리셋 설정
        if foodOption == "":
            qs = fBoard.objects.filter(bTitle__icontains=foodKeyword)
        elif foodOption == "지역":
            qs = fBoard.objects.filter(bLocation__icontains=foodKeyword)
        elif foodOption == "제목+내용":
            qs = fBoard.objects.filter(
                Q(bTitle__icontains=foodKeyword)
                | Q(bSubtitle__icontains=foodKeyword)
                | Q(bContent__icontains=foodKeyword)
            )
        elif foodOption == "작성자":
            qs = fBoard.objects.filter(member__nickname__icontains=foodKeyword)

        qs = qs.order_by("-bDate")

        # 페이징 처리
        paginator = Paginator(qs, 8)
        flist = paginator.get_page(npage)

        # 회원 여부 확인 및 각 게시글별 즐겨찾기 여부 설정
        id = request.session.get("session_id")
        member = None
        for f in flist:
            if member:
                f.star = Star.objects.filter(member=member, fboard=f).exists()
                f.is_liked = f.like_members.filter(id=member.id).exists()
            else:
                f.star = False
                f.is_liked = False
            f.like_count = f.like_members.count()

        context = {"flist": flist, "npage": npage}
        return render(request, "foodList.html", context)

def Stars(request):
    id = request.POST.get("id")
    bNo = request.POST.get("bNo")
    member = Member.objects.filter(id=id).first()
    fboard = fBoard.objects.filter(bNo=bNo).first()
    qs = Star.objects.filter(member=member, fboard=fboard)
    if qs:
        qs.delete()
    else:
        Star.objects.create(member=member, fboard=fboard)
    context = {"result": "1"}
    print(context)
    return JsonResponse(context)


def Likes(request):
    id = request.POST.get("id")
    bNo = request.POST.get("bNo")
    member = Member.objects.filter(id=id).first()
    fboard = fBoard.objects.filter(bNo=bNo).first()
  
    if fboard.like_members.filter(pk=id).exists():
        fboard.like_members.remove(member)
        result = "remove" # 좋아요 취소
    else:
        fboard.like_members.add(member)
        result="add" #좋아요 추가
    context = {"result":result}
    return JsonResponse(context)

def foodView(request,bNo):
    id = request.session.get("session_id")
    member = Member.objects.filter(id=id).first()
    qs = fBoard.objects.filter(bNo=bNo).first()
    qs.star = Star.objects.filter(member=member, fboard=qs).exists()
    qs.is_liked = qs.like_members.filter(id=member.id).exists()
    qs.like_count = qs.like_members.count()
    context = {"flist": qs}
    return render(request, "foodView.html",context)


def foodFind(request):
    return render(request, "foodFind.html")


def foodRes(request,bNo):
    qs = fBoard.objects.filter(bNo=bNo)
    context = {"flist": qs[0]}
    return render(request, "foodRes.html", context)

def foodWrite(request):
    if request.method == "GET":
        return render(request,'foodWrite.html')
    else:
        id = request.session.get('session_id')
        member = Member.objects.filter(id=id)
        bLocation = request.POST.get('bLocation')
        bTitle = request.POST.get("bTitle")
        bSubtitle = request.POST.get("bSubtitle")
        bContent = request.POST.get("bContent")
        bFile1 = request.FILES.get("bFile1")
        bFile2 = request.FILES.get("bFile2")
        bFile3 = request.FILES.get("bFile3")
        qs = fBoard(member=member[0],bLocation=bLocation,bTitle=bTitle, bSubtitle=bSubtitle,bContent=bContent,bFile1=bFile1,bFile2=bFile2,bFile3=bFile3)
        qs.save()
        return redirect('/foodBoard/foodList/')
