'''
# 도서 대여 서비스

# name : 대여하는 사람 이름
# num : 대여하는 책의 개수
def rental_book(name, num):
    decrease_book(num)
    print(f'{name}님이 {num}권의 책을 대여하였습니다.')

number_of_book = 100


# num : 감소시킬 책의 개수
def decrease_book():
    global number_of_book
    number_of_book -= 1
    print("남은 책의 개수 :", number_of_book)

rental_book("홍길동", 3)


# 신규 고객 증가 - 스코프
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

increase_user()
print('현재 가입 된 유저 수 : ', number_of_people)


# 신규 고객 등록과 환영 인사
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

print('현재 가입 된 유저 수 : ', number_of_people)


# 값들을 하나의 딕셔너리에 저장
def create_user(name, age, address):
    increase_user()

    user_info = {'name' : name,
                 'age' : age,
                 'address' : address}
    print(f'{name}님 환영합니다!')
    print(user_info)
    
    
    
create_user('홍길동', 30, '서울')
print('현재 가입 된 유저 수 : ', number_of_people)


# 함수 활용하기

pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title = None):
    global pro_num
    
    # 빈 딕셔너리 생성
    data = {}

    # create_data의 각 매개변수를 data의 적절한 key에 할당한다. 
    data['과목'] = subject
    data['일차'] = day
    data['제목'] = title

    # data의 '문제 번호' key에 할당 할 값은 global에 정의된 pro_num 변수의 값에 1을 더한 값이 되어야 한다.  
    pro_num += 1
    data['문제 번호'] = pro_num
    
    return data

# 문자열 'python'과 정수 3을 순서대로 담아 호출한다.
result_1 = create_data('python', 3)

# 각 인자들이 적절한 매개변수에 할당 될 수 있도록 키워드 인자를 작성한다. 
# 일차: 정수 1 
# 과목: 문자열 'web' 
# 제목: 'web 연습하기' 
result_2 = create_data(subject = 'web', day = 1, title = 'web 연습하기')

# create_data 호출시, global_data 변수를 언패킹하여 인자로 전달한다. 
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)


# 재귀함수 만들기

'''
'''
        함수(2) 실행
            number에 2 할당
            if 2 == 1 조건문 만족하지 않음
            else문 2 + 함수(2-1) 
                결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

                함수(2-1) 실행
                    number에 1 할당
                    if 1 == 1 조건문 만족하므로 1 반환
            
            else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
            2 + 1 반환
        결과 : 3  
    '''


'''
def recur_example(number):
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    '''
'''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
'''
    if exponent == 0:
        return print(1)
    else:
        return base * (base * (exponent - 1))
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    '''
'''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
'''
    if number < 10:
        return number
    else:
        return (number % 10) + sum_of_digits(number // 10)
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6



# 도서 대여 서비스

#대여자의 이름과 대여하는 책의 수
def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다')

number_of_book = 100

# 대여하는 책의 수
def decrease_book(count):
    global number_of_book
    number_of_book -= count
    print('남은 책의 수 :', number_of_book)
 
  
rental_book('홍길동', 3)



# 다양한 built-in function

# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
print(abs(negative))


# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(bool(empty_list))


# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))


# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
print(sorted(unsorted_list))


# 대규모 신규 고객 등록

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


# 값들을 하나의 딕셔너리에 저장
def create_user(name, age, address):
    increase_user()

    user_info = {'name' : name,
                 'age' : age,
                 'address' : address}  

    print(f'{name}님 환영합니다!')
    # print(user_info) 
    return user_info # 딕셔너리 변환

# 유저 정보 리스트
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 유저별 정보 묶기
user_data = zip(name, age, address)

# map으로 create_user 함수 적용
result = list(map(lambda user : create_user(*user), user_data))

print(result)

'''

# 대규모 도서 대여 서비스

number_of_people = 0 # 유저 수
number_of_book = 100 # 책의 수

# 유저 수 증가
def increase_user():
    global number_of_people # 글로벌 함수 유저 수
    number_of_people += 1 # 유저 수 1 증가


# 대여하는 책의 수 줄이기
def decrease_book(count):
    global number_of_book # 글로벌 책의 수
    number_of_book -= count # 책의 수 대여 책의 수만큼 감소
    print('남은 책의 수 :', number_of_book) # 남은 책의 수 값 호출

# 유저 정보 리스트
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


# 유저별 정보 묶기
user_data = zip(name, age, address)


# 유저 생성
def create_user(name, age, address): 
    increase_user()

    user_info = {'name' : name,
                 'age' : age,
                 'address' : address}  

    print(f'{name}님 환영합니다!')
    return user_info # 딕셔너리 변환

# map으로 create_user 함수 적용
many_user = list(map(lambda user : create_user(*user), user_data))


# 책 대여
def rental_book(info): # 이름과 책 대여수
    decrease_book(info['age']) # decrease_book에서 책 대여 갯수 가져오기
    print(f'{info["name"]}님이 {info["age"]}권의 책을 대여하였습니다') # 호출


# 사용자별 책 대여(나이 기준: 나이 // 10권 대여)
list(map(rental_book,map(lambda x: {'name': x['name'], 'age': x['age'] // 10}, many_user)))


