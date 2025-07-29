# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add('d')
print(my_set) # {'b', 1, 2, 3, 'c', 'd', 'a'}

my_set.add('d')
print(my_set) # {'b', 1, 2, 3, 'c', 'd', 'a'}

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {'b', 1, 3, 'c', 'a'}
my_set.remove(10)  # KeyError: 10

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # b -> 값이 바뀔 수 있음
print(my_set) # {1, 2, 3, 'c', 'a'}

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {'b', 1, 3, 'c', 'a'}
my_set.discard(10) # 아무런 일이 발생되지 않는다.

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
my_set.update([1, 4, 5]) -> 다른 이터러블 넣어보기
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))  # True
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}
