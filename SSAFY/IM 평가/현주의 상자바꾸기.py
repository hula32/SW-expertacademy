T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    
    num = []
    for q in range(Q):
        L, R = map(int, input().split())
        num.append((L, R))

    cnt = [0] * (N + 1)

    n = 1
    for l, r in num:
        for i in range(l, r+1):
            cnt[i] = n
        n += 1

    result = []
    
    for j in range(1, len(cnt)):
        result.append(cnt[j])
    
    print(f'#{t}', *result)



