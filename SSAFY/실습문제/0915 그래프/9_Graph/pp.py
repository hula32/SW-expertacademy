def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

    '''
    [0, 1, 2, 3, 4, 5, 6]
    '''

# 대표자 찾기
def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


# 결합하기
def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x == rep_y:
        return
    
    parents[rep_y] = rep_x


N = 6
parents = make_set(N)

union(2, 4)
print(union(2, 4))


