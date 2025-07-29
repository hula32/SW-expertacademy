# 아래 함수를 수정하시오.

def add_item_to_dict2(my_dict, key, value):
    # new_dict = my_dict.copy() # my_dict를 복사해서 새로운 dict 객체 생성
    # new_dict.setdefault(key, value)
    new_dict = {} # 빈 dict 생성
    for k in my_dict:
        new_dict[k] = my_dict[k] # my_dict 값을 new_dict에 복사 
    new_dict[key] = value
    return new_dict # new_dict 객체 반환


def add_item_to_dict(my_dict, key, value):
    new_dict = my_dict.copy() # my_dict를 복사해서 새로운 dict 객체 생성
    # new_dict.setdefault(key, value)
    new_dict[key] = value
    return new_dict # new_dict 객체 반환


my_dict = {'name': 'Alice', 'age': 25} # dict 객체를 생성
result = add_item_to_dict2(my_dict, 'country', 'USA') # 함수 호출하면서 매개변수로 dict 객체, 문자열
# result = new_dict
print(result)