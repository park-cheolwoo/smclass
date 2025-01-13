from django.shortcuts import render

# Create your views here.
def write(request):
  if request.method == "GET":
    return render(request,'write.html')
  else:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']