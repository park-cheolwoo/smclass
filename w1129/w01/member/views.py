from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from member.models import Member
# Create your views here.
def login(request):
    return render(request, "login.html")

def loginChk(request):
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
        request.session['session_id'] = id
        request.session['session_nicName'] = qs[0].nicName
        context = {"result": "success"}
    else:
        context = {"result": "fail"}
    return JsonResponse(context)

def logout(request):
    request.session.clear()
    return redirect("/")
