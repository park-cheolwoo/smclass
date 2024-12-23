from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from member.models import Member
from event.models import Attendance
from coupon.models import Coupon
from datetime import date
from django.db.models import F


# 출석체크, 10p 앙포인트, 응모권 지급 (test) => 오류 ~_~


# <<중복인 view라 임시 주석 처리>>
# def calendar(request):
#   # 미로그인 페이지 오픈
#   if request.method == "GET":
#     id = request.session.get('session_id')
#     print(id)
#     member = Member.objects.filter(id=id).first()
#     qs = Attendance.objects.filter(member=member).first()
#     if qs:
#       context = {"count":qs.count,"aTicket":qs.aTicket,"usedTicket":qs.usedTicket,"point":member.point}
#       # filter().first() >> 1개만 불러오는 함수이므로 qs[0]이 아닌 qs로 수정
#     else:
#       context = {"count":0,"aTicket":0,"usedTicket":0,"point":0}
#     return render(request, 'calendar.html',context)
#   else:
#     # 세션에서 id 가져오기
#     id = request.session.get('session_id')
#     # Member 객체 가져오기 (Member.point 정보 필요함)
#     member= Member.objects.filter(id=id).first()
#     today = date.today() # 오늘 날짜 today에 저장
#     print(id,today)

#     # Attendance 객체 가져오기 (사용자별로 출석 기록을 가져옴)
#     qs = Attendance.objects.filter(member=member).first()

#     ## 매달 1일에 count 리셋
#     first_day_of_month = today.replace(day=1)

#     if today == first_day_of_month:
#       qs.count = 0 # 카운트 리셋
#       qs.aTicket = 0
#       qs.save()
#       print("카운트 리셋 count",qs.count)

#     # aDate과 today 비교
#     if qs:
#       if qs.aDate != today:
#         qs.aDate = today
#         # -- 검증 필요 --
#         qs.count=F(('count')+1) # 출석 횟수 추가
#         qs.aTicket=(F('aTicket')+1) # 응모권 개수 추가
#         qs.member.point=(F('point')+10) # 포인트 10p 추가
#         # -- 검증 필요 --
#         qs.save()
#         member.save()
#         context = {"result":"success","count":qs.count,"aTicket":qs.aTicket,"aPoint":qs.aPoint}
#       else:
#         context = {"result":"already_checked"}
#     else:
#       Attendance.objects.create(member=member,aDate=today,count=1,aTicket=1)
#       context = {"result":"success","count":1,"aTicket":1,"aPoint":10}
#     return JsonResponse(context)


# 출석체크 및 응모권 지급 까지만 되는 함수
def calendar(request):
  # 출석체크 페이지 오픈
  if request.method == "GET":
    id = request.session.get('session_id')
    #print("id: ",id)
    member = Member.objects.filter(id=id).first()
    #print("member: ",member)
    if member:
      qs = Attendance.objects.filter(member=member).first()
      if qs:
        #print("qs: ",qs)
        context = {"count":qs.count,"aTicket":qs.aTicket,"usedTicket":qs.usedTicket}
      else:
        context = {"count":0,"aTicket":0,"usedTicket":0}
    else:
      context = {"count":0,"aTicket":0,"usedTicket":0}
    return render(request, 'calendar.html',context)

  else:
    #print("출석체크 시도")
    # 세션에서 aId 가져오기
    id = request.session.get('session_id')
    today = date.today() # 오늘 날짜 today에 저장
    member = Member.objects.filter(id=id).first()
    #print("member: ",member)
    #print("today : ",today)


    ## 매달 1일에 count 리셋
    first_day_of_month = today.replace(day=1)

    # aDate과 today 비교
    # if member: // 임시 주석처리
    # Attendance 객체 가져오기 (사용자별로 출석 기록을 가져옴)
    qs = Attendance.objects.filter(member=member).first()
    # qs : member=member인 Attendance model의 객체
    if qs:
      #print("qs : ",qs)
      if today == first_day_of_month:
        qs.count = 0 # 카운트 리셋
        qs.aTicket = 0
        qs.save()
        #print("카운트 리셋 count",qs.count)
        #print("aDate : "+qs.aDate)
      # Attendance의 aDate값이 없거나 오늘이 아니면
      if qs.aDate == None or qs.aDate != today:
        qs.aDate = today
        qs.save()
        qs.update(count=F('count')+1) # 출석 횟수 추가
        qs.update(aTicket=F('aTicket')+1) # 응모권 개수 추가
        context = {"result":"success","count":qs.count,"aTicket":qs.aTicket}
      else:
        context = {"result":"already_checked"}
    #qs가 없으면
    else:
      Attendance.objects.create(member=member,aDate=today,count=1,aTicket=1) # member는 있지만 Attendance가 없는 경우 >> 이벤트 처음 참여하는 경우
      context = {"result":"success","count":1,"aTicket":1}
    return JsonResponse(context)  


# 응모권 개수 차감, 쿠폰 지급
def apply(request):
    id = request.session.get('session_id')
    member = Member.objects.filter(id=id).first()
    qs = Attendance.objects.filter(member=member).first()
    ticketDeduction = int(request.POST.get('ticketDeduction',0)) # 클라이언트에서 전송한 차감할 응모권 수
    print(qs,ticketDeduction)
    if qs: 
        if qs.aTicket < ticketDeduction:
            return JsonResponse({"result":"not_yet"}) # 응모권 부족

        else:
            ticket_count = qs.aTicket
            if ticket_count >= ticketDeduction:
                if ticketDeduction == 5:
                    # 쿠폰 지급
                    coupon = Coupon.objects.create(
            member=member,
            attendance=qs,
            discount = 1000, # 쿠폰 금액
            used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
            used_to = timezone.now()+timezone.timedelta(days=30) # 쿠폰 유효기간 30일
          )
                    print(coupon.discount) 

                elif ticketDeduction == 10:
                    # 쿠폰 지급
                    coupon = Coupon.objects.create(
            member=member,
            attendance=qs,
            discount = 3000, # 쿠폰 금액
            used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
            used_to = timezone.now()+timezone.timedelta(days=30) # 쿠폰 유효기간 30일
          )
                    print(coupon.discount)
            # qs[0].coupon_code = coupon.discount
            qs.aTicket = F("aTicket") - ticketDeduction
            qs.usedTicket = F("usedTicket") + ticketDeduction
            qs.save()
            print("aTicket : ", qs.aTicket, "usedTicket : ", qs.usedTicket)
            # 업데이트된 qs를 한번 더 호출
            qs = Attendance.objects.filter(member=member).first()
            context = {"result": "success", "aTicket": qs.aTicket, "usedTicket": qs.usedTicket}
            return JsonResponse(context)


# 럭키드로우(행운뽑기)

def luckyDraw(request):
  id = request.session.get('session_id')
  member = Member.objects.filter(id=id).first()
  qs = Attendance.objects.filter(member=member).first()
  ticketDeduction = int(request.POST.get('ticketDeduction',0)) # 클라이언트에서 전송한 차감할 응모권 수
  print(qs,ticketDeduction)
  if qs: 
    if qs.aTicket < ticketDeduction:
      return JsonResponse({"result":"not_yet"}) # 응모권 부족

    else:
      ticket_count = qs.aTicket
      if ticket_count >= ticketDeduction:
        
        # 쿠폰 지급 
        coupon = Coupon.objects.create(
          member=member,

          attendance=qs,
          discount = 5000, # 쿠폰 금액
          used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
          used_to = timezone.now()+timezone.timedelta(days=5) # 쿠폰 유효기간 30일
        )
        print(coupon.discount) 
      # qs[0].coupon_code = coupon.discount
      qs.aTicket=(F('aTicket')-ticketDeduction)
      qs.usedTicket=(F('usedTicket')+ticketDeduction)
      print("aTicket : ",qs.aTicket,"usedTicket : ",qs.usedTicket)
      qs.save()
      # 업데이트된 qs를 한번 더 호출
      qs = Attendance.objects.filter(member=member).first()
      context = {"result":"success","aTicket":qs.aTicket,"usedTicket":qs.usedTicket}
      print(qs.aTicket)
      print(qs.usedTicket)
      return JsonResponse(context)


# 쿠폰 리스트페이지
def coupon(request):
  return render(request, 'coupon.html')


# 앙포인트 페이지
def point(request):
    print("GET이어야함 : ", request.method)
    if request.method == "GET":
        id = request.session.get("session_id")
        member = Member.objects.filter(id=id).first()
        print("member : ", member)
        qs = Attendance.objects.filter(member=member).first()
        print("qs : ", qs)
        if qs:
            context = {"result": "success", "point": member.point}
        else:
            context = {"result": "notLogin", "point": 0}
        print("point : ", member.point)
        print("context : ", context)
        print(request)
        return render(request, "point.html", context)
    else:
        # 이게 없으면 httpresponse가 안되는 것 같습니다
        # 일단 GET과 동일하게 뒀습니다.
        id = request.session.get("session_id")
        member = Member.objects.filter(id=id).first()
        print("member : ", member)
        qs = Attendance.objects.filter(member=member).first()
        print("qs : ", qs)
        if qs:
            context = {"result": "success", "point": member.point}
        else:
            context = {"result": "notLogin", "point": 0}
        print("point : ", member.point)
        print("context : ", context)
        print(request)
        return render(request, "point.html", context)

    # return render(request, 'point.html')


# def event_coupon(request, aId):
#   qs = Attendance.objects.filter(aId=aId)
#   ticketDeduction = int(request.POST.get('ticketDeduction',0))

#   ticket_count = qs[0].aTicket
#   if ticket_count >= ticketDeduction:

#     # 쿠폰 지급
#     coupon = Coupon.objects.create(
#       aId=qs
#     )
#   else if :

#   return render(request, 'coupon.html')
