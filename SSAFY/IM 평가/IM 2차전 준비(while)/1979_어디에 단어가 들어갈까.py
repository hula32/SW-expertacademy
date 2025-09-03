# N*N 배열에 K의 자리 길이 만큼 들어가는 곳 찾기
# 길이가 넘어가도 불가능
# 흰색 1, 검정 0


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# N = 5
# K = 3

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
            if arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0


        if cnt == K:
            result += 1

    # 열 검사
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0:
                if cnt == K:
                    result += 1
                cnt = 0


        if cnt == K:
            result += 1

    print(f'#{t} {result}')






