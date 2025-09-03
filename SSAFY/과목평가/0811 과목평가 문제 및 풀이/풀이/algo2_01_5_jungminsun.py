T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    result = 0

    for r in range(1, N-1): # 1
        for c in range(1, M-1): # 1, 2

            cnt = arr[r][c] # 값 1, 0
            num = [] # [0,0,0,0] [1,1,1,1]

            for d in range(4):

                for m in range(1, 2):
                    nr, nc = r + dr[d], c + dc[d]
                    num.append(arr[nr][nc])


            counts = 0

            for i in num:
                if cnt > i:
                    counts += 1

            if counts == 4:
                result += 1

    print(f'#{t} {result}')



