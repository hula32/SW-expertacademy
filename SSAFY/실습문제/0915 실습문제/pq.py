from collections import deque

def bfs(node):
    q = deque([node])

    while q:
        
        v = q.popleft()

        print(v, end = ' ')

        for next_node in graph[v]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            q.append(next_node)

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for i in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (v+1)
visited[1] = 1
bfs(1)