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
    N = int(input())

    edges = []
    '''
    [(0, 1, 10000.0), (0, 2, 160000.0), 
    (0, 3, 170000.0), (1, 2, 170000.0), 
    (1, 3, 160000.0), (2, 3, 10000.0)]
    '''
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    for i in range(N):
        for j in range(i+1, N):
            cost = (((x_list[i] - x_list[j]) ** 2) + 
                    ((y_list[i] - y_list[j]) ** 2)) * tax
            
            edges.append((i, j, cost))

    edges.sort(key=lambda x : x[2])

    parents = [i for i in range(N)]

    cnt = 0
    result = 0
    for x, y, w in edges:
        if find(x) != find(y):
            union(x, y)
            cnt += 1
            result += w

            if cnt == N-1:
                break

    print(f'#{t} {result:.0f}')

    
