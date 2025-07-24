'''
## 도서관 사용자 관리 서비스 - 사전 준비

import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'

# API 요청
response = requests.get(API_URL)

# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data)

# 변환 데이터의 타입
print(type(parsed_data))

# 특정 데이터 출력
print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name'])


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



## 도서관 사용자 관리 서비스 - 데이터 수집

# 10명의 데이터 요청
i = 0

for i in range(1, 11) :
    # 무작위 유저 정보 요청 경로
    API_URL = (f'https://jsonplaceholder.typicode.com/users/{i}')

    ## API 요청
    response = requests.get(API_URL)

    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # 이름만 출력
    print(parsed_data['name'])



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

for matrix_len in matrix:
    temporary_len = 0
    for j in matrix_len <= 4:
        temporary_len +=1
    print(f"{matrix_len}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.")

# for matrix_len in matrix[:] :
#     matrix_len += 1
#     print(matrix_len)

# for number in matrix_len :
#     temporary_len = 0
#     for matrix in temporary_len <= 4:
#         temporary += 1
#         print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for x in range(matrix_len(x, y)):
    for y in range(len(matrix[x])):
        matrix[x][y]
    print('matrix의 {x}, {y}번째 요소의 값은 {matrix[x][y]}입니다.')



