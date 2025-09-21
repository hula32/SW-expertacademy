from heapq import heappush, heappop

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists




INF = float('inf')
V, E = map(int, input().split())

start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

result = dijkstra(start_node)
print(result)
