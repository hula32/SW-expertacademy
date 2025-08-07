T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    # 상하좌우
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    # 대각선
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]

    
    for r in range(N):
        for c in range(N):

            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r+dr[d]*m, c+dc[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]

            if max_val < cnt:
                max_val = cnt

            
            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r+di[d]*m, c+dj[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]

            if max_val < cnt:
                max_val = cnt

    print(f'#{t} {max_val}')


            
    
