from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse


# 1. 학생페이지 열기 2. 학생정보저장
def write(request):
    if request.method == "POST":
        name = request.POST.get("name")  # 데이터가 없을 시 None
        major = request.POST.get("major")
        grade = request.POST["grade"]  # 데이터가 없으면 에러 처리
        age = request.POST["age"]
        gender = request.POST["gender"]
        # hobby = request.POST['hobby'] # 1개의 값만 가져옴
        hobbys = request.POST.getlist("hobby")  # checkbox >> 여러개의 값
        hobby = (",").join(hobbys)  # list > str 변경
        # hobbys = hobby.split(",") # str > list변경
        print(name, hobby)
        # qs.save()
        qs = Student(
            name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys
        )
        qs.save()
        # create
        Student.objects.create(
            name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys
        )
        return redirect("/students/list/")
    else:
        return render(request, "write.html")


def list(request):
    # 학생 전체 정보 가져오기
    qs = Student.objects.all().order_by("-grade","name")
    context = {"slist": qs}
    return render(request, "list.html", context)


# 학생 상세보기
def view(request, name):
    qs = Student.objects.get(name=name)
    context = {"stu": qs}
    return render(request, "view.html", context)


# 1. 학생수정페이지 2. 학생수정저장
def update(request):
    if request.method == "GET":
        qs = Student.objects.get(name=name)
        context = {"stu": qs}
        return render(request, "update.html", context)
    else:
        name = request.POST.get("name")
        major = request.POST.get("major")
        grade = request.POST.get("grade")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        # Student 검색
        qs = Student.objects.get(name=name)
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.hobby = hobby
        qs.save()
        return redirect("students:view",name)
        # return redirect(reverse("students:view",args=(name,)))

# 학생 정보 삭제
def delete(request, name):
    print("삭제 정보 이름 : ",name)
    Student.objects.get(name=name).delete()
    return redirect('/students/list')

def search(request):
    search = request.GET.get("search")
    print("검색 단어 : ",search)
    qs = Student.objects.filter(name__contains=search)
    context = {"slist":qs}
    return render(request,'list.html',context)