T = 10
for t in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]

    result = 0

    for c in range(N):
        state = 0
        for r in range(N):
            if arr[r][c] == 1:
                state = 1  
            elif arr[r][c] == 2 and state == 1:
                result += 1
                state = 0
            
    
    print(f'#{t} {result}')