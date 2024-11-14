from django.shortcuts import render

# Create your views here.
def reg(request):
  return render(request,'reg.html')