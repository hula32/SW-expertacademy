# 출발점 : 0, 도착점: 99
# 정점(분기점) 100개

'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7

'''

def dfs(start, tree, visited):

    stack = [start]

    while stack:
        node = stack.pop()

        if node == 99:
            return 1
        
        if not visited[node]:
            visited[node] = True

            for nxt in tree[node]:
                stack.append(nxt)

    return 0


for t in range(1, 11):
    num, N = map(int, input().split())
    number = list(map(int, input().split()))

    tree = [[] for _ in range(100)]

    for i in range(0, N*2, 2):
        s, e = number[i], number[i+1]
        tree[s].append(e)

    visited = [False] * 100

    result = dfs(0, tree, visited)

    print(f'#{t} {result}')