N = 3
arr = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def find_min(r, c):
    min_val = arr[r][c]

    min_r, min_c = -1, -1

    for d in range(4):
        nr, nc = r + dr[d], c + dc[c]
        if 0 <= nr < N and 0 <= nc < N:
            if min_val > arr[nr][nc]:
                min_val = arr[nr][nc]
                min_r, min_c = nr, nc
    return min_r, min_c

def is_min(r, c):
    for r in range(N):
        for c in range(N):
            

def simulation(r, c): 
    cnt = 1

    while not is_min:
        nr, nc = find_min(r, c)
        r, c = nr, nc
        cnt += 1

    return cnt


# 공굴리기 제일 긴 최대값 도출하기
max_cnt = 0
for r in range(N):
    for c in range(N):
        cnt = simulation(r, c)

        if max_cnt < cnt:
            max_cnt = cnt
print(max_cnt)
        





