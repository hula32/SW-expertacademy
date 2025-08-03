# 문자열 입력받기
str_list = list(input())
# 결과값 저장
result_list = []
# 아스키 코드를 이용하여 문자를 숫자로 변경
for list in str_list:
    if 'a'<= list <= 'z':
        result = (ord(list) - ord('a')) % 26 + 1
        result_list.append(result)
    if 'A' <= list <= 'Z':
        result = (ord(list) - ord('A')) % 26 + 1
        result_list.append(result)
print(' '.join(map(str, result_list)))


# 선생님 풀이
s = input().lower

for ch in s:
    print((ord(ch) - ord('a')) + 1, end = ' ')
