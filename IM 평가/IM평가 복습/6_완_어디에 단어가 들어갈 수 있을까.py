T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# N, K = 5, 3
# arr = [[0, 0, 1, 1, 1], 
#        [1, 1, 1, 1, 0], 
#        [0, 0, 1, 0, 0], 
#        [0, 1, 1, 1, 1], 
#        [1, 1, 1, 0, 1]]

    result = 0

    # 행 검사
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            elif arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        else: 
            if cnt == K:
                result += 1

    # 열 검사
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            elif arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        else: 
            if cnt == K:
                result += 1

    print(f'#{t} {result}')
        

    