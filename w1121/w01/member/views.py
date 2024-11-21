from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.

def logout(request):
    request.session.clear() # 전체 섹션 삭제
    # del request.session['session_id'] # 해당 섹션 삭제
    return redirect('index')


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            msg = "로그인 되었습니다."
            print(msg)
            request.session['session_id'] = id
            request.session['session_nickname'] = qs[0].nickname
            return redirect("index")
        else:
            msg = "아이디 또는 패스워드가 일치하지 않습니다."
            print(msg)
            return render(request, "login.html", {"login_msg": msg})

def mlist(request):
    id = request.session['session_id']
    if id == "admin":
        qs = Member.objects.all()
    else : 
        qs = Member.objects.filter(id=id)
    return render(request,'mlist.html',{"members":qs})

def mview(request,id):
    print("아이디 : ",id)
    qs=Member.objects.filter(id=id)
    if qs:
        return render(request,'mview.html',{"mem":qs[0]})

def mupdate(request,id):
    qs = Member.objects.filter(id=id)
    if qs :
        return render(request,'mupdate.html',{"mem":qs[0]})

def mwrite(request):
    if request.method=="GET":
        return render(request,'mwrite.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        tel = request.POST.get('tel')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ",".join(hobbys)

        qs = Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
        qs.save()
        return redirect("member:mlist")

def mupdate(request,id):
    if request.method == "GET":
        qs = Member.objects.filter(id=id)
        return render(request,'mupdate.html',{"mem":qs[0]})
    else: 
        print("id : ",id)
        id = request.session['session_id'] # admin이 아니면 세션을 가지고 저장
        # 관리자 로그인이면, id를 가져와서 저장
        if request.session.session_id == "admin":
            id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        nickname = request.POST.get("nickname")
        tel = request.POST.get("tel")
        gender = request.POST.get("gender")
        hobbys = request.POST.getlist("hobby")
        hobby = ",".join(hobbys)

        qs = Member.objects.get(id=id)
        qs.id = id
        qs.pw = pw
        qs.name = name
        qs.nickname = nickname
        qs.tel = tel
        qs.gender = gender
        qs.hobby = hobby
        qs.save()
        return redirect("member:mlist") 
    
def mdelete(request,id):
    print("회원정보 : ",id)
    Member.objects.get(id=id).delete()
    # return render(request,'mlist.html')
    return redirect('member:mlist')
