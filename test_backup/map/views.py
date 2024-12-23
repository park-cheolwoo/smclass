from django.shortcuts import render

def mview(request):
  return render(request, 'mview.html')

def success(request):
  if request.method == 'POST':
    search_word = request.POST.get('search_word', '')
    print(search_word)  # 디버깅용
    context = {'search_word': search_word, "remote": "1"}
  else:
    context = {"remote": "0"}
  return render(request, 'success.html', context)

def test4(request):
  return render(request, 'test4.html')

def test5(request):
  return render(request, 'test5.html')

def test6(request):
  return render(request, 'test6.html')

def test7(request):
  return render(request, 'test7.html')

def test8(request):
  return render(request, 'test8.html')

def test9(request):
  return render(request, 'test9.html')

def weather(request):
  return render(request, 'weather.html')