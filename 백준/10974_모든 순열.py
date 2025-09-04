N = int(input())

path = []
visited = [False] * (N+1)

def recur(cnt):
    if cnt == N:
        print(*path)
        return
    
    for idx in range(1, N+1):
        if visited[idx]:
            continue

        visited[idx] = True
        path.append(idx)
        recur(cnt + 1)
        path.pop()
        visited[idx] = False

recur(0)