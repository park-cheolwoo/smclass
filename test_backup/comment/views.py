from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from django.db.models import Q
from django.db.models import F, Max
from comment.models import Comment
from member.models import Member
from board.models import Board


def cwrite(request):    ## 하단댓글 저장
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  print(bno)
  board = Board.objects.get(bno=bno)
  ccontent = request.POST.get("ccontent","")
  print("cwrite 확인: ", bno, ccontent)
  
  qs = Comment.objects.create(member=member,board=board,ccontent=ccontent)
  qs.cgroup = qs.cno
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("cwrite qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)

def reply(request):
    cno = request.POST.get("cno")  # 부모 댓글 ID
    bno = request.POST.get("bno")  # 게시글 ID
    ccontent = request.POST.get("ccontent")  # 댓글 내용

    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    board = Board.objects.get(bno=bno)

    if cno:  # 대댓글인 경우
        parent_comment = Comment.objects.get(cno=cno)
        cgroup = parent_comment.cgroup
        parent_step = parent_comment.cstep
        parent_indent = parent_comment.cindent

        # 같은 그룹 내에서 부모 댓글보다 step이 큰 댓글들의 step을 1 증가
        Comment.objects.filter(cgroup=cgroup, cstep__gt=parent_step).update(cstep=F('cstep') + 1)

        # 새 댓글의 step과 indent 계산
        new_step = parent_step + 1
        new_indent = parent_indent + 1

        # 대댓글 생성
        new_comment = Comment.objects.create(
            member=member,
            board=board,
            ccontent=ccontent,
            cgroup=cgroup,
            cstep=new_step,
            cindent=new_indent
        )
    else:  # 최상위 댓글인 경우
        max_group = Comment.objects.filter(board=board).aggregate(Max('cgroup'))['cgroup__max'] or 0
        new_comment = Comment.objects.create(
            member=member,
            board=board,
            ccontent=ccontent,
            cgroup=max_group + 1,
            cstep=0,
            cindent=0
        )

    return JsonResponse({'result': 'success', 'comment': {
        'cno': new_comment.cno,
        'ccontent': new_comment.ccontent,
        'cdate': new_comment.cdate.strftime('%Y-%m-%d %H:%M:%S')
    }})

def cdelete(request):    ## 하단댓글 삭제
  cno = request.POST.get("cno")
  print("확인 : ",cno)
  Comment.objects.get(cno=cno).delete()
  context = {"result":"success"}
  return JsonResponse(context)


def cupdate(request):    ## 하단댓글 수정저장
  id = request.session['session_id']
  cno = request.POST.get("cno")
  ccontent = request.POST.get('ccontent')
  print("확인 : ",cno,ccontent)
  # 수정
  qs = Comment.objects.get(cno=cno)
  qs.ccontent = ccontent
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)