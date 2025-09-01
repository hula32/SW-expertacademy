T = int(input())

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def is_min(r, c):

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[r][c] > arr[nr][nc]:
                return True
                    
    return False

def find_min(r, c):

    min_val = arr[r][c]
    min_r = -1
    min_c = -1

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if min_val > arr[nr][nc]:
                min_r, min_c = nr, nc
                min_val = arr[nr][nc]

    return min_r, min_c

def simulation(r, c):

    cnt = 1

    while is_min(r, c):
        nr, nc = find_min(r, c)
        r, c = nr, nc
        cnt += 1

    return cnt

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N):
        for c in range(N):
            cnt = simulation(r, c)

            if cnt > max_val:
                max_val = cnt
            
    print(f'#{t} {max_val}')




