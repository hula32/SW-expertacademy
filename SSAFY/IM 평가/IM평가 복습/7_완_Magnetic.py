
for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for c in range(N):
        count = 0
        for r in range(N):
            if arr[r][c] == 1:
                count += 1
            elif count > 0 and arr[r][c] == 2:
                result += 1
                count = 0

    print(f'#{t} {result}')

