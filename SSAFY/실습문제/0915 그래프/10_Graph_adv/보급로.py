from heapq import heappush, heappop

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    INF = float("inf")
    dists = [[INF] * N for _ in range(N)]

    pq = [(0, 0, 0)] # 가중치, r, c

    while pq:
        dist, r, c = heappop(pq)

        if dist > dists[r][c]:
            break
        
        if (r, c) == (N-1, N-1):
            break
    
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                new_dist = dist + arr[nr][nc]
                if new_dist < dists[nr][nc]:
                    dists[nr][nc] = new_dist
                    heappush(pq, (new_dist, nr, nc))

    print(f'#{t} {dists[N-1][N-1]}')
        
            








