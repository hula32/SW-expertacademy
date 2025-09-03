T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 행 순회

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1 # 3, 4, 1, 4, 4
            if arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
            else:
                if c == N-1:
                    if cnt == K:
                        result += 1

    # 열 순회

    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1 
            if arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
            else:
                if r == N-1:
                    if cnt == K:
                        result += 1


    print(f'#{t} {result}')

