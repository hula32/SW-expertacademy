from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 입력받기
for t in range(1, 11):
    input()
    arr = [list(map(int, input())) for _ in range(16)]

    
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    q = deque()
    q.append((1,1))

    can_reach = False


    while q: # 큐에 인자가 있으면
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif arr[nr][nc] == 3:
                    can_reach = True
                    print(f'#{t} 1')
                    
    if can_reach == False:
        print(f'#{t} 0')

                
                
        




        





