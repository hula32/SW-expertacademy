# integer : -21억 ~ 21억

T = 10

for t in range(1, T+1):
    input()
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_val = -float('inf') # 파이썬 정수 범위에서 가장 최소값

    for r in range(100):
        sum = 0
        for c in range(100):
            sum += arr[r][c]

        if max_val < sum:
            max_val = sum

    for c in range(100):
        sum = 0
        for r in range(100):
            sum += arr[r][c]

        if max_val < sum:
            max_val = sum

    sum = 0
    for i in range(100):
        sum += arr[i][i]

    if max_val < sum:
        max_val = sum

    sum = 0
    for r in range(100):
        sum += arr[r][99-r]

    if max_val < sum:
        max_val = sum

    print(f'#{t} {max_val}')




