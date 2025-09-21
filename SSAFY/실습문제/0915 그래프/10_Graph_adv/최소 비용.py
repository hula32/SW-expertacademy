# 조건 1 : 출발 위치 - (0, 0), 도착 위치 - (N-1, N-1)
# 조건 2 : 상하좌우로 이동 가능
# 인접 지역으로 이동 시 +1, 현재 위치보다 다음 위치의 값이 크면 그 차이 많큼 +a

from heapq import heappush, heappop

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
        
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    INF = float("inf")
    dists = [[INF] * N for _ in range(N)]

    pq = [(0, 0, 0)]

    while pq:
        dist, r, c = heappop(pq)

        if dist > dists[r][c]:
            continue

        if (r, c) == (N-1, N-1):
            break

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                extra = 1
                extra += max(0, arr[nr][nc] - arr[r][c])
                
                new_dist = dist + extra
                if new_dist < dists[nr][nc]:
                    dists[nr][nc] = new_dist
                    heappush(pq, (new_dist, nr, nc))

    print(f'#{t} {dists[N-1][N-1]}')
