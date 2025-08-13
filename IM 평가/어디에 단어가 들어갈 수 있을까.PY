T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split()) # N : 가로세로길이 / K : 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]


    count = 0

    for r in range(N):
        row_val = 0
        for c in range(N):
            if arr[r][c] == 1:
                row_val += 1
            if arr[r][c] == 0:
                if row_val == K:
                    count += 1
                row_val = 0
        
        if row_val == K:
            count += 1

    for c in range(N):
        col_val = 0
        for r in range(N):
            if arr[r][c] == 1:
                col_val += 1
            elif arr[r][c] == 0:
                if col_val == K:
                    count += 1
                col_val = 0
    

        if col_val == K:
            count += 1

    print(f'#{t} {count}')

