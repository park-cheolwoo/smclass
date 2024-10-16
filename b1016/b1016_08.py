import datetime
# 전역변수 설정
member = []
product = [
    {"pNo": 1, "pCode": "t001", "pName": "삼성TV", "price": 2000000, "color": "black"},
    {
        "pNo": 2,
        "pCode": "g001",
        "pName": "LG냉장고",
        "price": 3000000,
        "color": "white",
    },
    {
        "pNo": 3,
        "pCode": "h001",
        "pName": "하만카돈스피커",
        "price": 500000,
        "color": "gray",
    },
    {"pNo": 4, "pCode": "w001", "pName": "세탁기", "price": 1000000, "color": "yellow"},
]
cart = []
session_info = {}
flag = 0
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H-%M-%S")
cNo = len(cart)
# ----------------------------------------------------------------------------------------------

# 초기 member 읽기
def mem_read():
    f = open("member.txt", "r", encoding="utf-8")
    mem_keys = ["id", "pw", "name", "nicName", "address", "money"]
    while True:
        line = f.readline()
        if not line:
            break
        s = line.strip().split(",")
        s[5] = int(s[5])
        member.append(dict(zip(mem_keys, s)))
    f.close()
# --------------------------------------------------------------
# 초기 cart 읽기
def cart_read():
    ff = open("cart.txt", "r", encoding="utf-8")
    c_keys = ["cNo", "name", "pCode", "pName", "price", "date"]
    while True:
        line2 = ff.readline()
        if not line2:
            break
        t = line2.strip().split(",")
        t[0] = int(t[0])
        t[5] = int(t[5])
        cart.append(dict(zip(c_keys, t)))
    ff.close()
# ---------------------------------------------------------------

# 로그인 함수
def login():
  while True:
      print(" [ 로그인 화면 ] ")
      flag = 0
      user_id = input("아이디를 입력하세요.")
      user_pw = input("비밀번호를 입력하세요.")
      for s in member:
          if user_id == s["id"] and user_pw == s["pw"]:
              session_info = s
              print(session_info)
              flag = 1
              print(f"SM SHOP에 오신 것을 환영합니다 {s['nicName']} 님")
              break
      if flag == 0:
          print("아이디와 비밀번호가 일치하지 않습니다. 다시 시도해주세요.")
      else:
          break
  return session_info
# ---------------------------------------------------------
# 구매하기 함수
def buy_pro(cNo):
    print(f"{product[choice-1]['pName']} 을 구매하셨습니다.")
    cNo += 1
    cart.append(
        {
            "cNo": cNo,
            "name": {session_info["name"]},
            "pCode": {product[choice - 1]["pCode"]},
            "pName": {product[choice - 1]["pName"]},
            "price": {product[choice - 1]["price"]},
            "date": today,
        }
    )
    session_info["money"] -= product[choice - 1]["price"]
    return cNo
# -----------------------------------------------------------------
# 구매내역 저장 함수
def cart_write():
    ff = open("cart.txt", "w", encoding="utf-8")
    for s in cart:
        ff.write(f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]},{s[5]},{s[6]}")
    ff.close()
# ------------------------------------------------------------------

# 프로그램 시작


mem_read()
cart_read()
session_info = login()
while True:
    print(" [ SM SHOP ] ")
    print(f"                       닉네임 : {session_info['nicName']}님 ")
    print(f"                       금액   : {session_info['money']} 원 ")
    print("1. 삼성TV 구매 - 2,000,000")
    print("2. LG냉장고 구매 - 3,000,000")
    print("3. 하만카돈스피커 구매 - 500,000")
    print("4. 세탁기 구매 - 1,000,000")
    print("7. 구매내역 저장")
    print("8. 구매내역 확인")
    print("9. 금액 충전")
    print("0. 프로그램 종료")
    choice = int(input("원하시는 번호를 입력하세요. >> "))
    if choice == 0:
        print("프로그램을 종료합니다.")
        break
    elif choice == 1:
        buy_pro(cNo)
    elif choice == 2:
        buy_pro(cNo)
    elif choice == 3:
        buy_pro(cNo)
    elif choice == 4:
        buy_pro(cNo)
    elif choice == 7:
        cart_write()
    elif choice == 8:
        pass
    elif choice == 9:
        pass
# -----------------------------------------------------------------
