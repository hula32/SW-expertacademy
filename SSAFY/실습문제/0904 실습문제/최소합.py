# 오른쪽 or 아래 이동 가능
# 최소 합계

T = int(input())

dr = [0, 1]
dc = [1, 0]

def recur(r, c, total, visited, arr):
    global visited

    if r == c == N-1:
        return total
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            recur(nr, nc, total + arr[nr][nc])
            visited[nr][nc] = False

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    min_val = 99999

    r, c, total = recur(0, 0, 0, visited, arr)

    if min_val > total:
        min_val = total




        





