# problem08.py
# ---
# 문자열 `text`와 정수 `shift` 값을 받아, 카이사르 암호화를 수행하여 암호화된 문자열을 반환하는 `caesar_cipher` 함수를 완성하시오.
# 대소문자를 구분하며, 알파벳이 아닌 문자는 그대로 유지하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def caesar_cipher(text, shift):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = []
    for word in text:
        if 'a' <= word <= 'z':
            new_word = (ord(word) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(new_word))
        elif 'A' <= word <= 'Z':
            new_word = (ord(word) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_word))
        else:
            result.append(word)
    return ''.join(result)


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(caesar_cipher("hello", 3)) # khoor
print(caesar_cipher("Python123!", 5)) # Udymts123!
print(caesar_cipher("ABC", 1)) # BCD
