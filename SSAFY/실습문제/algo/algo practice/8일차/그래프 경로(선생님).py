T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    # [[], [4, 3], [3, 5], [], [6], [], []]
    for r in range(E):
        parent, child = map(int,input().split())
        adj[parent].append(child)

    S, G = map(int, input().split())

    stack = []
    connected = False

    visited = [0] * (V+1)

    visited[S] = 1
    stack.append(S)

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
    


            




