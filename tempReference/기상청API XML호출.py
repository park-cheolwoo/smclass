import requests
import pprint
from bs4 import BeautifulSoup


url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
params = {
    "serviceKey": "Decode서비스키",
    "pageNo": "1",
    "numOfRows": "10",
    "dataType": "XML",
    "base_date": "20241210",
    "base_time": "1450",
    "nx": "55",
    "ny": "127",
}

response = requests.get(url, params=params)
datas = BeautifulSoup(response.content,'lxml-xml')
items = datas.find('items')
for item in items:
    category = item.select_one("category")
    obsrValue = item.select_one("obsrValue")
    print("category : ",category.text)
    print("obsrValue : ",obsrValue.text)
print("끝")
