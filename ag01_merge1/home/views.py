from django.shortcuts import render, redirect

def index(request):
  if request.method == 'GET':
    return render(request, 'index.html')
  else:
    return redirect('map:mview')

def homesweet(request):
  return render(request, 'homesweet.html')