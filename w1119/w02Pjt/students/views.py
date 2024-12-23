from django.shortcuts import render,redirect
from students.models import Student

def write(request):
  if request.method == "GET":
    return render(request,'write.html')
  else : 
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    hobbys = request.POST.getlist("hobby")
    hobby = (",").join(hobbys)

    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
    return redirect("/")

def list(request):
  qs = Student.objects.all()
  context={"slist":qs}
  return render(request,'list.html',context)

def view(request,name):
  qs = Student.objects.filter(name=name)
  context = {"stu":qs[0]}
  return render(request,'view.html',context)

def update(request,name):
    if request.method == "GET":
        qs = Student.objects.filter(name=name)
        context = {"stu": qs[0]}
        return render(request, "update.html", context)
    else:
        name = request.POST['name']
        major = request.POST["major"]
        grade = request.POST["grade"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        hobbys = request.POST.getlist("hobby")
        hobby = (",").join(hobbys)
        qs = Student.objects.filter(name=name)
        qs[0].major = major
        qs[0].grade = grade
        qs[0].age = age
        qs[0].gender = gender
        qs[0].hobby = hobby
        qs[0].save()
        return redirect("/students/list")

def delete(request,name):
    Student.objects.filter(name=name).delete()
    return redirect("/students/list")
