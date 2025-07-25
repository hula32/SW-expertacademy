
## 도서관 사용자 관리 서비스 - 사전 준비

import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'

# # API 요청
# response = requests.get(API_URL)

# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)

# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

'''
## 함수와 제어문 연습

food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

###for문###

# {이름}은/는 {종류}(이)다.
print(f'{food_list[0]["이름"]} 은/는 {food_list[0]["종류"]} (이)다')

# 만약 이름이 '토마토' 라면, 종류를 '과일' 로 변경하고 출력
for food_list in food_list:
    if food_list['이름'] == '토마토':
        food_list['종류'] = '과일'
        print(f'{food_list["이름"]} 은/는 {food_list["종류"]} (이)다')
    if food_list['이름'] == '자장면':
        print('자장면엔 고춧가루지')
        print(f'{food_list["이름"]} 은/는 {food_list["종류"]} (이)다')


# food_list의 dict 값 출력
print(food_list)

###while###

i = 0

while i < len(food_list):
    food = food_list[i]

    if food['이름'] == '잡채':
        print(f'{food["이름"]} 은/는 {food["종류"]} (이)다')

    if food['이름'] == '토마토':
        food['종류'] = '과일'
        print(f'{food["이름"]} 은/는 {food["종류"]} (이)다')

    if food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
        print(f'{food["이름"]} 은/는 {food["종류"]} (이)다')

    i += 1
        
# food_list의 dict 값 출력
print(food_list)

'''

## 도서관 사용자 관리 서비스 - 데이터 수집

# 10명의 데이터 요청
# i = 0

# for i in range(1, 11) :
#     # 무작위 유저 정보 요청 경로
#     API_URL = (f'https://jsonplaceholder.typicode.com/users/{i}')

#     ## API 요청
#     response = requests.get(API_URL)

#     # JSON -> dict 데이터 변환
#     parsed_data = response.json()

#     # 이름만 출력
#     print(parsed_data['name'])


'''
## 대여 불가 도서 구분하기
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


for book in list_of_book:
    if book in rental_list:
        print('모든 도서가 대여 가능한 상태입니다.')
    else:
        print(f'{book} 은/는 보유하고 있지 않습니다.')
        break

'''

'''

## 중첩 리스트 순회 연습

matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

matrix_len = 0

for _ in matrix:
    matrix_len += 1
print(matrix_len)

for matrix_len in matrix: 
    temporary_len = 0
    for number in matrix_len[:4]:
        temporary_len +=1
    print(f"{matrix_len}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.")


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'matrix의 {x}, {y}번째 요소의 값은 {matrix[x][y]}입니다.')

'''

## 도서관 사용자 관리 서비스 - 데이터 처리 - 몰라.. 질무,,,

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
    print(parsed_data)
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
    print(lat)
    lng = float(parsed_data['address']['geo']['lng'])
    print(lng)

    """
    응답 결과

    -37.3159
    81.1496

    """

    # company name, name를 호출
    company_name = parsed_data['company']['name']
    print(company_name)
    name = parsed_data['name']
    print(name)
    """
    응답 결과

    'Romaguera-Crona'
    'Leanne Graham'

    """

    # dummy_data리스트에 dict로 구성해서 삽입하기
    dummy_data = [{company_name, lat, lng, name}]



    break # 반복하지 말고 1개만 테스트해보기.

    # lat, lng 숫자로 변환
    # lat : float(parsed_data['address']['geo']['lat'])
    # lng : float(parsed_data['address']['geo']['lng'])

    # lat(위도)과 lng(경도)의 조건문
    # if -80 < lat < 80 and -80 < lng < 80:
    #     dummy = {"company" : parsed_data['company']['name'], 
    #               "name" : parsed_data['name'], 
    #               "lat" : lat, 
    #               "lng" : lng}
        
    #     dummy_data.append(dummy)
    


print(dummy_data)
    
'''
## 대여 불가 도서 관리하기

# 보유 중인 도서 리스트
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

# 대여 예정 도서 리스트
rental_list = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

# 보유하고 있지 않은 도서 리스트
# 리스트 컴프리헨션 [표현식 for 항목 in 반복가능한객체 if 조건]
missing_book = [book for book in rental_list if book not in list_of_book]

if len(missing_book) == 0:
    print('모든 도서가 대여 가능한 상태입니다.')
else :
    for book in missing_book:
        print(f'{book} 을/를 보충하여야 합니다.')
'''

    

    



