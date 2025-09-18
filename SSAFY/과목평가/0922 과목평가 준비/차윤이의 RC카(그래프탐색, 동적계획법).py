dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for t in range(1, T+1):
    N = int(input()) # 필드의 크기
    arr = [list(input().strip()) for _ in range(N)]

    start_r, start_c = end_r, end_c = -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_r, start_c = r, c
            elif arr[r][c] == 'Y':
                end_r, end_c = r, c
    
    
    Q = int(input()) # 조종 횟수
    result = []

    for q in range(Q):
        C, command = input().split()
        cmd_len = int(C)

        r, c = start_r, start_c
        d = 0

        for com in command: # RRAALAA
            if com == 'A':
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != "T":
                    r, c = nr, nc
            elif com == 'L':
                d = (d + 3) % 4
            elif com == 'R':
                d = (d + 1) % 4


        if (r, c) == (end_r, end_c):
            result.append('1')
        else:
            result.append('0')
    
    print(f"#{t} {' '.join(result)}")

