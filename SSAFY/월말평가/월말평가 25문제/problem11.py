import re # regex, RegExp, Regular Expression

# problem11.py
# ---
# 문자열 `text` 내에 있는 모든 숫자(연속된 숫자 문자열)를 찾아 정수로 변환한 후 합산하여 반환하는 `sum_digits_in_string` 함수를 완성하시오.
# (힌트: `re` 모듈 활용)
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.

def sum_digits_in_list(lst):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum = 0
    for item in lst:
        if item.isdigit():
            sum += int(item)
    
    return sum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
# print(sum_digits_in_string("abc123def45gh")) # 168
# print(sum_digits_in_string("가격:1000원, 수량:5개")) # 1005
# print(sum_digits_in_string("숫자 없음")) # 0

a = ['12', '23', 'a', 'b', '232', 'c']
print(sum_digits_in_list(a))