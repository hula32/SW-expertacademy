T = int(input())

for t in range(1, T+1):
    N, M = list(map(int,input().split()))
    N_list = list(map(int, input().split()))

    play = M % N

    for m in range(play):
        num = N_list.pop(0)
        N_list.append(num)

    print(f'#{t} {N_list[0]}')