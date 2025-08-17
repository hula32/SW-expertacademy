T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split()) # 5 2



    box = [0] * N # [0,0,0,0,0]
    for i in range(1, Q+1): # 1, 2
        L, R = map(int, input().split())
        # 1 3
        # 2 4
        for j in range(L-1, R): # 0,1,2
            box[j] = i
    print(f"#{t}", *box)

        

