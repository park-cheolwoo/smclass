from django.shortcuts import render
from foodBoard.models import fBoard

def foodList(request):
    return render(request,'foodList.html')


def foodView(request):
    return render(request, "foodView.html")


def foodFind(request):
    return render(request, "foodFind.html")
