
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

# # 특정 데이터 출력
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
#     # 무작위 유저 정보 요청 경로
    API_URL = (f'https://jsonplaceholder.typicode.com/users/{i}')

#     ## API 요청
    response = requests.get(API_URL)

#     # JSON -> dict 데이터 변환
    parsed_data = response.json()

#     # 이름만 출력
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



## 도서관 사용자 관리 서비스 - 데이터 처리

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

print(dummy_data)


    

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
                print(censored_user_list.get(data['company']))
                censored_user_list.get(data['company']).append(data['name']) # 그 리스트에 데이터 추가
            else: # 해당 회사 이름의 리스트가 딕셔너리에 없다면.
                censored_user_list[data['company']] = [data['name']] # 그 회사 이름으로 리스트 만들어서 넣기
                # censored_user_list[data['company']] = []
                # censored_user_list[data['company']].append(data['name'])
    return censored_user_list


print(create_user(dummy_data))  

## 도서관 사용자 관리 서비스 - 데이터 유효성 검사

user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17@yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelson@yahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': [
            'https://www.boyer-stevens.org/',
            'http://www.johnson.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': [
            'http://montgomery-rogers.biz/',
            'http://www.williams-nixon.com/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': [
            'https://flowers-parker.info/',
            'http://oliver-rice.info/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = [
    'Jenkins-Garcia',
    'Stephens Group',
    'White, Andrade and Howard',
    'Warren-Stewart',
]

def create_user(user_data):
    user_list = []
    count = 0
    for data in user_data:
        result = is_validation(data)
        if result == 'blocked':
            count += 1
            continue

        elif result[0] == False:
            count += 1
            for wrong_data in result[1]:
                data[wrong_data] = None
        user_list.append(data)
    print(f'잘못된 데이터로 구성된 유저의 수는 {count} 입니다.')
    return user_list


def is_validation(data):
    if data['company'] in black_list:
        return 'blocked'

    check = True
    check_list = []
    if data['blood_group'] not in blood_types:
        check = False
        check_list.append('blood_group')
    if '@' not in data['mail']:
        check = False
        check_list.append('mail')
    if 2 > len(data['name']) or 30 < len(data['name']):
        check = False
        check_list.append('name')
    if len(data['website']) <= 0:
        check = False
        check_list.append('website')

    return check, check_list


print(create_user(user_data))