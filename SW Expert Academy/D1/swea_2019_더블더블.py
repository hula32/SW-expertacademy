# 입력값 받기
N = int(input())
# 누적된 곱한 값들 초기 값
total = 1
# 이전 결과값 * 2
for i in range(1, N + 2):
    if i == 1:
        print(i, end = ' ')
    else:
        total = total * 2
        print(total, end = ' ')
        