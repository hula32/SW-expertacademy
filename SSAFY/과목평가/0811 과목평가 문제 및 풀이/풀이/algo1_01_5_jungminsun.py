T = int(input())

for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    arr = [list(input())for _ in range(N)]

    result = []

    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = []
            cnt_num = 0

            for d in range(M):
                for m in range(M):
                    nr, nc = r+d, c+m
                    cnt.append(arr[nr][nc])
            for i in cnt:
                if i == '*':
                    cnt_num += 1

            if cnt_num == K:
                result.append(r)
                result.append(c)
    if not result:
        result.append(-1)
        result.append(-1)

    print(f'#{t}', *result)






