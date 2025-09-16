T = int(input())

def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

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

    parents[rep_y] = rep_x

for t in range(1, T+1):
    N, M = map(int, input().split())

    parents = make_set(N)

    number = []
    for m in range(M):
        a, b = map(int, input().split())
        number.append((a, b))

    for s, e in number:
        union(s, e)

    groups = set()
    for i in range(1, N+1):
        groups.add(find(i))

    print(f'#{t} {len(groups)}')