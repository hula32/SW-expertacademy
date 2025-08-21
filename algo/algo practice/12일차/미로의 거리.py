from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [([False] * N) for _ in range(N)]

    # 시작점과 종료점 좌표 
    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c
            if arr[r][c] == 3:
                end_r, end_c = r, c

    q = deque()

    # 시작점 큐 저장
    visited[start_r][start_c] = True
    q.append((start_r, start_c, 0))

    can_reach = False
    maze_level = 0


    # 큐이 비워질 때까지
    while q: # 큐에 값이 있으면
        r, c, level = q.popleft()


        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, level + 1))

                if arr[nr][nc] == 3:
                    can_reach = True
                    maze_level = level

    print(f'#{t} {maze_level}')
                        

                    