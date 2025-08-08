T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = 0
            for d in range(M):
                for s in range(M):
                    cnt += arr[r+d][c+s]
            print(cnt)
        print()


            





