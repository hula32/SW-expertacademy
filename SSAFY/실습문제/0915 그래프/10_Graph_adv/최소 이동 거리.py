from heapq import heappop, heappush

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())

    INF = float("inf")
    dists = [INF] * (N+1)

    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))

    pq = [(0, 0)] # 가중치, node

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        if node == N:
            break

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    print(f'#{t} {dists[N]}')



    
