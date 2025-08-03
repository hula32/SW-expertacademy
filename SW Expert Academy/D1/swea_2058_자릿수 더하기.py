# 자연수 입력받기
n = input()
#입력 받은 자연수 한글자씩 분리하기
number = list(map(int, str(n)))
# 합계
total = 0

for nums in number:
    total += nums

print(total)