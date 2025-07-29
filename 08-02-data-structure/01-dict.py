# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alico
print(person.get('country')) # None
print(person.get('country', '해당 키는 존재하지 않습니다.')) # 해당 키는 존재하지 않습니다.
print(person['name']) # Alice
print(person['country'])  # KeyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
person_keys = person.keys()  # dict_keys(['name', 'age'])
person['country'] = 'Korea'
print(person_keys) # dict_keys(['name', 'age', 'country'])
for item in person.keys():
    print(item)
'''
name
age

# dict_keys(['name', 'age'])
: 실시간으로 동기화되는 확인 창(view)

'''

# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for value in person.values():
    print(value)
'''
Alice
25
'''
# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value)

"""
name Alice
age 25
"""

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
print(person.pop('country'))  # KeyError: 'country'

# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}

# setdefault
person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('country', 'Korea'))  # KOREA
print(person.setdefault('name', 'Korea')) # {'name': 'Alice', 'age': 25} -> 키가 없으면 'Korea'를 반환하기 때문에 적용 X
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}
# 'name': 'Alice' -> 'name': 'Jane' 동일한 키를 가졌을 경우 마지막 키의 값으로 덮어씀

person.update(age=100, address='SEOUL')
# age(키), 100(값) 등으로 구성된 형태
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}

person.update('age'=100, 'address'='SEOUL')
# 키를 문자열로 진행하면 오류 발생

문자열 = 정수
update는 근본적으로 함수

함수('문자열' = 정수) 라는 것은 없음
함수(매개변수(인자) = 값) 



# 똑같은 딕셔너리 유지
D1 = {'name': 'Alice', 'age': 25}
D1.clear()

# 재할당(다른 딕셔너리가 된 것)
D2 = {'name': 'Alice', 'age': 25}
D2 = {}

# 생김새는 동일하지만, 위와 아래는 다른 로직임
