from django.shortcuts import render
from foodBoard.models import fBoard

def foodList(request):
    qs = fBoard.objects.all()
    context = {"flist":qs}
    return render(request,'foodList.html',context)


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
