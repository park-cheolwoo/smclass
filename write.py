# pip install geopy

from geopy.geocoders import Nominatim

geo_local = Nominatim(user_agent='South Korea')
address = "경기도 성남시 수정구 모란로 46"
# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        print(x_y)
        return x_y
    except:
        return [0,0]
    
geocoding(address)