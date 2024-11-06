import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

data = soup.select_one("table.type_5")
stocks = data.select("tr")
# print("개수 : ",len(stocks))

# 상단 타이틀 출력
tits = stocks[0].select("th") # ResultSet >> 객체의 리스트, 리스트로 사용 가능
title=[]

for tit in tits:
    title.append(tit.text)
a = ",".join(title) + "\n"
with open("c1022/a.text", "w", encoding="utf8") as f:
    f.write(a)
#   print(tit.text,end="\t")
# print()
# print("-"*80)
# print(tit.text.strip())
# print(title)
# print(stocks[0].select("th"))


# 주식 30개 출력 - 5개 출력 / 출력과 동시에 리스트에 추가
# print(title)
# print("-" * 30)
st_lists = []
for i in range(2,49+1):
    st_list = []
    sts = stocks[i].select("td")
    if len(sts) <=1:continue # td가 1개 이하이면 제외
    for idx, st in enumerate(sts):
        s = ""
        if idx == 4:
            s = st.select_one("span").text
            s += st.select_one("span").next.next.next.text.strip()
            print(st.select_one("span").text, end="\t")
            print(st.select_one("span").next.next.next.text.strip(),end="\t")
        else:
            s = st.text.strip()
            print(st.text.strip(),end="\t")
        st_list.append(s)
    with open("c1022/stocks.txt", "a", encoding="utf8") as f:
        f.write(",".join(st_list) + "\n")
    st_lists.append(st_list)    

    print()
    print("-"*30)
# print(st_lists)

# stock.txt 저장
