import datetime
import os

members = []
m_title = ["id", "pw", "name", "nicName", "address", "money"]
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H-%M-%S")


#### member.csv파일 불러오기-------------------------------
f = open("b1017/member.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    # c리스트 저장
    c = line.strip().split(",")
    c[5] = int(c[5])  # money
    # members리스트에 딕셔너리 저장
    members.append(dict(zip(m_title, c)))
f.close()
# ----------------------------------------------------------
# cart.txt파일 읽기, member딕셔너리 저장
cart = []

c_keys = ["cno", "id", "name", "pCode", "pName", "price", "date"]
# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지 확인
if os.path.exists("b1017/cart.txt"):
    f = open("b1017/cart.txt", "r", encoding="utf-8")
    while True:
        line = f.readline()
        if not line:
            break
        c = line.strip().split(",")
        c[0] = int(c[0])
        c[5] = int(c[5])
        cart.append(dict(zip(c_keys, c)))
    f.close()
cartNo = len(cart)
# -----------------------------------------------------------
# product 파일 저장해서 불러오기
product = [
    {"pno": 1, "pCode": "t001", "pName": "삼성TV", "price": 2000000, "color": "black"},
    {
        "pno": 2,
        "pCode": "g001",
        "pName": "LG냉장고",
        "price": 3000000,
        "color": "white",
    },
    {
        "pno": 3,
        "pCode": "h001",
        "pName": "하만카돈스피커",
        "price": 500000,
        "color": "gray",
    },
    {"pno": 4, "pCode": "w001", "pName": "세탁기", "price": 1000000, "color": "yellow"},
]
p_title = ["번호", "아이디", "이름", "코드", "상품명", "가격", "구매일자"]
ff = open("b1017/product.txt", "w", encoding="utf-8")
for s in product:
    t = list(s.values())
    ff.write(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]}\n")
print("저장이 완료되었습니다.")
ff.close()
session_info = {}


# ------------------------------------------------------------
# 물품 구매 함수-----------------------------------------------
def buy(cartNo,choice):
    cartNo += 1
    print(cartNo)
    session_info["money"] -= product[choice-1]["price"]
    c = f"{cartNo},{session_info["id"]},{session_info["name"]},{product[choice-1]["pCode"]},{product[choice-1]["pName"]},{product[choice-1]["price"]},{today}\n"
    cart.append(c)
    print(f"{product[choice-1]['pName']} 상품 구매가 완료되었습니다.")
    return cartNo
# --------------------------------------------------------------------

#####  프로그램 시작  #####
while True:
    print("[ 메인화면 ]")
    print("1. 로그인")
    print("2. 회원가입")
    print("0. 프로그램 종료")
    print("-" * 30)
    choice = input("원하는 번호를 입력하세요.>>")
    # 로그인 구현 ---------------------------------------
    if choice == "1":
        flag = 0
        input_id = input("아이디를 입력하세요. >> ")
        input_pw = input("아이디를 입력하세요. >> ")
        for s in members:
            if input_id == s["id"] and input_pw == s["pw"]:
                flag = 1
                session_info = s
                print("SM SHOP에 오신 것을 환영합니다.")
                break
        if flag == 0:
            print("아이디 또는 비밀번호가 일치하지 않습니다.")
        else:
            break
    # -------------------------------------------------------
    # 회원가입 구현 -----------------------------------------
    elif choice == "2":
        input_id = input("아이디를 입력하세요.>> ")
        input_pw = input("패스워드를 입력하세요.>> ")
        name = input("이름을 입력하세요.")
        nicName = input("닉네임을 입력하세요.")
        address = input("주소를 입력하세요.")
        money = int(input("충전 금액을 입력하세요."))
        m_list = [input_id, input_pw, name, nicName, address, money]
        members.append(dict(zip(m_title, m_list)))
        session_info = dict(zip(m_title, m_list))
        # 회원가입 후 다시 파일에 저장 -------------------------
        # ----------------------------------------------------
        print(f"{name} 님 가입을 환영합니다.")
        break
    # --------------------------------------------------------
    # 프로그램 종료 ------------------------------------------
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    # -------------------------------------------------------


# 메인화면 -----------------------------------------------------------
while True:
    print("           [ SM-SHOP ]")
    print(f"                       닉네임:{session_info['nicName']}님")
    print(f"                       금액 :{session_info['money']:,} 원")
    print("1. 삼성TV - 2,000,000")
    print("2. LG냉장고 - 3,000,000")
    print("3. 하만카돈스피커 - 500,000")
    print("4. 세탁기 - 1,000,000")
    print("7. 내용저장")
    print("8. 구매내역 ")
    print("9. 금액충전 ")
    print("0. 프로그램 종료")
    choice = int(input("구매하려는 상품번호를 입력하세요.>> "))

    if choice == 1:
        cartNo = buy(cartNo, choice)
    if choice == 2:
        cartNo = buy(cartNo, choice)
    if choice == 3:
        cartNo = buy(cartNo, choice)
    if choice == 4:
        cartNo = buy(cartNo, choice)
    if choice == 7:
        f = open('b1017/cart.txt','w',encoding='utf-8')
        for s in cart:
            f.write(s)
        print("저장이 완료되었습니다.")
        f.close()
  # 아래부터 구현 필요 ----------------------------------------------------
    if choice == 8:
        pass
    if choice == 9:
        pass
    if choice == 0:
        print("프로그램을 종료합니다.")
        break
