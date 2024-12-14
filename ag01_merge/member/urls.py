from django.urls import path, include
from . import views

app_name = "member"
urlpatterns = [
    ### 로그인
    path('login/', views.login, name="login"),  # 로그인
    path('loginChk/', views.loginChk, name="loginChk"),  # 아이디 / 패스워드 일치 확인
    path('logout/', views.logout, name="logout"),  # 로그아웃

    ### 아이디/비밀번호 찾기
    path('findInfo/', views.findInfo, name="findInfo"),  # 아이디/비밀번호 찾기 페이지
    ## 아이디 찾기
    path('findId/', views.findId, name="findId"),  # 아이디 찾기 페이지 - 이름 / 이메일주소 일치 확인
    ## 패스워드 찾기
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'), # 인증메일 발송
    path('verify_code/', views.verify_code, name='verify_code'), # 인증번호 확인
    path('findPassword/', views.findPassword, name='findPassword'), # 이름, 이메일주소, 인증번호 일치/존재 확인

    ### 회원가입
    path('signup/', views.signup, name="signup"),  # 회원가입
    path('newMember/', views.newMember, name="newMember"),  # 회원정보 저장
    path('idDupChk/', views.idDupChk, name="idDupChk"),  # 아이디 중복 확인
    path('nicknameDupChk/', views.nicknameDupChk, name="nicknameDupChk"),  # 닉네임 중복 확인
    path('telDupChk/', views.telDupChk, name="telDupChk"),  # 전화번호 중복 확인
    path('emailDupChk/', views.emailDupChk, name="emailDupChk"),  # 이메일 중복 확인
    path('agreeChk/', views.agreeChk, name="agreeChk"),  # 회원가입 step01 약관동의

]
