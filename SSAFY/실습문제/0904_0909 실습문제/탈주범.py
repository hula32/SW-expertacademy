# 조건 1: 탈주범이 있을 수 있는 위치의 개수 계산하기
# 조건 2: 터널끼리 연결이 되어있는 경우 이동 가능
# 조건 3: 시간당 1의 거리 이동

from collections import deque
# 상하좌우 터널 타입
types = {
    1 : [1, 1, 1, 1], 
    2 : [1, 1, 0, 0],
    3 : [0, 0, 1, 1],
    4 : [1, 0, 0, 1],
    5 : [0, 1, 0, 1], 
    6 : [0, 1, 1, 0],
    7 : [1, 0, 1, 0]
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def bfs(R, C):
    # 후보군
    q = deque([(R, C)])
    visited[R][C] = 1

    # 종료조건: 상하좌우 더이상 갈 곳이 없으면 종료
    while q:
        now_r, now_c = q.popleft()
        dirs = types[arr[now_r][now_c]]

        # 상하좌우 확인
        for d in range(4):
            # 만약 출구가 없으면 패스
            if dirs[d] == 0:
                continue

            new_r = now_r + dr[d]
            new_c = now_c + dc[d]

            if 0 > new_r or new_r >= N or 0 > new_c or new_c >= M:
                continue 

            if arr[new_r][new_c] == 0:
                continue

            if visited[new_r][new_c]:
                continue

            next_dirs = types[arr[new_r][new_c]]

            if d % 2 == 0 and next_dirs[d + 1] == 0:
                continue

            if d % 2 == 1 and next_dirs[d - 1] == 0:
                continue

            if visited[now_r][now_c] + 1 > L:
                continue

            visited[new_r][new_c] = visited[now_r][now_c] + 1
            q.append((new_r, new_c))



T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # R의 크기 # C의 크기 # 맨홀뚜껑위치 R # C # 탈출 소요된 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문기록
    visited = [[0] * M for _ in range(N)]

    # 위치 개수 계산
    bfs(R, C)
    cnt = 0
    for r in range(N):
        for c in range(M):
            if 0 < visited[r][c] <= L:
                cnt += 1

    print(f'#{t} {cnt}')