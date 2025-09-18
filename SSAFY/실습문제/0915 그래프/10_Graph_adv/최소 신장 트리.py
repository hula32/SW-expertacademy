T = int(input())

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)
    
    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

for t in range(1, T+1):
    V, E = map(int, input().split())

    graph = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph.append((start, end, weight))

    graph.sort(key=lambda x : x[2])
    
    cnt = 0
    result = 0

    parents = [i for i in range(V+1)]

    for s, e, w in graph:
        if find(s) != find(e):
            union(s, e)
            cnt += 1
            result += w

            if cnt == V:
                break
    
    print(f'#{t} {result}')
