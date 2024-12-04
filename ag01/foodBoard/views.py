from django.shortcuts import render,redirect
from foodBoard.models import fBoard
from django.core.paginator import Paginator

def foodList(request):
  npage = int(request.GET.get('npage',1))
  qs = fBoard.objects.all()
  paginator = Paginator(qs,8)
  flist = paginator.get_page(npage)
  context = {"flist":flist,"npage":npage}
  return render(request,"foodList.html",context)


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
        bTitle = request.POST.get("bTitle")
        bSubtitle = request.POST.get("bSubtitle")
        bContent = request.POST.get("bContent")
        bFile1 = request.FILES.get("bFile1")
        bFile2 = request.FILES.get("bFile2")
        bFile3 = request.FILES.get("bFile3")
        qs = fBoard(bTitle=bTitle, bSubtitle=bSubtitle,bContent=bContent,bFile1=bFile1,bFile2=bFile2,bFile3=bFile3)
        qs.save()
        return redirect('/foodBoard/foodList/')
