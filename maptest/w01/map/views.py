from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def map(request):
  return render(request,'map_merge2.html')

def locCheck(request):
    lat = request.GET.get("clickLat")
    loc = request.GET.get("clickLon")
    



    context = {"result": "success"}
    return JsonResponse(context)
