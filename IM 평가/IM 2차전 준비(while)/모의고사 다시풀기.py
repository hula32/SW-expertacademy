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

        
        # 상하좌우 중 작은 숫자 구하기 -> 이동하기
        min_val = sorted([])
        cnt = 0
        while True:
            for d in range(4):
                nr, nc = start_r + dr[d], start_c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and arr[start_r][start_c] > arr[nr][nc]:
                    min_val.append((arr[nr][nc], nr, nc))
            
            if min_val:
                start_r, start_c = min_val[0][1], min_val[0][2]
                cnt += 1
            else:
                result[start_r][start_c] = cnt

                
print(result)
        





