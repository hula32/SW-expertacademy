for t in range(1, 11):
    M = int(input())
    arr = [list(input().strip()) for _ in range(8)]

    cnt = 0

    # 행순회
    for r in range(8):
        for c in range(8-M+1):
            lft = c
            rgt = c + M - 1

            pal = M // 2

            is_pal = True
            for i in range(pal):
                if arr[r][lft+i] != arr[r][rgt-i]:
                    is_pal = False
            
            if is_pal:
                cnt += 1
    
    for c in range(8):
        for r in range(8-M+1):
            lft = r
            rgt = r + M - 1

            pal = M // 2

            is_pal = True
            for i in range(pal):
                if arr[lft+i][c] != arr[rgt-i][c]:
                    is_pal = False
            
            if is_pal:
                cnt += 1

    print(f'#{t} {cnt}')
    
            

