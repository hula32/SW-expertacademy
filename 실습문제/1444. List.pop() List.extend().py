# 아래 함수를 수정하시오.
def even_elements(data):
    new_data = []
    for num in data:
        if num % 2 == 0:
            new_data.extend([num])

    return new_data


"""
리스트.append(하나의원소) : 그냥 통째로 넣는다.
리스트.extend(반복가능한것 ex,리스트,튜플,집합,문자열) : 반복가능한 것의 원소 하나하나씩 쪼개서 넣는다.


"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)