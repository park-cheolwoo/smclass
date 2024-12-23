from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "Adminlogin.html")
    else:
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        qs = Member.objects.filter(id=id, pw=pw).first()
        if qs:
            request.session["session_id"] = id
        return render(request, 'Adminindex.html')
