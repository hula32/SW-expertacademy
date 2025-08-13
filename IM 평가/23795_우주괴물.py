T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    count = 0

    for r in range(N):
        for c in range(N):

            if arr[r][c] == 2:
                for d in range(4):
                    for m in range(N):
                        nr, nc = r + dr[d] * m, c + dc[d] * m  # 영역 설정 완.
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 0: # 0일 때
                                arr[nr][nc] += 3 # 1씩 더해줘
                            if arr[nr][nc] == 1:
                                break

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                count += 1

    print(f'#{t} {count}')
