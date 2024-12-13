from django.shortcuts import render,redirect
from foodBoard.models import fBoard
from django.core.paginator import Paginator
from member.models import Member
# from FoodCafe.models import Food

def foodList(request):
    if request.method == "GET":
        id = request.session.get('session_id')
        member = (Member.objects.filter(id=id))[0]
        npage = int(request.GET.get("npage", 1))
        qs = fBoard.objects.all()
        
        paginator = Paginator(qs, 8)
        flist = paginator.get_page(npage)
        context = {"flist": flist, "npage": npage}
    else:
        npage = int(request.POST.get("npage", 1))
        foodKeyword = request.POST.get("foodKeyword")
        qs = fBoard.objects.filter(bTitle=foodKeyword)
        paginator = Paginator(qs, 8)
        flist = paginator.get_page(npage)
        context = {"flist":flist,"npage":npage}
    return render(request, "foodList.html", context)


def foodView(request,bNo):
    qs = fBoard.objects.filter(bNo=bNo)
    context = {"flist":qs[0]}
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
        bTitle = request.POST.get("bTitle")
        bSubtitle = request.POST.get("bSubtitle")
        bContent = request.POST.get("bContent")
        bFile1 = request.FILES.get("bFile1")
        bFile2 = request.FILES.get("bFile2")
        bFile3 = request.FILES.get("bFile3")
        qs = fBoard(member=member[0],bTitle=bTitle, bSubtitle=bSubtitle,bContent=bContent,bFile1=bFile1,bFile2=bFile2,bFile3=bFile3)
        qs.save()
        return redirect('/foodBoard/foodList/')
