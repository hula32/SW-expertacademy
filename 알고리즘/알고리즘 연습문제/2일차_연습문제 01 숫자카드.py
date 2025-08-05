T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input())) # [4, 9, 6, 7, 9]

    arr = [0] * 10

    for n in N_list:
        arr[n] += 1 # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    max_a = 0
    max_idx = -1

    for idx, a in enumerate(arr):
        if max_a < a:
            max_a = a
            max_idx = idx
        if max_a == a:
            if max_idx < idx:
                max_idx = idx
    
    
    print(f'#{t}', max_idx, max_a)
        


    
    