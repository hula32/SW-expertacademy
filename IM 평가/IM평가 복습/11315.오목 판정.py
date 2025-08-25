T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = "NO"

    # 행
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 'o':
                cnt += 1
            elif arr[r][c] == '.':
                cnt = 0
            if cnt >= 5:
                result = "YES"



    # 열              
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 'o':
                cnt += 1
            elif arr[r][c] == '.':
                cnt = 0
            
            if cnt >= 5:
                result = "YES" 


    # 우상향
    points = [(r, 0) for r in range(N-1)] + [(N-1, c) for c in range(N)]
    dr = -1
    dc = 1

    for r, c in points:
        cnt = 0
        for i in range(N):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'o':
                    cnt += 1
                elif arr[nr][nc] == '.':
                    cnt = 0
                        
                if cnt >= 5:
                    result = "YES"



    # 우하향
    points = [(r, 0) for r in range(N-1)] + [(0, c) for c in range(N)]

    di = 1
    dj = 1

    for r, c in points:
        cnt = 0
        for i in range(N):
            nr, nc = r + di * i , c + dj * i
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'o':
                    cnt += 1
                elif arr[nr][nc] == '.':
                    cnt = 0
                        
                if cnt >= 5:
                    result = "YES"
            
    print(f"#{t} {result}")
