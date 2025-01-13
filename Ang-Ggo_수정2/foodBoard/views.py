from django.shortcuts import render,redirect
from foodBoard.models import fBoard,fTime
from django.core.paginator import Paginator
from member.models import Member,Star,Rating,Reservation
from django.db.models import Q,Avg
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
        if member:
            star = Star.objects.filter(member=member)
            star_values = star.values_list("fboard__bNo", flat=True)
            star_qs = qs.filter(bNo__in=star_values).order_by("-bDate")
            non_star_qs = qs.exclude(bNo__in=star_values).order_by("-bDate")
        else: # 비로그인 시
            star_qs = fBoard.objects.none()
            non_star_qs = qs.order_by("-bDate")

        # 조건 3: 두 쿼리셋 합치기
        combined_qs = list(star_qs) + list(non_star_qs)

        # 페이징 처리
        paginator = Paginator(combined_qs, 8)
        flist = paginator.get_page(npage)
        # 각 게시글별 즐겨찾기/좋아요 여부 확인 및 context에 추가
        for f in flist:
            if member:
                f.star = Star.objects.filter(member=member, fboard=f).exists()
                f.is_liked = f.like_members.filter(id=id).exists()
            else:
                f.star = False
                f.is_liked = False
            f.like_count = f.like_members.count()

        context = {"flist": flist, "npage": npage, "bLocation": bLocation}
        return render(request, "foodList.html", context)

    else:
        id = request.session.get("session_id")
        npage = int(request.POST.get("npage", 1))
        foodOption = request.POST.get("foodOption", "")
        foodKeyword = request.POST.get("foodKeyword")
        print("Option:", foodOption)
        print("Keyword:", foodKeyword)

        # 조건1. 검색 조건 필터링
        if foodOption == "":
            qs = fBoard.objects.filter(bTitle__icontains=foodKeyword)
        elif foodOption == "지역":
            qs = fBoard.objects.filter(bLocation__icontains=foodKeyword)
            print(qs)
        elif foodOption == "제목+내용":
            qs = fBoard.objects.filter(Q(bTitle__icontains=foodKeyword) | Q(bSubtitle__icontains=foodKeyword) | Q(bContent__icontains=foodKeyword))
        elif foodOption == "작성자":
            qs = fBoard.objects.filter(member__nickname__icontains=foodKeyword)

        qs = qs.order_by("-bDate")

        # 조건 2: 회원의 즐겨찾기 여부 확인
        member = None
        if id:
            member = Member.objects.filter(id=id).first()
        if member:
            star = Star.objects.filter(member=member)
            star_values = star.values_list("fboard__bNo", flat=True)
            star_qs = qs.filter(bNo__in=star_values).order_by("-bDate")
            # member가 즐겨찾기한 게시글 조회
            non_star_qs = qs.exclude(bNo__in=star_values).order_by("-bDate")
            # member가 즐겨찾기한 게시글 제외 후 조회
            non_star_qs = qs.exclude(
                bNo__in=star.values_list("fboard__bNo", flat=True)
            ).order_by("-bDate")
            # member가 즐겨찾기한 게시글 제외 후 조회
        else:  # 비로그인 시
            star_qs = fBoard.objects.none()
            non_star_qs = qs.order_by("-bDate")

        # 조건 3: 두 쿼리셋 합치기
        combined_qs = list(star_qs) + list(non_star_qs)

        # 페이징 처리
        paginator = Paginator(qs, 8)
        flist = paginator.get_page(npage)

        # 회원 여부 확인 및 각 게시글별 즐겨찾기/좋아요 여부 설정
        member = None
        for f in flist:
            if member:
                f.star = Star.objects.filter(member=member, fboard=f).exists()
                f.is_liked = f.like_members.filter(id=id).exists()
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
        result = "remove"  # 좋아요 취소
    else:
        fboard.like_members.add(member)
        result = "add"  # 좋아요 추가
    context = {"result": result}
    return JsonResponse(context)


def foodView(request, bNo):
    # foodView 페이지 열기
    if request.method == "GET":
        id = request.session.get("session_id")
        member = Member.objects.filter(id=id).first()
        # fboard = fBoard.objects.filter(bNo=bNo)
        qs = fBoard.objects.filter(bNo=bNo).first()
        fTime2 = fTime.objects.filter(fboard=qs)
        # 댓글(반응) 기록 조회
        rating_counts = Rating.objects.filter(fboard=qs)
        ratings = Rating.objects.filter(fboard=qs, member=member)
        rate_list = []
        rate_count = []
        if ratings:
            for f in ratings:
                rate_list.append(f.rating)
        print(rate_list) # 회원이 남긴 반응 리스트

        if rating_counts:
            for i in range(1, 10):  # 1부터 9까지의 rating 값에 대해 카운트
                count = rating_counts.filter(rating=i).count() or 0
                print(f"{i}번 반응 : "+str(count)+"회")
                rate_count.append(count)
        else:
            rate_count = [0, 0, 0, 0, 0, 0, 0, 0, 0] # rating 값이 없으면 0으로 고정

        # 시간별 평균 대기시간 조회
        labels = []
        times = []
        counts = []
        for hour in range(0, 24):
            data = fTime.objects.filter(fboard=qs, fDate__hour=hour)
            if not data:
                # 데이터가 없으면 0으로 처리
                labels.append(hour)
                times.append(0)
                counts.append(0)
            else:
                # 데이터가 1개라도 있으면 아래의 함수를 실행
                AvgData = data.aggregate(Avg("fTime"))["fTime__avg"] or 0
                try:
                    # 평균을 계산해서 정수 변환
                    AvgData = int(AvgData)
                except:
                    # 그 시간대의 데이터가 없으면 0으로 처리
                    AvgData = 0
                count = data.count()
                if not count:
                    count = 0
                labels.append(hour)
                times.append(AvgData)
                counts.append(count)
        # 즐겨찾기 기능 조회
        qs.star = Star.objects.filter(member=member, fboard=qs).exists()
        qs.is_liked = qs.like_members.filter(id=id).exists()
        qs.like_count = qs.like_members.count()
        # 평균 대기시간 조회
        TimeAvg = fTime2.aggregate(Avg("fTime"))["fTime__avg"]
        if TimeAvg is not None:
            TimeAvg = int(TimeAvg)
        else:
            TimeAvg = 0
        # 현재 날짜 조회 후 문자 변환
        now = datetime.datetime.now().strftime("%y-%m-%d")

        context = {
            "flist": qs,
            "TimeAvg": TimeAvg,
            "labels": labels,
            "times": times,
            "counts": counts,
            "rate_list": rate_list,
            "rate_count": rate_count,
            "now": now,
        }
        print("times : ", times)
        print("counts : ", counts)
        print("labels : ", labels)
        return render(request, "foodView.html", context)

    else:
        # foodView 평균 대기시간 투표 기능
        id = request.session.get("session_id")
        bNo = request.POST.get("bNo")
        # 아이디 로그인이나 게시물 번호가 없을 경우 투표 불가
        if not id or not bNo:
            print('아이디나 게시물번호가 없음')
            context = {"result": "2"}
            response = render(request, "foodView.html", context)
        elif f"votetime{bNo}" in request.COOKIES:
            print("중복 투표 확인")
            # 중복 투표 방지(당일 자정에 투표 기회 초기화)
            if request.COOKIES[f"votetime{bNo}"] == f"id : {id}, bNo : {bNo}":
                context = {"result": "0", "bNo": bNo}
                response = render(request, "foodView.html", context)
        else:
            # 투표를 한 적이 없다면
            id = request.session.get("session_id")
            member = Member.objects.filter(id=id).first()
            bNo = request.POST.get("bNo")
            fBoard2 = fBoard.objects.filter(bNo=bNo).first()
            fDate = None
            fPeople = request.POST.get("fPeople")
            fTime2 = request.POST.get("waitselect")
            select = request.POST.get("enterselect")
            if select == "0":
                # 입장 시간이 지금 이라면
                fDate = datetime.datetime.now().time()
            elif select == "1":
                # 입장 시간이 직접 입력 이라면
                # 오전 오후 구분
                category = request.POST.get("timeselect")
                hour = 0
                minute = 0
                if category == "AM":
                    hour = int(request.POST.get("hour"))
                    if hour < 10:
                        # 0~9시는 00~09로 변환
                        hour = int("0" + str(hour))
                if category == "PM":
                    hour = int(request.POST.get("hour")) + 12
                    # 오후 12시는 자정이 아닌 정오로 변환
                    if hour == 24:
                        hour = 12
                minute = int(request.POST.get("minute"))
                # 0~9분은 00~09로 변환
                if minute < 10:
                    minute = int("0" + str(minute))
                # 초는 0으로 고정
                second = 0
                fDate = datetime.time(hour, minute, second)
            context = {"result": "1", "bNo": bNo}
            response = render(request, "foodView.html", context)
            # 투표 후 쿠키 유효시간 설정
            expires = datetime.datetime.now().replace(hour=23, minute=59, second=59)
            # 투표 기록 쿠키에 저장
            response.set_cookie(f"votetime{bNo}", f"id : {id}, bNo : {bNo}", expires=expires)
            fTime.objects.create(
                member=member,
                fboard=fBoard2,
                fPeople=fPeople,
                fTime=fTime2,
                fDate=fDate,
            )
    return response


def foodFind(request):
    return render(request, "foodFind.html")


def foodRes(request,bNo):
    if request.method == "GET":
        qs = fBoard.objects.filter(bNo=bNo).first()
        context = {"flist": qs}
        return render(request, "foodRes.html", context)
    else:
        bNo = request.POST.get("bNo")
        id = request.session.get("session_id")
        member = Member.objects.filter(id=id).first()
        resPeople = request.POST.get("resPeople")
        # resTel = request.POST.get("resTel")
        # resDate = request.POST.get("resDate")
        resMemo = request.POST.get("resMemo")
        qs = fBoard.objects.filter(bNo=bNo).first()
        qs2 = Reservation.objects.create(res=member, resPeople=resPeople, resMemo=resMemo)
        print(qs2)
        context = {"result": "1"}
        return render(request, "foodRes.html", context)


def foodWrite(request):
    if request.method == "GET":
        return render(request,'foodWrite.html')
    else:
        id = request.session.get('session_id')
        member = Member.objects.filter(id=id).first()
        bLocation = request.POST.get('bLocation')
        bTitle = request.POST.get("bTitle")
        bSubtitle = request.POST.get("bSubtitle")
        bContent = request.POST.get("bContent")
        bFile1 = request.FILES.get("bFile1")
        bFile2 = request.FILES.get("bFile2")
        bFile3 = request.FILES.get("bFile3")
        qs = fBoard(member=member,bLocation=bLocation,bTitle=bTitle, bSubtitle=bSubtitle,bContent=bContent,bFile1=bFile1,bFile2=bFile2,bFile3=bFile3)
        qs.save()
        context={"result":"1"}
        return render(request,'foodWrite.html',context)


def Ratings(request):
    id = request.session.get("session_id")
    member = Member.objects.filter(id=id).first()
    bNo = request.POST.get("bNo")
    fboard = fBoard.objects.filter(bNo=bNo).first()
    rating = request.POST.get("rating")
    status = request.POST.get("status")
    print("id : ", id)
    print("bNO : ", bNo)
    print("rating : ", rating)
    print("status : ", status)
    if status == "1":
        print("반응 추가")
        qs = Rating.objects.filter(member=member, fboard=fboard, rating=rating)
        if not qs:
            Rating.objects.create(member=member, fboard=fboard, rating=rating)
            context = {"result": "1", "status": "1"}
            return JsonResponse(context)
        else:
            print("반응 추가 에러 발생")
    elif status == "0":
        print("반응 삭제")
        qs = Rating.objects.filter(member=member, fboard=fboard, rating=rating).first()
        if qs:
            qs.delete()
            context = {"result": "1", "status": "0"}
            return JsonResponse(context)
        else:
            print("반응 삭제 에러 발생")


def foodDelete(request):
    bNo = request.POST.get("bNo")
    qs = fBoard.objects.filter(bNo=bNo).first()
    if qs:
        qs.delete()
        context = {"result": "3"}
    else : context = {"result":"4"}
    return JsonResponse(context)

def foodUpdate(request,bNo):
    if request.method == "GET":
        print(bNo)
        qs = fBoard.objects.filter(bNo=bNo).first()
        print(qs)
        context = {"flist": qs, "bNo": bNo}
        return render(request, "foodUpdate.html", context)
    else: 
        bNo = request.POST.get("bNo")
        bLocation = request.POST.get("bLocation")
        bTitle = request.POST.get("bTitle")
        bSubtitle = request.POST.get("bSubtitle")
        bContent = request.POST.get("bContent")
        print("bNo : ", bNo)
        print("bLocation : ", bLocation)
        print("bTitle : ", bTitle)
        print("bSubtitle : ", bSubtitle)
        print("bContent : ", bContent)

        qs = fBoard.objects.filter(bNo=bNo).first()
        print(qs)
        qs.bLocation = bLocation
        qs.bTitle = bTitle
        qs.bSubtitle = bSubtitle
        qs.bContent = bContent
        qs.save()
        context = {"result": "1", "bNo": bNo}
        return render(request,"foodUpdate.html", context)

def foodDelete(request,bNo):
    bNo = request.POST.get("bNo")
    print(bNo)
    qs = fBoard.objects.filter(bNo=bNo).first()
    print(qs)
    if qs:
        fTime.objects.filter(fboard=qs).delete() # 웨이팅 시간 데이터 삭제
        Rating.objects.filter(fboard=qs).delete() # 반응 데이터 삭제
        qs.delete()
        context = {"result": "3"}
    else:
        context = {"result": "4"}
    return JsonResponse(context)


def getImages(request):
    print("getImages 시작")
    id = request.session.get("session_id")
    member = Member.objects.filter(id=id).first()
    pKey = request.GET.get("pKey")
    print("pKey : ", pKey)
    qs = fBoard.objects.filter(pKey=pKey).first()
    bNo = qs.bNo
    print("qs : ", qs)
    # 로그인시 반응 추가유무, 반응 기능 추가
    # 비로그인시 반응 추가 불가능

    rating_counts = Rating.objects.filter(fboard=qs)
    if member:
        ratings = Rating.objects.filter(fboard=qs, member=member)

    # rate_list : {"1":"1번 반응", "2":"2번 반응", ...}
    # rate_count : {"1":"1번 반응 카운트", "2":"2번 반응 카운트", ...}

    rate_list = []
    rate_count = []
    if ratings:
        for f in ratings:
            rate_list.append(f.rating)
    print(rate_list) # 회원이 남긴 반응 리스트

    if rating_counts:
        for i in range(1, 10):  # 1부터 9까지의 rating 값에 대해 카운트
            count = rating_counts.filter(rating=i).count() or 0
            print(f"{i}번 반응 : "+str(count)+"회")
            rate_count.append(count)
    else:
        rate_count = [0, 0, 0, 0, 0, 0, 0, 0, 0] # rating 값이 없으면 0으로 고정

    TimeAvg = fTime.objects.filter(fboard=qs).aggregate(Avg("fTime"))["fTime__avg"]
    if TimeAvg is not None:
        TimeAvg = int(TimeAvg)
    else:
        TimeAvg = -1

    if qs:
        context = {"result": "1", "bFile1": qs.bFile1.url, "bFile2": qs.bFile2.url, "bFile3": qs.bFile3.url, "TimeAvg": TimeAvg,\
                    "rate_list": rate_list, "rate_count": rate_count, "bNo": bNo} # rate_list : 회원이 남긴 반응, rate_count : 반응 카운트
        print("rate_list : ", rate_list)
        print("rate_count : ", rate_count)
    else:
        context = {"result": "0"}
    return JsonResponse(context)


def addPkey(request):
        # pKey 의 list
    plist = [1114356301, 1040638501, 1093486001, 1104585101, 1134911301, 1137459301, 226314801, 1036699701, 581844301, 568556401, 1039723801, 539474201, 681503501, 1180605601, 299389301, 151146001, 226076800, 275446100, 151147201, 1089199001, 151146001, 236561100]
        #bTitle 의 list
    nlist = ["커피사피엔스 가산 한라원앤원점", "인크커피 가산점", "원두서점", "파란만잔 가산한라원앤원점", "이에노", "파더스베이글 가산디지털단지점", "피오니", "커피 벌스데이", "피오니 연남점", "1984", "산리오러버스클럽", "딥커피", "테일러커피 연남1호점", "씨더라이트", "콘하스 연남점", "Tora.b", "위드커피", "앤트러사이트 합정점", "퐁포네뜨", "오퍼", "위드커피", "더카페 가산이노플렉스점"]
    print("시작")
    for i in nlist:
        print("i : ", i)
        qs = fBoard.objects.filter(bTitle=i).first()
        print("qs.title : ", qs.bTitle)
        if qs:
            qs.pKey = plist[nlist.index(i)]
            print(qs.pKey)
            qs.save()
    print("완료")


