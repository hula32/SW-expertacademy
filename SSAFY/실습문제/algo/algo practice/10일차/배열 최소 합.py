T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # N = 3
    # arr = [[2, 1, 2],
    #        [5, 5, 5],
    #        [7, 2, 2]]

    visited = [False] * N
    res = [0] * N
    ans = 10000



    def perm(idx, total):
        global ans
        if total >= ans: # 가지치기
            return
        if idx == N: # 모든 행을 다 선택했으면
            ans = min(ans, total)
            return
        
        for c in range(N):
            if not visited[c]:
                visited[c] = True
                perm(idx+1, total + arr[idx][c])
                visited[c] = False


    perm(0, 0)
    print(f'#{t} {ans}')

    

