def Bubble(N_list, N):
    for i in range(N-1, 0, -1): # 4, 3, 2, 1
        for j in range(i): # 0~3, 0~2, 0~1
            if N_list[j] > N_list[j+1]:
                N_list[j], N_list[j+1] = N_list[j+1], N_list[j]

    return N_list



T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    print(f'#{t}', *Bubble(N_list, N))



