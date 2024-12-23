from django.shortcuts import render,redirect
from foodBoard.models import fBoard,fTime
from django.core.paginator import Paginator
from member.models import Member,Rating
from django.db.models import Q,Avg
from member.models import Star
from django.http.response import JsonResponse
import datetime


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
            star_qs = qs.filter(star_fboard__member=member).order_by("-bDate")
            non_star_qs = qs.exclude(star_fboard__member=member).order_by("-bDate")
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
    if request.method == "GET":
        id = request.session.get("session_id")
        member = Member.objects.filter(id=id).first()
        # fboard = fBoard.objects.filter(bNo=bNo)
        qs = fBoard.objects.filter(bNo=bNo).first()
        fTime2 = fTime.objects.filter(fBoard=qs)
        rating_counts = Rating.objects.filter(fboard=qs)
        ratings = Rating.objects.filter(fboard=qs,member=member)
        rate_list = []
        rate_count = []
        if ratings:
           for f in ratings:
              rate_list.append(f.rating)
        print(rate_list)

        if rating_counts: 
            for i in range(1, 10): # 1부터 9까지의 rating 값에 대해 카운트
                count = rating_counts.filter(rating=i).count() or 0
                rate_count.append(count)
        
        labels = []
        times = []
        counts = []
        for hour in range(0,24):
            data = fTime.objects.filter(fBoard=qs,fDate__hour=hour)
            if not data:
                labels.append(hour)
                times.append(0)
                counts.append(0)
            else:
                AvgData = data.aggregate(Avg("fTime"))["fTime__avg"] or 0
                try:AvgData=int(AvgData)
                except:AvgData=0
                count = data.count()
                if not count : count=0
                labels.append(hour)
                times.append(AvgData)
                counts.append(count)
        qs.star = Star.objects.filter(member=member, fboard=qs).exists()
        qs.is_liked = qs.like_members.filter(id=member.id).exists()
        qs.like_count = qs.like_members.count()
        TimeAvg = fTime2.aggregate(Avg("fTime"))["fTime__avg"]
        if TimeAvg is not None: 
            TimeAvg = int(TimeAvg) 
        else: 
            TimeAvg = 0
        now = datetime.datetime.now().strftime("%y-%m-%d")
        
        context = {"flist": qs,"TimeAvg":TimeAvg,"labels":labels,"times":times,"counts":counts, "rate_list":rate_list,\
                    "rate_count":rate_count,"now":now}
        return render(request, "foodView.html",context)

    else:
        if 'votetime' in request.COOKIES: 
            id = request.session.get('id')
            bNo = request.POST.get('bNo') 
            votetime = f"id: {id}, bNo: {bNo}"
            if id is None or bNo is None:
                context = {"result": "2"}
                return render(request,context,'foodView.html')  
            elif request.COOKIES.get('votetime') == votetime: 
                context = {"result": "0", "bNo":bNo} 
                print(context)
                return render(request, "foodView.html", context)
        else:
            id = request.session.get('session_id')
            member = Member.objects.filter(id=id).first()
            bNo = request.POST.get('bNo')
            fBoard2 = fBoard.objects.filter(bNo=bNo).first()
            fDate = None
            fPeople = request.POST.get('fPeople')
            fTime2 = request.POST.get('waitselect')
            select = request.POST.get("enterselect")
            if select == "0":
                fDate = datetime.datetime().now().time()
            elif select == "1":
                category = request.POST.get("timeselect")
                hour=0
                minute=0
                if category == "AM":
                    hour = int(request.POST.get('hour'))
                    if hour < 10 :
                        hour = int("0" + str(hour))
                if category == "PM":
                    hour = int(request.POST.get('hour'))+12
                    if hour == 24: hour = 12
                minute = int(request.POST.get('minute'))
                if minute <10:
                    minute = int("0" + str(minute))
                second=0
                fDate = datetime.time(hour, minute,second)
            context = {"result":"1","bNo":bNo}
            response = render(request, "foodView.html", context)
            expires = datetime.datetime.now().replace(hour=23,minute=59,second=59)
            response.set_cookie('votetime',f"id : {id}, bNo : {bNo}",expires=expires)
            fTime.objects.create(member=member,fBoard=fBoard2,fPeople=fPeople,fTime=fTime2,fDate=fDate)
            return response

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

def Ratings(request):
    id = request.session.get('session_id')
    member = Member.objects.filter(id=id).first()
    bNo = request.POST.get('bNo')
    fboard = fBoard.objects.filter(bNo=bNo).first()
    rating = request.POST.get('rating')
    status = request.POST.get('status')
    print("id : ",id)
    print("bNO : ",bNo)
    print("rating : ",rating)
    print("status : ",status)
    if status =="1":
        print("반응 추가")
        qs = Rating.objects.filter(member=member,fboard=fboard,rating=rating)
        if not qs:
            Rating.objects.create(member=member,fboard=fboard,rating=rating)
            context ={"result":"1","status":"1"}
            return JsonResponse(context)
        else: print("반응 추가 에러 발생")
    elif status == "0":
        print("반응 삭제")
        qs = Rating.objects.filter(member=member,fboard=fboard,rating=rating).first()
        if qs:
            qs.delete()
            context ={"result":"1","status":"0"}
            return JsonResponse(context)
        else: print("반응 삭제 에러 발생")
