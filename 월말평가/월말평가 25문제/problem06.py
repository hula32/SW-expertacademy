# problem06.py
# ---
# 주어진 `numbers` 리스트(정수 또는 실수)의 모든 요소의 합계를 반환하는 `calculate_sum` 함수를 완성하시오.
# Python 내장 함수 `sum()` 사용 금지.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 sum 함수를 사용하지 않습니다.
def calculate_sum(numbers):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not numbers:
        return 0
    
    total = 0

    for num in numbers:
        total += num
    
    return total
        


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(calculate_sum([1, 2, 3, 4, 5])) # 15
print(calculate_sum([10.5, 20.5, 30])) # 61.0
print(calculate_sum([])) # 0

# if not numbers:
#         return 0
    
#     total = 0.0
#     for num in numbers:
#         total = total + num
    
#     return total