T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]

    for e in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)

    S, G = map(int, input().split())

    stack = []
    stack.append(S)

    connected = False

    visited = [0] * (V+1)

    while stack:
        v = stack.pop()

        if v == G:
            connected = True
            break

        for w in adj[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)

    if connected:
        print(f'#{t} 1')

    else:
        print(f'#{t} 0')

