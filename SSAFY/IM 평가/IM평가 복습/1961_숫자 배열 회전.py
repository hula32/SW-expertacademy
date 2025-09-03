T = int(input())

for t in range(1, T+1):
    N = int(input()) # 3
    arr = [list(map(int, input().split())) for _ in range(N)] 

    # 90도 배열
    arr_90 = [[0] * N for _ in range(N)]

    for r in range(N): # 0,1,2
        for c in range(N): # 0,1,2
            arr_90[r][c] = arr[N-1-c][r]

    # 180도 배열
    arr_180 = [[0] * N for _ in range(N)]

    for r in range(N): # 0,1,2
        for c in range(N): # 0,1,2
            arr_180[r][c] = arr_90[N-1-c][r]

    # 270도 배열
    arr_270 = [[0] * N for _ in range(N)]

    for r in range(N): # 0,1,2
        for c in range(N): # 0,1,2
            arr_270[r][c] = arr_180[N-1-c][r]

    print(f'#{t}')
    for i in range(N):#0,1,2
        print(''.join(map(str, arr_90[i])), end = ' ')
        print(''.join(map(str, arr_180[i])), end = ' ')
        print(''.join(map(str, arr_270[i])), end = ' ')
        print()

            
        
    

        
                    
