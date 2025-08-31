'''
5
13101
10101
10101
10101
10021

'''

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(start_r, start_c, arr, visited):

    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True

    while stack:
        r, c = stack.pop()

        if arr[r][c]== 3:
            return 1
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 1:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

    return 0
                
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]


    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    result = dfs(start_r, start_c, arr, visited)

    print(f'#{t} {result}')




    