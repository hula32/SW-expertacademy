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

# # 블랙리스트
# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]
# # 
# def create_user(dummy_data):
#     censored_user_list = {}
#     for data in dummy_data:
#         if censorship(data):
#             if censored_user_list.get(data['company']):
#                 print(censored_user_list.get(data['company']))
#                 censored_user_list.get(data['company']).append(data['name'])
#             continue
#         else:
#             censored_user_list[data['company']] = data['name']


# # 블랙리스트 포함 확인
# def censorship(data):
#     for data in dummy_data:
#         if data['company'] in black_list:
#             print(f'{comepany_name}소속의 {name} 은/는 등록할 수 없습니다.')
#             return False
#         else:
#             print('이상 없습니다.')
#            return True

## 도서관 사용자 관리 서비스 - 블랙리스트 관리

i = 0

dummy_data = []

for i in range(1, 11) :
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' # 요청을 보낼 주소

    ## API 요청
    response = requests.get(API_URL) # 서버에 해당 주소로 데이터를 달라고 요청
    # 서버의 응답은 response 변수에 저장됨.

    # JSON -> dict 데이터 변환
    parsed_data = response.json() # 응답 중에서 데이터 본문 부분만 json 형식으로 가져옴
    # json(자바스크립트) : python의 dict와 같은 형식
    # print(parsed_data)
    """
응답 본문
parsed_data = {'address': {'city': 'Gwenborough',
                            'geo': {'lat': '-37.3159', 'lng': '81.1496'},
                            'street': 'Kulas Light',
                            'suite': 'Apt. 556',
                            'zipcode': '92998-3874'},
                            'company': {'bs': 'harness real-time e-markets',
                                        'catchPhrase': 'Multi-layered client-server neural-net',
                            'name': 'Romaguera-Crona'},
                'email': 'Sincere@april.biz',
                'id': 1,
                'name': 'Leanne Graham',
                'phone': '1-770-736-8031 x56442',
                'username': 'Bret',
                'website': 'hildegard.org'}

 parsed_data['geo']['lat']
    """
    # print(parsed_data['address']['geo']['lat'])
    # lat, lng 정보 호출 및 실수형을 변경
    lat = float(parsed_data['address']['geo']['lat'])
    # print(lat)
    lng = float(parsed_data['address']['geo']['lng'])
    # print(lng)

    """
    응답 결과

    -37.3159
    81.1496

    """

    # company name, name를 호출
    company_name = parsed_data['company']['name']
    # print(company_name)
    name = parsed_data['name']
    # print(name)
    """
    응답 결과

    'Romaguera-Crona'
    'Leanne Graham'

    """

    # dummy_data리스트에 dict로 구성해서 삽입하기
    # lat(위도)과 lng(경도)의 조건문
    if -80 < lat < 80 and -80 < lng < 80:
        dic = {
            'company' : company_name,
            'lat' : lat,
            'lng' : lng,
            'name' : name}
        
        dummy_data.append(dic)


# 블랙리스트
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(data):
    if data['company'] in black_list:
        print(f'{data["company"]} 소속의 {data["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True


def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:
        if censorship(data):
            if censored_user_list.get(data['company']): # 만약에 해당 회사이름의 리스트가 있다면
                censored_user_list.get(data['company']).append(data['name']) # 그 리스트에 데이터 추가
            else: # 해당 회사 이름의 리스트가 딕셔너리에 없다면.
                censored_user_list[data['company']] = [data['name']] # 그 회사 이름으로 리스트 만들어서 넣기
                # censored_user_list[data['company']] = []
                # censored_user_list[data['company']].append(data['name'])
    return censored_user_list


print(create_user(dummy_data))  