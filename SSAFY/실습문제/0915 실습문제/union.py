def make_set(n):
    parents = [i for i in range(n + 1)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    # parents[rep_y] = rep_x

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

N = 6
parents = make_set(N)

union(2, 4)
union(4, 6)

if find_set(2) == find_set(4):
    print("2와 4는 같은 집합")