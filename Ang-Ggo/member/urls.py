from django.urls import path, include
from . import views

app_name = "member"
urlpatterns = [
    ### 로그인 / 로그아웃
    path("login/", views.login, name="login"),  # 로그인 페이지
    path("loginChk/", views.loginChk, name="loginChk"),  # 아이디 / 패스워드 일치 확인
    path("logout/", views.logout, name="logout"),  # 로그아웃
    ### 아이디 / 비밀번호 찾기
    path("findInfo/", views.findInfo, name="findInfo"),  # 아이디 / 비밀번호 찾기 페이지
    ## 아이디 찾기 탭
    path("findId/", views.findId, name="findId"),  # 이름 / 이메일주소 일치 확인
    ## 비밀번호 찾기 탭
    path(
        "send_verification_code/",
        views.send_verification_code,
        name="send_verification_code",
    ),  # 인증메일 발송
    path("verify_code/", views.verify_code, name="verify_code"),  # 인증번호 확인
    path(
        "findPassword/", views.findPassword, name="findPassword"
    ),  # 이름, 이메일주소, 인증번호 일치/존재 확인
    # 새 비밀번호 페이지(비밀번호 재설정) - 비밀번호 찾기 탭에서 넘어감
    path("newPassword/", views.newPassword, name="newPassword"),  # 새 비밀번호 페이지
    path(
        "newPasswordCheck/", views.newPasswordCheck, name="newPasswordCheck"
    ),  # 새 비밀번호 사용 가능여부 확인. 기존 비밀번호와 새 비밀번호 비교
    ### 회원정보 수정 페이지(마이페이지)
    path("changeInfo/", views.changeInfo, name="changeInfo"),
    ## 비밀번호 확인 페이지 - 회원정보 수정에서 비밀번호 변경할 때 필요한 비밀번호 확인
    path("passwordCheck/", views.passwordCheck, name="passwordCheck"),
    path("forPasswordCheck/", views.forPasswordCheck, name="forPasswordCheck"),
    # 새 비밀번호 페이지(비밀번호 재설정) - 회원정보 수정에서 비밀번호 변경할 때
    path("changeInfoNewPw/", views.changeInfoNewPw, name="changeInfoNewPw"),
    path("changeInfoNewPwChk/", views.changeInfoNewPwChk, name="changeInfoNewPwChk"),
    ### 약관 동의
    path("join01/", views.join01, name="join01"),  # 약관동의 페이지
    path("joinAgree/", views.joinAgree, name="joinAgree"),  # 약관동의에 체크했는지 확인
    ### 회원가입
    path("signup/", views.signup, name="signup"),  # 회원가입 페이지
    path("newMember/", views.newMember, name="newMember"),  # 회원정보 저장
    path("idDupChk/", views.idDupChk, name="idDupChk"),  # 아이디 중복 확인
    path(
        "nicknameDupChk/", views.nicknameDupChk, name="nicknameDupChk"
    ),  # 닉네임 중복 확인
    path("telDupChk/", views.telDupChk, name="telDupChk"),  # 전화번호 중복 확인
    path("emailDupChk/", views.emailDupChk, name="emailDupChk"),  # 이메일 중복 확인
    ### 회원탈퇴
    path(
        "deleteAccount/", views.deleteAccount, name="deleteAccount"
    ),  # 회원탈퇴 페이지
    path("forDeleteAccount/", views.forDeleteAccount, name="forDeleteAccount"),


    ##
    # path("hash_pw/", views.hash_pw, name="hash_pw"),  # 비밀번호 암호화
    ##
]
