
dr = [-1, 1, 0, 0] + [-1, 1, -1, 1]
dc = [0, 0, -1, 1] + [-1, -1, 1, 1]


def dfs(sr, se):

    for d in range(8):
        nr = sr + dr[d]
        nc = se + dc[d]
        if 0 <= nr < H and 0 <= nc < W:
            if not visited[nr][nc] and arr[nr][nc] == 1:
                visited[nr][nc] = True
                dfs(nr, nc)

while True:

    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(H)]

    visited = [[False] * W for _ in range(H)]
    cnt = 0

    for r in range(H):
        for c in range(W):
            if not visited[r][c] and arr[r][c] == 1:
                visited[r][c] = True
                dfs(r, c)
                cnt += 1

    print(cnt)


# ----------------------------------------------------------
    
    
