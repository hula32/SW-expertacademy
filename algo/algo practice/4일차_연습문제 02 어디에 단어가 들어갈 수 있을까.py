T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]


    tri = 0

    for r in range(N):
        for c in range(N-K+1):
            is_ok = True
            for i in range(K):
                if arr[r][c+i] == 1:
                    continue
                else:
                    is_ok = False
            print(r, c)        
            if is_ok:
                if (c + K < N and arr[r][c+K] == 1) or (c - 1 >= 0 and arr[r][c]):
                    continue
                tri += 1
            print(r,c)
            print(tri)
            print('====================================')
    print(tri)

    for c in range(N):
        for r in range(N-K+1):
            is_ok = True
            for i in range(K):
                if arr[r+i][c] != 1:
                    is_ok = False
                    break
            if is_ok:
                if (r + K < N and arr[r+K][c] == 1) or (r - 1 >= 0 and arr[r-1][c]):
                    continue
                tri += 1

    print(f'#{t} {tri}')

                

