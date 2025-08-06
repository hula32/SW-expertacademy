T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행의 개수
    rows = len(arr)

    # 열의 개수
    cols = len(arr[0])

    # 인덱스(r, c) 상하좌우(nr, nc)
    nr = [0, 1, 0, -1]
    nc = [1, 0, -1, 0]

    # 대각선(dr, dc)
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    max_val = 0

    for r in range(N):
        for c in range(N):
            # r, c를 중심으로
            s1 = arr[r][c] # 누적합
            s2 = arr[r][c]
            
            # 상하좌우
            for nr, nc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for p in range(1, M):
                    ni, nj = r+nr*p, c+nc*p
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]

            for dr, dc in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                for p in range(1, M):
                    di, dj = r+dr*p, c+dc*p
                    if 0 <= di < N and 0 <= dj < N:
                        s2 += arr[di][dj]

            if s1 > s2:
                if max_val < s1:
                    max_val = s1
            elif s1 < s2:
                if max_val < s2:
                    max_val = s2
            

    print(f'#{t} {max_val}')







