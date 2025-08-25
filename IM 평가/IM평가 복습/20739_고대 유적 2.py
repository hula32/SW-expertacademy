T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # 3, 3
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N): # 0,1,2
        row_val = 0 # 1,1,1
        for c in range(M): # 0,1,2
            if arr[r][c] == 1:
                row_val += 1
            if arr[r][c] == 0:
                max_val = max(max_val, row_val)
                row_val = 0

        max_val = max(max_val, row_val)
     
    
    for c in range(M):
        col_val = 0 # 0,3,0
        for r in range(N):
            if arr[r][c] == 1:
                col_val += 1
            if arr[r][c] == 0:
                max_val = max(max_val, col_val)
                col_val = 0

        max_val = max(max_val, col_val)
        
    if max_val > 1:
        print(f'#{t} {max_val}')
    else:
        print(f"#{t} 0")


        
                
            



