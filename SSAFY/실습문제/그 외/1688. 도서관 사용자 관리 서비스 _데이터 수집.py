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
    dummy_data.append(parsed_data['name'])
    i += 1

print(dummy_data)