T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    max_val = 0

    for i in N_list:
        if max_val < i:
            max_val = i

    counts = [0] * (max_val+1)
    Temp = [0] * N

    for i in range(len(N_list)):
        counts[N_list[i]] += 1
    
    for i in range(1, max_val+1):
        counts[i] += counts[i-1]

    for i in range(N-1, -1, -1):
        counts[N_list[i]] -= 1
        Temp[counts[N_list[i]]] = N_list[i]

    print(f'#{t}', *Temp)

