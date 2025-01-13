from django.shortcuts import render
from member.models import Member

# 회원 리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request,'mlist.html',context)

# 로그인 페이지
def login(request):
    if request.method == "GET":
        # 쿠키 정보 검색 :request.COOKIES.get('이름')
        # 쿠키 저장 : request.set_cookie("key",'value')
        # 쿠키 삭제 : request.delete_cookie('key')
        print("쿠키 정보 : ", request.COOKIES.get('cookinfo'))
        saveId = request.COOKIES.get("saveId",'')
        context = {"saveId":saveId}
        response = render(request, "login.html",context)
        if not request.COOKIES.get('cookinfo'):
            response.set_cookie("cookinfo", "1111",max_age=60*60) #max_age=60초*60분
        # max_age가 없으면 브라우저 종료시 삭제
        return response
    else:
        print("쿠키 정보 : ", request.COOKIES)
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        pw = request.POST["pw"]  # 값이 없을 경우 에러
        saveId = request.POST.get("saveId", "값 없음")
        # 값이 없으면 뒤의 값으로 전달
        print("전달받은 정보 : ", id, pw, saveId)
        response = render(request, "login.html")
        ## 아이디 기억하기 정보가 있으면
        if saveId is not None:
            response.set_cookie("saveId", id, max_age=60*60)  # 아이디 기억하기 체크가 있으면 저장
        else:
            response.delete_cookie("saveID")  # 아 이디 기억하기 체크가 없으면 삭제
        return response

def login2(request):
    if request.method == "GET":
        cookId = request.COOKIES.get('cookId','')
        print('cookID : ',cookId)
        context = {'cookId':cookId}
        response = render(request,'login2.html',context)
        return response
    else:
        response = render(request,'index.html')
        # 3개 정보
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        saveId = request.POST.get('saveId')
        if saveId is not None:
            response.set_cookie('cookId',id,max_age=60*60)
        else : response.delete_cookie('cookId')
        return response

def product(request):
    if request.method == "GET":
        c_pId = request.COOKIES.get("c_pId","")
        c_pName = request.COOKIES.get("c_pName","")
        context = {"c_pId":c_pId,"c_pName":c_pName}
        return render(request,'product.html',context)
    else : 
        pId = request.POST.get('pId')
        pName = request.POST.get('pName')
        pOption = request.POST.get('pOption')
        saveP = request.POST.get('saveP')
        response = render(request,'index.html')
        if saveP is not None:
            response.set_cookie('c_pId',pId)
            response.set_cookie('c_pName',pName)
        else : 
            response.delete_cookie('c_pId')
            response.delete_cookie('c_pName')
        return response

def m2(request):
    if request.method == "GET":
        memberId = request.COOKIES.get('c_memberId',"")
        money = request.COOKIES.get('c_money',"")
        option = request.COOKIES.get('c_option',"")
        context = {"c_memberId":memberId, "c_money":money, "c_option":option}
        return render(request,'m2.html',context)
    else:
        memberId = request.POST.get("memberId") 
        money = request.POST.get("money") 
        option = request.POST.get("option") 
        saveMember = request.POST.get("saveMember")
        response = render(request,'index.html')
        if saveMember is not None:
            response.set_cookie("c_memberId",memberId)
            response.set_cookie("c_money",money)
            response.set_cookie("c_option",option)
        else:
            response.delete_cookie("c_memberId")
            response.delete_cookie("c_money")
            response.delete_cookie("c_option")
        return response
