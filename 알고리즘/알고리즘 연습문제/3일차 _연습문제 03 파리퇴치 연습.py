T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

 

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    max_val = -1

    for r in range(N):
        for c in range(N):

            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr[d]*m 
                    nc = c + dc[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]
            max_val = max(max_val, cnt)


            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr = r + di[d]*m
                    nc = c + dj[d]*m 
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += arr[nr][nc]
            max_val = max(max_val, cnt)


print(f'#{t} {max_val}')

    
