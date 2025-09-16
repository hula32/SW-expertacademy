from collections import deque

T = int(input())

def bfs(start, target):
    if start == target:
        return 0
    
    MAX = 1000000

    visited = [False] * (MAX + 1)
    q = deque([(start, 0)])
    visited[start] = True

    while q:
        v, dist = q.popleft()

        for nxt in (v + 1, v - 1, v * 2, v - 10):
            if nxt == target:
                return dist + 1
            
            if 0 <= nxt <= MAX and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, dist + 1))
    
    return -1


for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{t} {ans}')
