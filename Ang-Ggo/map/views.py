from django.shortcuts import render
from member.models import Member, Rating
from foodBoard.models import fBoard
from django.http import JsonResponse


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

def weather(request):
    return render(request, 'weather.html')


def Rating2(request):
    id = request.session.get("session_id")
    member = Member.objects.filter(id=id).first()
    pKey = request.POST.get("pKey")
    fboard = fBoard.objects.filter(pKey=pKey).first()
    rating = request.POST.get("rating")
    status = request.POST.get("status")
    print("id : ", id)
    print("rating : ", rating)
    print("status : ", status)
    print("fboard : ", fboard)
    print("fboard.bNo", fboard.bNo)
    if status == "1":
        print("반응 추가")
        qs = Rating.objects.filter(member=member, fboard=fboard, rating=rating)
        if not qs:
            Rating.objects.create(member=member, fboard=fboard, rating=rating)
            context = {"result": "1", "status": "1"}
            return JsonResponse(context)
        else:
            print("반응 추가 에러 발생")
    elif status == "0":
        print("반응 삭제")
        qs = Rating.objects.filter(member=member, fboard=fboard, rating=rating).first()
        if qs:
            qs.delete()
            context = {"result": "1", "status": "0"}
            return JsonResponse(context)
        else:
            print("반응 삭제 에러 발생")
