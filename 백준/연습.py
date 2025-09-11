'''
number_of_people = 0

def increase_user() :
    global number_of_people
    number_of_people += 1

print("현재 가입된 유저 수 : ", number_of_people)

def create_user(name, age, address) :
    increase_user()
    user_info = {'name' : name,
                 'age' : age,
                 'address' : address}
    print(f'{name}님 환영합니다!')

create_user('홍길동', 30, '서울')
print('현재 가입된 유저 수 : ', number_of_people)


pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title = None) :
    global pro_num

    data = {}

    data['과목'] = subject
    data['일차'] = day
    data['제목'] = title

    pro_num += 1
    data['문제번호'] = pro_num

    return data 

result_1 = create_data('python', 3)
result_2 = create_data(subject= 'web', day = 1, title = 'web 연습하기')
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)
'''
