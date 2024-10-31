import func

while True:
    # 시작화면 출력
    choice = func.screen()
    # 로그인 부분
    if choice == "1":
        func.memlogin()
    # 비밀번호 찾기 부분
    elif choice == "2":
       func.search_pw()
    # 회원가입 부분
    elif choice == "3":
        pass