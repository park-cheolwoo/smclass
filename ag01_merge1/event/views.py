from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from member.models import Member
from event.models import Attendance
from coupon.models import Coupon
from datetime import date
from django.db.models import F




# 출석체크, 10p 앙포인트, 응모권 지급 (test) => 오류 ~_~
# def calendar(request):
#   # 미로그인 페이지 오픈
#   if request.method == "GET":
#     aId = request.session.get('session_id')
#     qs = Attendance.objects.filter(aId=aId)
#     member = Member.objects.filter(id=aId)
#     print("member:",member,"attendance:",qs)
#     if qs:
#       context = {"count":qs[0].count,"aTicket":qs[0].aTicket,"usedTicket":qs[0].usedTicket,"aPoint":member[0].point}
#     else:
#       context = {"count":0,"aTicket":0,"usedTicket":0,"aPoint":0}
#     return render(request, 'calendar.html',context)
#   else:
#     # 세션에서 aId 가져오기
#     aId = request.session.get('session_id')
#     today = date.today() # 오늘 날짜 today에 저장
#     print(aId,today)

#     # Attendance 객체 가져오기 (사용자별로 출석 기록을 가져옴)
#     qs = Attendance.objects.filter(aId=aId)

#     # Member 객체 가져오기 (Member[0].point 정보 필요함)
#     member = Member.objects.filter(id=aId)


#     ## 매달 1일에 count 리셋
#     first_day_of_month = today.replace(day=1)

#     if today == first_day_of_month:
#       qs[0].count = 0 # 카운트 리셋
#       qs[0].aTicket = 0
#       qs[0].save()
#       print("카운트 리셋 count",qs[0].count)


#     # aDate과 today 비교
#     if qs:
#       if qs[0].aDate != today:
#         qs[0].aDate = today
#         qs[0].save()
#         qs.update(count=F('count')+1) # 출석 횟수 추가
#         qs.update(aTicket=F('aTicket')+1) # 응모권 개수 추가
#         qs.update(aPoint=F('aPoint')+10) # 포인트 10p 추가
#         # member[0].point=qs[0].aPoint
#         # member[0].save()
#         context = {"result":"success","count":qs[0].count,"aTicket":qs[0].aTicket,"aPoint":qs[0].aPoint}
#       else:
#         context = {"result":"already_checked"}
#     else:
#       Attendance.objects.create(aId=aId,aDate=today,count=1,aTicket=1,aPoint=10)
#       context = {"result":"success","count":1,"aTicket":1,"aPoint":10}
#     return JsonResponse(context)


    
# 출석체크 및 응모권 지급 까지만 되는 함수
def calendar(request):
  # 출석체크 페이지 오픈
  if request.method == "GET":
    aId = request.session.get('session_id')
    qs = Attendance.objects.filter(aId=aId)
    if qs:
      context = {"count":qs[0].count,"aTicket":qs[0].aTicket,"usedTicket":qs[0].usedTicket}
    else:
      context = {"count":0,"aTicket":0,"usedTicket":0}
    return render(request, 'calendar.html',context)
  else:
    # 세션에서 aId 가져오기
    aId = request.session.get('session_id')
    today = date.today() # 오늘 날짜 today에 저장
    print(aId,today)

    # Attendance 객체 가져오기 (사용자별로 출석 기록을 가져옴)
    qs = Attendance.objects.filter(aId=aId)

    ## 매달 1일에 count 리셋
    first_day_of_month = today.replace(day=1)

    if today == first_day_of_month:
      qs[0].count = 0 # 카운트 리셋
      qs[0].aTicket = 0
      qs[0].save()
      print("카운트 리셋 count",qs[0].count)


    # aDate과 today 비교
    if qs:
      if qs[0].aDate != today:
        qs[0].aDate = today
        qs[0].save()
        qs.update(count=F('count')+1) # 출석 횟수 추가
        qs.update(count=F('aTicket')+1) # 응모권 개수 추가
        context = {"result":"success","count":qs[0].count,"aTicket":qs[0].aTicket}
      else:
        context = {"result":"already_checked"}
    else:
      Attendance.objects.create(aId=aId,aDate=today,count=1,aTicket=1)
      context = {"result":"success","count":1,"aTicket":1}
    return JsonResponse(context)
     

########## 뭐야 잘되다가 갑자기 왜 오류남 꺄악
# 응모권 개수 차감, 쿠폰 지급
def apply(request):
  aId = request.session.get('session_id')
  qs = Attendance.objects.filter(aId=aId)
  ticketDeduction = int(request.POST.get('ticketDeduction',0)) # 클라이언트에서 전송한 차감할 응모권 수
  print(qs,ticketDeduction)
  if qs: 
    if qs[0].aTicket < ticketDeduction:
      return JsonResponse({"result":"not_yet"}) # 응모권 부족

    else:
      ticket_count = qs[0].aTicket
      if ticket_count >= ticketDeduction:
        if ticketDeduction == 5:
          # 쿠폰 지급 
          coupon = Coupon.objects.create(
            attendance=qs[0],
            discount = 1000, # 쿠폰 금액
            used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
            used_to = timezone.now()+timezone.timedelta(days=30) # 쿠폰 유효기간 30일
          )
          print(coupon.discount) 
          
        elif ticketDeduction == 10:
          # 쿠폰 지급 
          coupon = Coupon.objects.create(
            attendance=qs[0],
            discount = 3000, # 쿠폰 금액
            used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
            used_to = timezone.now()+timezone.timedelta(days=30) # 쿠폰 유효기간 30일
          )
          print(coupon.discount) 
      # qs[0].coupon_code = coupon.discount
      qs.update(aTicket=F('aTicket')-ticketDeduction)
      qs.update(usedTicket=F('usedTicket')+ticketDeduction)
      print("aTicket : ",qs[0].aTicket,"usedTicket : ",qs[0].usedTicket)
      context = {"result":"success","aTicket":qs[0].aTicket,"usedTicket":qs[0].usedTicket}
      return JsonResponse(context)


# 럭키드로우(행운뽑기)
def luckyDraw(request):
  aId = request.session.get('session_id')
  qs = Attendance.objects.filter(aId=aId)
  ticketDeduction = int(request.POST.get('ticketDeduction',0)) # 클라이언트에서 전송한 차감할 응모권 수
  print(qs,ticketDeduction)
  if qs: 
    if qs[0].aTicket < ticketDeduction:
      return JsonResponse({"result":"not_yet"}) # 응모권 부족

    else:
      ticket_count = qs[0].aTicket
      if ticket_count >= ticketDeduction:
        
        # 쿠폰 지급 
        coupon = Coupon.objects.create(
          attendance=qs[0],
          discount = 5000, # 쿠폰 금액
          used_from = timezone.now(), # 쿠폰 사용 시작 가능 시간
          used_to = timezone.now()+timezone.timedelta(days=5) # 쿠폰 유효기간 30일
        )
        print(coupon.discount) 
      # qs[0].coupon_code = coupon.discount
      qs.update(aTicket=F('aTicket')-ticketDeduction)
      qs.update(usedTicket=F('usedTicket')+ticketDeduction)
      print("aTicket : ",qs[0].aTicket,"usedTicket : ",qs[0].usedTicket)
      context = {"result":"success","aTicket":qs[0].aTicket,"usedTicket":qs[0].usedTicket}
      return JsonResponse(context)


# 쿠폰 리스트페이지
def coupon(request):
  return render(request, 'coupon.html')


# member[0].point 를 띄우고 싶은데 안돼서 임시로 qs[0].pointㅠㅠ
# 앙포인트 페이지
def point(request):
  if request.method == "GET":
    aId = request.session.get('session_id')
    qs = Attendance.objects.filter(id=aId)
    if qs:
      context = {"result":"success","point":qs[0].aPoint}
    else:
      context = {"result":"notLogin","point":0}
    return render(request, 'point.html',context)

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