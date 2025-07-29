# problem09.py
# ---
# 양의 정수 `decimal_num`을 받아, 해당 숫자의 이진수 표현을 문자열로 반환하는 `decimal_to_binary` 함수를 완성하시오.
# `0`은 `"0"`으로, 음수나 정수가 아닌 값은 `"오류"` 문자열로 반환하시오.
# Python 내장 함수 `bin()` 사용 금지.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 bin 함수를 사용하지 않습니다.
def decimal_to_binary(decimal_num):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not isinstance(decimal_num, int) or decimal_num < 0:
        return "오류"
    
    if decimal_num == 0:
        return "0"
    
    result = []

    while decimal_num != 0:
        new_num = decimal_num % 2
        result.append(str(new_num))
        decimal_num = decimal_num // 2
        
    return ''.join(result[::-1])


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(decimal_to_binary(10)) # 1010
print(decimal_to_binary(0)) # 0
print(decimal_to_binary(25)) # 11001
print(decimal_to_binary(-5)) # 오류
print(decimal_to_binary(3.14)) # 오류
