from django.urls import path
from . import views

app_name = "pros"
urlpatterns = [
    ### 로그인/메인화면
    path("login/", views.prologin, name="prologin"),  # 로그인
    path("loginChk/", views.prologinChk, name="prologinChk"),  # 로그인 체크
    path("layout/", views.prolayout, name="prolayout"),  # 대시보드



    # 관리자 페이지
    path("admin1/", views.proadmin1, name="proadmin1"),  # 관리자 전체 조회
    path(
        "getAdminList/", views.getAdminList, name="getAdminList"
    ),  # 관리자 전체 조회 Ajax
    path("addAdminList/", views.addAdminList, name="addAdminList/"),  # 관리자 추가 Ajax
    path(
        "updateAdminList/", views.updateAdminList, name="updateAdminList"
    ),  # 관리자 수정 Ajax
    path("delAdminList/", views.delAdminList, name="delAdminList"),  # 관리자 삭제 Ajax
    # path(
    #     "searchAdminList/", views.searchAdminList, name="searchAdminList"
    # ),  # 관리자 검색 Ajax
    


    # 회원 페이지
    path("member1/", views.promember1, name="promember1"),  # 회원 전체 조회
    path(
        "getMemberList/", views.getMemberList, name="getMemberList"
    ),  # 회원 전체 조회 Ajax
    path(
        "updateMemberList/", views.updateMemberList, name="updateMemberList"
    ),  # 회원 수정 Ajax
    path("delMemberList/", views.delMemberList, name="delMemberList"),  # 회원 삭제 Ajax



    # 게시판 페이지
    path("board1/", views.proboard1, name="proboard1"),  # 게시판 전체 조회
    path(
        "getBoardList/", views.getBoardList, name="getBoardList"
    ),  # 게시판 전체 조회 Ajax
    path(
        "updateBoardList/", views.updateBoardList, name="updateBoardList"
    ),  # 게시판 수정 Ajax



    # 이벤트 페이지
    path("event1/", views.proevent1, name="proevent1"),  # 이벤트 전체 조회
    path(
        "getEventList/", views.getEventList, name="getEventList"
    ),  # 이벤트 전체 조회 Ajax
    path(
        "updateEventList/", views.updateEventList, name="updateEventList"
    ),  # 이벤트 수정 Ajax
    path("delEventList/", views.delEventList, name="delEventList"),  # 이벤트 삭제 Ajax
    path("addEventList/", views.addEventList, name="addEventList"),  # 이벤트 추가 Ajax

]
