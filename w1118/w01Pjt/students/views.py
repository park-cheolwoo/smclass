from django.shortcuts import render,redirect
from students.models import Student

# Create your views here.
def write(request):
    # form 보내는 방식이 GET or POST인 점을 활용
    if request.method == "GET":
        print("GET 방식으로 들어옴")
        return render(request, "write.html")
    else:
        print('POST방식으로 들어옴')
        name = request.POST['name']
        major = request.POST['major']
        grade = request.POST['grade']
        age = request.POST['age']
        gender = request.POST['gender']
        print("입력데이터 : ",name,major,grade,age,gender)
        Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender)
        print('학생 1명 저장')
        return redirect("students:lists")

def list(request):
    qs = Student.objects.all()
    context = {"s_list":qs}
    return render(request,'list.html',context)

def view(request,name):
    print("이름 정보 : ",name)
    qs = Student.objects.filter(name=name) # 없으면 빈 세트{}, filter의 경우 list타입
    context = {'stu':qs[0]}
    return render(request,'view.html',context)
    # qs = Student.object.get(name=name) # 없으면 에러
    # qs = get_object_or_404(Student,name=name) # 없으면 구문 리턴

# 1. url - 매개변수로 데이터값을 전달받음
def modify(request,name):
    if request.method == "GET":
        print("modify 이름 정보 : ",name)
        qs = Student.objects.filter(name=name)
        context={"stu":qs[0]}
        return render(request,'update.html',context)
    else:
        print("POST 호출")
        qs = Student.objects.get(name=name)
        # print(name)
        name = request.POST["name"]
        major = request.POST["major"]
        grade = request.POST["grade"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        print("수정 정보 :", name, major,grade, age, gender)
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        return redirect("/")

# 2. 파라미터
def modify2(request):
    name = request.GET.get('name')
    print("modify2 이름 정보 : ",name)
    qs = Student.objects.filter(name=name)
    context = {"stu": qs[0]}
    return render(request, "update.html", context)

# 3. Appname - 매개변수로 데이터값을 전달받음
def modify3(request,name):
    print("modify3 이름 정보 : ",name)
    qs = Student.objects.filter(name=name)
    context = {"stu": qs[0]}
    return render(request, "update.html", context)



def delete(request,name):
    print("삭제 정보 : ",name)
    # qs = Student.objects.get(name=name).delete()
    return redirect('students:list')
