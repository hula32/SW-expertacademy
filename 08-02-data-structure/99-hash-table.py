# 정수
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)
"""
1
2
3
100
4
39
9
10
52
87
set()
# 계속 똑같은 버킷 위치에 배치
"""
# 문자열
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
"""
1회차
b
h
c
g
f

2회차
g
c
f
e
i
"""

print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름
print(hash('a')) # 실행시마다 다름

print(hash(1))
print(hash(1.0))
print(hash('1'))
print(hash((1, 2, 3)))

'''
1
1
2972664383696949827
529344067295497451

-> 계속 바뀜

'a' -> 해시 함수 -> 1110115...(주소)

'''

# 딕셔너리의 키로 사용 불가라는 의미
# TypeError: unhashable type: 'list'
print(hash((1, 2, [3, 4])))
# TypeError: unhashable type: 'list'
print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
my_dict = {{3, 2}: 'a'}
