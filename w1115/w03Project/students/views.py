from django.shortcuts import render
from students.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

def write(request):
    if not request.POST:
        print("GET방식")
        return render(request, "write.html")
    else:
         print("학생 정보 저장")
         name = request.POST['s_name']
         major = request.POST['s_major']
         grade = request.POST['s_grade']
         age = request.POST['s_age']
         gender = request.POST['s_gender']
         print(name,major,grade,age,gender)

         sq = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
         sq.save()
         return HttpResponseRedirect(reverse("index"))


def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)