# problem05.py
# ---
# 정수 또는 실수로 이루어진 `numbers` 리스트를 받아, 리스트 요소들의 평균값을 반환하는 `average_value` 함수를 완성하시오.
# 리스트가 비어있으면 `0.0`을 반환하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def average_value(numbers):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not numbers:
        return 0.0
    total = 0.0
    count = 0
    for num in numbers:
        total = total + num
        count = count + 1
            
    return total / count
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(average_value([10, 20, 30])) # 20.0
print(average_value([1, 2, 3, 4, 5])) # 3.0
print(average_value([])) # 0.0
