import requests
from pprint import pprint as print

i = 1
dummy_data = []

for i in range(1, 11):

    # 무작위 유저 정보 요청 경로
    API_URL = (f'https://jsonplaceholder.typicode.com/users/{i}')

    # API 요청
    response = requests.get(API_URL)

    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # 특정 데이터 출력
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    comepany_name = parsed_data['company']['name']


    if -80 < lat < 80 and -80 < lng < 80:
        dict = {
            'company' : comepany_name,
            'lat' : lat,
            'lng' : lng,
            'name' : name}
        dummy_data.append(dict)

print(dummy_data)