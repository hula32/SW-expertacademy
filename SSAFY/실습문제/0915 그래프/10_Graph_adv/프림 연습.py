from heapq import heappop, heappush

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_weight, next_node in graph[node]:
            if not MST[next_node]:
                heappush(pq, (next_weight, next_node))

    return min_weight

V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))

result = prim(0)

print(f'최소비용 = {result}')
