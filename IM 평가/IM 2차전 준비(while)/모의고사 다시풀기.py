N = 3
arr = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

result = [[0] * N for _ in range(N)]


# 기준점
for r in range(N):
    for c in range(N):
        start_r, start_c = r, c


        min_val = []
        for d in range(4):
            nr, nc = start_r + dr[d], start_c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[start_r][start_c] > arr[nr][nc]:
                    start_r, start_c = nr, nc
                else:


