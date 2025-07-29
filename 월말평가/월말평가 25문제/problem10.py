# problem10.py
# ---
# 정수 리스트 `counts`와 문자열 `char_to_repeat`를 받아,
# `counts` 리스트의 각 숫자만큼 `char_to_repeat`를 반복하여 생성된 모든 문자열을 이어 붙여 최종 문자열을 반환하는 `repeat_and_join` 함수를 완성하시오.
# `counts` 리스트에 0 또는 음수, 혹은 정수가 아닌 값이 있을 경우 해당 값은 무시하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def repeat_and_join(counts, char_to_repeat):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not counts:
        return char_to_repeat
    
    char = []

    
    for count in counts:
        if isinstance(count, int) and count > 0:
            repeat_str = char_to_repeat * count
            char.append(repeat_str)
    
    return "".join(char)




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(repeat_and_join([2, 5, 1, 3], "*")) # **********
print(repeat_and_join([1, 0, 2], "A")) # AAA
print(repeat_and_join([], "#")) #
print(repeat_and_join([3, -1, 2, 'a'], "@")) # @@@@@
