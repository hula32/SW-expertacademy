T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]


    result = 1
    # 행검사
    for r in range(9):
        num_cnt = set()
        for c in range(9):
            num_cnt.add(arr[r][c])
        if len(num_cnt) < 9:
            result = 0
            break

    for c in range(9):
        num_cnt = set()
        for r in range(9):
            num_cnt.add(arr[r][c])
        if len(num_cnt) < 9:
            result = 0
            break
    
    dr = [0, 0, 1, -1] + [1, 1, -1, -1]
    dc = [1, -1, 0, 0] + [-1, 1, -1, 1]

    
    for r in [1, 4, 7]:
        for c in [1, 4, 7]:
            num_cnt = set()
            num_cnt.add(arr[r][c])
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < 9 and 0 <= nc < 9:
                    num_cnt.add(arr[nr][nc])
            if len(num_cnt) < 9:
                result = 0
                break
            

    print(f'#{t} {result}')

    

    
    
            
            
        
