from django.shortcuts import render
from pros.models import adminUser
from django.http import JsonResponse
# from django.contrib.auth.hashers import check_password  # 암호화 된 비밀번호와 원래 비밀번호 비교
# from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from member.models import Member
from board.models import Board
from event.models import Attendance

## 로그인/메인화면 ##

# 관리자 로그인 페이지
def prologin(request):
        return render(request, 'login2.html')
# 관리자 로그인
def prologinChk(request):
    id = request.POST.get("id", "")
    pw = request.POST.get("pw", "")
    qs = adminUser.objects.filter(id=id, pw=pw).first()
    if qs:
        request.session["session_adminId"] = qs.id
        request.session["session_adminName"] = qs.name
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

    # 추후 암호화 예정
    # db에서 해당 아이디 검색
    # try:
    #     adminUser = adminUser.objects.get(id=id)
    #     # 입력된 비밀번호와 저장된 암호화된 비밀번호 비교
    #     if check_password(pw, adminUser.pw):
    #         # 로그인 성공, 세션에 사용자 정보 저장
    #         request.session["session_id"] = adminUser.id
    #         request.session["session_nickname"] = adminUser.nickname
    #         list_qs = list(adminUser.objects.filter(id=id).values())  # 사용자 정보 가져오기
    #         context = {"result": "success", "member": list_qs}  # member 정보를 JSON으로 반환
    #     else:
    #         context = {"result": "fail", "message": "비밀번호가 틀렸습니다."}
    # except adminUser.DoesNotExist:
    #     context = {"result": "fail", "message": "아이디가 존재하지 않습니다."}

# 관리자 대시보드
def prolayout(request):
    return render(request, 'pros_index.html')


## 관리자 ##


# 관리자 전체보기
def proadmin1(request):
    return render(request, 'pros_admin1.html')


# 관리자 전체 조회
def getAdminList(request):
    print("관리자 조회")
    qs = adminUser.objects.all()
    print(qs.first())
    data = [ # 좌측은 Table의 Column명과,  우측은 DB의 Column명과 일치해야함
        {
            "No": str(item.aNo),
            "ID": str(item.id),
            "PW": str(item.pw),
            "Name": str(item.name),
            "Authority": str(item.authority),
            "Mdate": str(datetime.strftime(item.mDate, "%Y-%m-%d %H:%M:%S")),
        }
        for item in qs
    ]
    response = {"recordsTotal": qs.count(), "recordsFiltered": qs.count(), "data": data}
    return JsonResponse(response)

# 관리자 추가
def addAdminList(request):
    print("관리자 추가")
    id = request.POST.get("ID", "")
    pw = request.POST.get("PW", "")
    name = request.POST.get("Name", "")
    authority = request.POST.get("Authority", "")
    print(id,pw,name,authority)
    if id == "" or pw == "" or name == "" or authority == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    qs = adminUser.objects.filter(id=id).first()
    if qs: # id 중복이 있으면 fail
        context = {"result": "fail"}
    else:
        qs = adminUser(id=id, pw=pw, name=name, authority=authority)
        qs.save()
        context = {"result": "success"}
    return JsonResponse(context)


# 관리자 수정
def updateAdminList(request):
    print("관리자 수정")
    aNo = request.POST.get("No", "")
    id = request.POST.get("ID", "")
    pw = request.POST.get("PW", "")
    name = request.POST.get("Name", "")
    authority = request.POST.get("Authority", "")
    print(aNo,id,pw,name,authority)
    if id == "" or pw == "" or name == "" or authority == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    qs = adminUser.objects.filter(aNo=aNo).first()
    if qs:
        qs.id = id
        qs.pw = pw
        qs.name = name
        qs.authority = authority
        qs.save()
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

# 관리자 삭제
def delAdminList(request):
    print("관리자 삭제")
    aNo = request.POST.get("No", "")
    print(aNo)
    qs = adminUser.objects.filter(aNo=aNo).first()
    if qs:
        qs.delete()
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

# def searchAdminList(request):
#     print("관리자 검색")
#     keyword = request.POST.get("keyword", "")
#     qs = adminUser.objects.filter(id__contains=keyword)
#     print(qs)
#     if qs:
#         data = [ # 좌측은 Table의 Column명과,  우측은 DB의 Column명과 일치해야함
#             {
#                 "No": str(item.aNo),
#                 "ID": str(item.id),
#                 "PW": str(item.pw),
#                 "Name": str(item.name),
#                 "Authority": str(item.authority),
#                 "Mdate": str(datetime.strftime(item.mDate, "%Y-%m-%d %H:%M:%S")),
#             }
#             for item in qs
#         ]
#         print(data)
#         response = {"recordsTotal": qs.count(), "recordsFiltered": qs.count(), "data": data, 'result': 'success'}
#     else:
#         response = {'result': 'fail'}
#     return JsonResponse(response)


## 회원 ##
def promember1(request):
    return render(request, 'pros_member1.html')

def getMemberList(request):
    print("회원 조회")
    qs = Member.objects.all()
    data = [ # 좌측은 Table의 Column명과,  우측은 DB의 Column명과 일치해야함
        {
            "아이디": str(item.id),
            "비밀번호": str(item.pw),
            "이름": str(item.name),
            "닉네임": str(item.nickname),
            "이메일": str(item.email),
            "전화번호": str(item.tel),
            "주소": str(item.addr),
            "포인트": str(item.point),
            "필수약관": str(datetime.strftime(item.agree1, "%Y-%m-%d %H:%M:%S")),
            "선택약관": str(datetime.strftime(item.agree2, "%Y-%m-%d %H:%M:%S")),
            "가입일": str(datetime.strftime(item.mDate, "%Y-%m-%d %H:%M:%S")),
        }
        for item in qs
    ]
    print(data)
    response = {"recordsTotal": qs.count(), "recordsFiltered": qs.count(), "data": data}
    return JsonResponse(response)

def updateMemberList(request):
    print("회원 수정")
    id = request.POST.get("ID", "")
    nickname = request.POST.get("NickName", "")
    email = request.POST.get("Email", "")
    tel = request.POST.get("Phone", "")
    addr = request.POST.get("Address", "")
    print("받은 데이터 : ",id,nickname,email,tel,addr)
    if id == "" or nickname == "" or email == "" or tel == "" or addr == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    qs = Member.objects.filter(id=id).first()
    if qs:
        qs.id = id
        qs.nickname = nickname
        qs.email = email
        qs.tel = tel
        qs.addr = addr
        qs.save()
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

def delMemberList(request):
    print("회원 삭제")
    id = request.POST.get("ID", "")
    print(id)
    qs = Member.objects.filter(id=id).first()
    if qs:
        qs.delete()
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)


## 게시판 ##
def proboard1(request):
    return render(request, 'pros_board1.html')

def getBoardList(request):
    print("게시판 조회")
    qs = Board.objects.all()
    data = [ # 좌측은 Table의 Column명과,  우측은 DB의 Column명과 일치해야함
        {
            "bNo": str(item.bno),
            "ID": str(item.member.id),
            "Title": str(item.btitle),
            "Content": str(item.bcontent),
            "GPS": str(item.bgps),
            "Category": str(item.bselect),
            "Hit": str(item.bhit),
            "Bdate": str(datetime.strftime(item.bdate, "%Y-%m-%d %H:%M:%S")),
        }
        for item in qs
    ]
    response = {"recordsTotal": qs.count(), "recordsFiltered": qs.count(), "data": data}
    return JsonResponse(response)

def updateBoardList(request):
    print("게시판 수정")
    bNo = request.POST.get("bNo", "")
    btitle = request.POST.get("Title", "")
    bcontent = request.POST.get("Content", "")
    bgps = request.POST.get("GPS", "")
    bselect = request.POST.get("Category", "")
    if btitle == "" or bcontent == "" or bgps == "" or bselect == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    else:
        qs = Board.objects.filter(bno=bNo).first()
        if qs:
            qs.btitle = btitle
            qs.bcontent = bcontent
            qs.bgps = bgps
            qs.bselect = bselect
            qs.save()
            context = {"result": "success"}
        else:
            context = {"result": "fail"}
    return JsonResponse(context)


## 이벤트 ##
def proevent1(request):
    return render(request, 'pros_event1.html')

def getEventList(request):
    print("이벤트 조회")
    qs = Attendance.objects.all()
    data = [ # 좌측은 Table의 Column명과,  우측은 DB의 Column명과 일치해야함
        {
            "aNo": str(item.aNo),
            "ID": str(item.member.id),
            "Count": str(item.count),
            "aTicket": str(item.aTicket),
            "UsedTicket": str(item.usedTicket),
            "Point":str(item.member.point),
        }
        for item in qs
    ]
    response = {"recordsTotal": qs.count(), "recordsFiltered": qs.count(), "data": data}
    return JsonResponse(response)

def updateEventList(request):
    print("이벤트 수정")
    aNo = request.POST.get("aNo", "")
    count = request.POST.get("Count", "")
    aTicket = request.POST.get("aTicket", "")
    usedTicket = request.POST.get("usedTicket", "")
    point = request.POST.get("Point", "")
    if count == "" or aTicket == "" or usedTicket == "" or point == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    else:
        qs = Attendance.objects.filter(aNo=aNo).first()
        if qs:
            member=Member.objects.filter(id=qs.member.id).first()
            member.point = int(point)
            print("member.point : ",member.point)
            qs.count = count
            qs.aTicket = aTicket
            qs.usedTicket = usedTicket
            qs.save()
            member.save()
            context = {"result": "success"}
        else:
            context = {"result": "fail"}
    return JsonResponse(context)

def delEventList(request):
    print("이벤트 삭제")
    aNo = request.POST.get("aNo", "")
    print(aNo)
    qs = Attendance.objects.filter(aNo=aNo).first()
    if qs:
        qs.delete()
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

def addEventList(request):
    print("이벤트 추가")
    id = request.POST.get("ID", "")
    count = request.POST.get("Count", "")
    aTicket = request.POST.get("aTicket", "")
    usedTicket = request.POST.get("usedTicket", "")
    if id == "" or count == "" or aTicket == "" or usedTicket == "":
        context = {"result": "vacant"}
        return JsonResponse(context)
    else:
        member = Member.objects.filter(id=id).first()
        qs = Attendance.objects.filter(member=id).first()
        print(member)
        print(qs)
        if member and not qs:
            qs = Attendance(member=member, count=count, aTicket=aTicket, usedTicket=usedTicket, aDate=datetime.now())
            qs.save()
            context = {"result": "success"}
        else:
            context = {"result": "fail"}    
    return JsonResponse(context)