member = []
m_keys = ["id", "pw", "name", "nicName", "address", "money"]
f = open("b1017/member.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line:break
    s = line.strip().split(",")
    for idx, i in enumerate(s):
        if idx == 5:
            s[5] = int(i)  # money
    #member 리스트에 딕셔너리 저장
    member.append(dict(zip(m_keys, s)))
f.close()

while True:
    print("1. 회원등록")
    print("2. 회원검색")
    choice = input("원하는 번호를 입력하세요. >>")

    if choice == "1":
        #회원등록
        id = input("ID를 입력하세요. >> ")
        flag = 0
        for i in member:
            if id == i['id']:
                print(f"{id}와 동일한 아이디가 있습니다. 다시 입력하세요.")
                flag = 1
                break
        if flag == 1:
            continue
        else:
            print(f"{id}은(는) 사용 가능합니다.")
        pw = input("PW를 입력하세요. >> ")
        name = input("이름을 입력하세요. >> ")
        nicName = input("닉네임을 입력하세요. >> ")
        address = input("주소를 입력하세요. >> ")
        money = int(input("충전 금액을 입력하세요. >> "))
        m_list = [id,pw,name,nicName,address,money]
        member.append(dict(zip(m_keys,m_list)))
        print(f"{id} 님 회원가입이 완료되었습니다.")
        print(m_list)
        print("-"*50)
        print(member)

    if choice == "2":
        #회원검색
        search = []
        mm = input("검색할 회원을 입력하세요.")
        flag = 0
        for a in member:
            if a["id"].find(mm) != -1:
                flag = 1
                print("검색 회원을 찾았습니다.")
                search.append(a)

        if flag == 0:
            print("검색 회원을 찾지 못했습니다.")
        else:
            print(f'총 검색 인원 : {len(search)}명')
            print(search)





# 회원 검색

