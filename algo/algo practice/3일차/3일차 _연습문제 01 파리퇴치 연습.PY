T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]

    max_val = []

    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = 0
            for d in range(M):
                for m in range(M):
                    # nr, nc = r + d, c + M
                    cnt += arr[r+d][c+m]
            if max_val < cnt:
                max_val = cnt
    print(f'#{t} {max_val}')