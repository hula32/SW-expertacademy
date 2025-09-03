for t in range(1, 11):
    M = int(input()) # 찾아야하는 회문 길이
    arr = [list(input().strip()) for _ in range(8)]

    N = 8
    cnt = 0

    # 행검사
    for r in range(N):
        for c in range(N-M+1):
            lft = c
            rgt = c + M - 1

            pal = M // 2

            is_pal = True

            for step in range(pal):
                if arr[r][lft+step] != arr[r][rgt-step]:
                    is_pal = False
            
            if is_pal:
                cnt += 1
    
    for c in range(N):
        for r in range(N-M+1):
            lft = r
            rgt = r + M - 1

            pal = M // 2

            is_pal = True
            for step in range(pal):
                if arr[lft+step][c] != arr[rgt-step][c]:
                    is_pal = False
            if is_pal:
                cnt += 1

    print(f'#{t} {cnt}')