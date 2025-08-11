T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 방향전환
    dr = [0, 1, 0, -1] # 오, 아, 왼, 위
    dc = [1, 0, -1, 0]

    dir = 0
    r, c = 0, 0

    for num in range(1, N*N +1):
        arr[r][c] = num

        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr < 0 or nr >= N and nc < 0 or nc >= N != 0:
            dir = (dir + 1) % 4
            nr = r + dr[dir]
            nc = c + dc[dir]

        r, c = nr, nc

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], and = '')
        print()