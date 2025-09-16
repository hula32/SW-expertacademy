T = int(input())

# makeset
def makeset(n):
    parents = [i for i in range(n+1)]
    return parents 
    '''
    [0, 1, 2, 3, 4, 5]
    '''

# find
def find(x):
    if x == parents[x]:
        return x
        
    parents[x] = find(parents[x])
    return parents[x]

# union
def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x == rep_y:
        return

    parents[rep_y] = rep_x


for t in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    parents = makeset(N)

    for i in range(M):
        a = number[2*i]
        b = number[2*i+1]
    
        union(a, b)
    
    groups = set()
    for i in range(1, N+1):
        groups.append(find(i))
    
    print(f'#{t} {len(groups)}')



