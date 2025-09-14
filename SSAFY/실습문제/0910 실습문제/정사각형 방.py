# 조건 1 : 상하좌우에 있는 방으로 이동 가능(델타)
# 조건 2 : 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는가?
# 처음 출발해야하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지 출력
# 최대인 방이 여럿이면 그 중 가장 작은 것을 출력


T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)

    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    continue

                if arr[r][c] + 1 == arr[nr][nc] :
                    visited[arr[r][c]] = 1
                    break
        
    
    max_cnt = 0
    cnt = 0
    start = 0
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f'#{t} {start} {max_cnt+1}')