# T = int(input())

# for t in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]


n = 5
m = 3
arr = [[1, 3, 3, 6, 7], 
        [8, 13, 9, 12, 8], 
        [4, 16, 11, 12, 6], 
        [2, 4, 1, 23, 2], 
        [9, 13, 4, 7, 3]]

# 상하좌우
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 대각선
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

max_val = 0

for r in range(n):
    for c in range(n):

        

        i = arr[r][c] # 파리 고정값
        for d in range(4):
            for s in range(1, m):
                nr, nc = r + dr[d]  , c + dc[d] 
                if 0 <= nr < n and 0 <= nc < n:
                    i += arr[nr][nc]
                    print(f'{arr[nr][nc]}' , end = " ")
        print()
        if max_val < i:
            max_val = i

        i = arr[r][c]
        for d in range(4):
            for s in range(1, m):
                nr, nc = r + di[d] * s, c + dj[d] * s
                if 0 <= nr < n 





    
