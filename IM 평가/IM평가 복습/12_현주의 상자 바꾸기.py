T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())
    
    box = [0] * N

    for q in range(1, Q+1): # 1, 2
        L, R = map(int, input().split())
        for j in range(L-1, R): # 0,1,2
            box[j] = q
    print(f'#{t}', *box)

    
    