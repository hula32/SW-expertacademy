T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for R in range(N-M+1):
        for C in range(N-M+1):
            cnt = 0
            for r in range(M):
                for c in range(M):
                    cnt += arr[R+r][C+c]

            if max_val < cnt:
                max_val = cnt
    
    print(f'#{t} {max_val}')





