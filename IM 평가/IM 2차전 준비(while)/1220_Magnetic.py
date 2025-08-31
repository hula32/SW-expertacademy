for t in range(1, 11):
    input()
    arr= [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for c in range(100):
        cnt = 0
        for r in range(100):
            if arr[r][c] == 1:
                cnt = 1
            elif cnt == 1 and arr[r][c] == 2:
                result += 1
                cnt = 0

    print(f'#{t} {result}')


