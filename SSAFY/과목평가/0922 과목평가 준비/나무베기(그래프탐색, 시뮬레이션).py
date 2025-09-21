# 조건 1 : 앞으로 이동, 왼쪽 90도 회전, 오른쪽 90도 회전
# 조건 2 : 최단 거리가 아닌, 최소 리모컨 조작 횟수로 이동 가능
# 조건 3 : 나무를 벨 수 있는 최대 나무의 수가 주어짐
# 그 때 목적지까지 이동하기 위한 최소 조작 횟수 구하기(항상 위를 바라보는 상태)

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

def bfs(N, K, arr, start, end):
    sr, sc = start
    er, ec = end

    visited = {}

    q = deque()

    q.append((sr, sc, 0, 0, 0))
    visited[(sr, sc, 0, 0)] = True
    

    while q:
        r, c, d, cut, ops = q.popleft()

        if (r, c) == (er, ec) :
            return ops
        
        nd = (d + 3) % 4
        if (r, c, nd, cut) not in visited:
            visited[(r, c, nd, cut)] = True
            q.append((r, c, nd, cut, ops + 1))

        nd = (d + 1) % 4
        if (r, c, nd, cut) not in visited:
            visited[(r, c, nd, cut)] = True
            q.append((r, c, nd, cut, ops + 1))

        
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            cell = arr[nr][nc]

            if cell in ('G', 'Y'):
                if (nr, nc, nd, cut) not in visited:
                    visited[(nr, nc, d, cut)] = True
                    q.append((nr, nc, d, cut, ops + 1))

            elif cell == 'T' and cut < K:
                if (nr, nc, nd, cut + 1) not in visited:
                    visited[(nr, nc, d, cut + 1)] = True
                    q.append((nr, nc, d, cut + 1, ops + 1))

    return -1


for t in range(1, T+1):
    N, K = map(int, input().split()) # 필드크기, 나무 벨 수 있는 횟수
    arr = [list(input().strip()) for _ in range(N)]

    start = end = None
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start = (r, c)
                arr[r][c] = 'G'
            if arr[r][c] == 'Y':
                end = (r, c)

    if start is None or end is None:
        print(f'#{t} -1')

    ans = bfs(N, K, arr, start, end)

    print(f'#{t} {ans}')