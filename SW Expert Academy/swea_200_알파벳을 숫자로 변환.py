# 문제와 동일한 값을 도출하지만, 문자열의 인덱스 숫자일 뿐 알파벳을 숫자로 바꾸는 작업을 하지 않아 Fail
s = input()
num = len(s)

for i in range(1, num + 1) :
    print(i, end = ' ')


# ord함수를 활용하여 문자를 숫자로 변경
s = input().lower()  # 모두 소문자로 변환 (대소문자 구분 없애기)

for ch in s :
    print((ord(ch) - ord('a')) + 1, end =' ') # 변환 예시)ord('a') - ord('a') + 1 = 97 - 97 + 1 = 1
