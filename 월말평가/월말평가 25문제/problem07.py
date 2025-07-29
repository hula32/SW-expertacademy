# problem07.py
# ---
# 주어진 `scores` 리스트(정수)에서 가장 큰 값을 찾아 반환하는 `find_max_score` 함수를 완성하시오.
# Python 내장 함수 `max()` 사용 금지.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 max 함수를 사용하지 않습니다.
def find_max_score(scores):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not scores:
        return None
    
    max_val = scores[0]
    
    for num in scores[1:]:
        if num > max_val:
            max_val = num

    return max_val

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(find_max_score([30, 60, 90, 70])) # 90
print(find_max_score([5, 1, 9, 3, 7])) # 9
print(find_max_score([100, 100])) # 100
