# # 조건 1 : 2번 출발점, 3번 도착점, 1번 벽, 0번 통로
# # 조건 2 : 2번 출발 -> 0번 통로를 찾아서 이동

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        if arr[r][c] == '3':
            return True

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if not visited[nr][nc] and arr[nr][nc] != '1':
                    visited[nr][nc] = True
                    q.append((nr, nc))

    return False

for t in range(1):
    input()
    arr = [list(input().strip()) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]

    start_r, start_c = -1, -1
    for r in range(16):
        for c in range(16):
            if arr[r][c] == '2':
                start_r, start_c = r, c

    r, c = start_r, start_c
    visited[r][c] = True

    if bfs(r, c):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

# ------------------------------------------------------------------


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc, arr, visited):
    stack = [(sr, sc)]

    while stack:
        r, c = stack.pop()

        if arr[r][c] == '3':
            return True

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if not visited[nr][nc] and arr[nr][nc] != '1':
                    visited[nr][nc] = True
                    stack.append((nr, nc))

    return False

for t in range(1, 11):
    input()
    arr = [list(input().strip()) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]

    start_r, start_c = -1, -1
    for r in range(16):
        for c in range(16):
            if arr[r][c] == '2':
                start_r, start_c = r, c

    r, c = start_r, start_c
    visited[r][c] = True

    if dfs(r, c, arr, visited):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')