# 오른쪽 or 아래 이동 가능
# 최소 합계

T = int(input())

dr = [0, 1]
dc = [1, 0]

def recur(r, c, total):
    global min_val

    if r == c == N-1:
        if total < min_val:
            min_val = total
        return 
        
    for d in range(2):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N :
            recur(nr, nc, total + arr[nr][nc])

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_val = float('inf')
    
    recur(0, 0, arr[0][0])

    print(f'#{t} {min_val}')
    













        





