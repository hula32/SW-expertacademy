T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    di = [-1,-1,1,1]
    dj = [1,-1,-1,1]

    max_val = 0

    for r in range(N):
        for c in range(N):
            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + dr[d] * m, c + dc[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]
                
            max_val = max(max_val, cnt)

    for c in range(N):
        for r in range(N):
            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + di[d] * m, c + dj[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]
                
            max_val = max(max_val, cnt)

    print(f'#{t} {max_val}')

    


