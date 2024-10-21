import datetime
member = []
# member.txt 파일 읽기
# member에 저장
mem_keys = ["id","pw","name","nicName","address","money"]
f = open('member.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if not line:break
    mem_values = line.strip().split(",")
    mem_values[5] = int(mem_values[5])
    member.append(dict(zip(mem_keys,mem_values)))
f.close()

product = [
    {"pNo":1, "pCode":"t001", "pName" : "삼성TV", "price":2000000, "color":"black"},
    {"pNo":2, "pCode":"g001", "pName" : "LG냉장고", "price":3000000, "color":"white"},
    {"pNo":3, "pCode":"h001", "pName" : "하만카돈스피커", "price":500000, "color":"gray"},
    {"pNo":4, "pCode":"w001", "pName" : "세탁기", "price":1000000, "color":"yellow"}
]
c_title = ["번호","아이디","이름","상품코드","상품명","가격","구매시간"]
c_keys = ["cNo","id","name","pCode","pName","price","date"]
cartNo = 0
cart = []
ff = open('cart.txt','r',encoding='utf-8')
while True:
    line2 = ff.readline()
    if not line2:break
    c=line2.strip().split(",")
    c[0] = int(c[0])
    c[5] = int(c[5])
    cart.append(dict(zip(c_keys,c)))
ff.close()

session_info = {}

######## 함수 선언 ############
def buy(choice, cartNo):
    print(f"{product[choice-1]["pName"]}를 구매하셨습니다.")
    print("구매내역에 등록합니다.")
    print()
    # 로그인 정보
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    c = {
            "cNo": cartNo + 1,
            "id": session_info["id"],
            "name": session_info["name"],
            "pCode": product[choice-1]["pCode"],
            "pName": product[choice-1]["pName"],
            "price": product[choice-1]["price"],
            "date": today
        }
    cart.append(c)
    cartNo += 1
    session_info['money'] -= product[choice-1]['price']
    return cartNo

def buy_out():
    print(" [ 구매내역 ] ")
    print(
        f"{c_title[0]}\t{c_title[1]}\t{c_title[2]}\t{c_title[3]:7s}\t{c_title[4]:10s}\t{c_title[5]:8s}\t{c_title[6]}"
    )
    print()
    print("-"*90)
    sum = 0
    for s in cart:
        print(
            f"{s["cNo"]}\t{s["id"]}\t{s["name"]}\t{s["pCode"]:8s}\t{s["pName"]:10s}\t{s["price"]:8d}\t{s["date"]}"
        )
        sum += s['price']
    print()
    print("-"*90)
    print(f"총 구매 금액 : {sum:,}")
    print(f"총 구매 개수 : {len(cart)}")

def buy_money():
    print(" [ 금액 충전 ] ")
    print(f"현재 금액 : {session_info['money']}")
    session_info['money'] += int(input("충전하실 금액을 입력하세요. >> "))
    print(f"충전된 금액 : {session_info['money']}")

def buy_save():
    f = open("member.txt", "w", encoding="utf-8")
    for i in member:
        f.write(
            f"{i["id"]},{i["pw"]},{i["name"]},{i["nicName"]},{i["address"]},{i["money"]}\n"
        )
    f.close()
    ff = open("cart.txt","w",encoding='utf-8')
    for s in cart:
        ff.write(
            f"{s["cNo"]},{s["id"]},{s["name"]},{s["pCode"]},{s["pName"]},{s["price"]},{s['date']}\n"
        )
    ff.close()
    print("내용 저장이 완료되었습니다.")


########## 프로그램 시작 ##############
while True:
    print(" [ 메인 화면 ] ")
    print("1. 회원 로그인")
    print("2. 회원가입")
    input_id = input("아이디를 입력하세요.")
    input_pw = input("패스워드를 입력하세요.")

    # db에서 가져옴.
    flag = 0
    for i in member:
        if i["id"] == input_id and i["pw"] == input_pw:
            print("SM-SHOP에 오신 것을 환영합니다.!")
            session_info = i
            flag = 1
            break # for반복문 break
    if flag == 0:
        print("아이디 또는 패스워드가 일치하지 않습니다.")
    else:
        break


while True:
    print("            [ SM-SHOP ] ")
    print(f"                       닉네임 : {session_info['nicName']}님")
    print(f"                       금액 : {session_info['money']:,} 원")
    print("1. 삼성TV - 2,000,000")
    print("2. LG냉장고 - 3,000,000")
    print("3. 하만카돈스피커 - 500,000")
    print("4. 세탁기 - 1,000,000")
    print("7. 내용 저장")
    print("8. 구매내역 ")
    print("9. 금액충전 ")
    choice = int(input("구매하려는 상품번호를 입력하세요. >> "))

    if choice == 1:
        cartNo = buy(choice, cartNo) # 상품 구매함수 호출
    elif choice == 2:
        cartNo = buy(choice, cartNo)
    elif choice == 3:
        cartNo = buy(choice, cartNo)
    elif choice == 4:
        cartNo = buy(choice, cartNo)
    elif choice == 7:               # 내용 저장 함수 호출
        buy_save()
    elif choice == 8:
        buy_out()
    elif choice == 9:
        buy_money()
