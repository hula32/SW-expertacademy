# 조건 1 : 앞으로 이동, 왼쪽 90도 회전, 오른쪽 90도 회전
# 조건 2 : 최단 거리가 아닌, 최소 리모컨 조작 횟수로 이동 가능
# 조건 3 : 나무를 벨 수 있는 최대 나무의 수가 주어짐
# 그 때 목적지까지 이동하기 위한 최소 조작 횟수 구하기(항상 위를 바라보는 상태)

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

def bfs(sr, sc, er, ec, k):
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        d = 0
        cnt = 0
        cut = k

        if (r, c) == (er, ec):
            return cnt
        
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 'T' and cut > 0:
                cut -= 1
                arr[nr][nc] = 'G'
                q.append((nr, nc))
            
                
        


for t in range(1, T+1):
    N, K = map(int, input().split()) # 필드크기, 나무 벨 수 있는 횟수
    arr = [list(input().strip()) for _ in range(N)]

    start_r, start_c = end_r, end_c = -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_r, start_c = r, c
            if arr[r][c] == 'Y':
                end_r, end_c = r, c

    sr, sc = start_r, start_c
    er, ec = end_r, end_c

    min_val = float('inf')
    ans = bfs(sr, sc, er, ec, K)