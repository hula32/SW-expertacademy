T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    int_val = list(map(int,input().split()))

    min_val = 1000000
    max_val = -1000000
    
    for n in range(N-M+1):
        num_list = sum(int_val[n:n+M])
        if min_val > num_list:
            min_val = num_list
        if max_val < num_list:
            max_val = num_list
        
    result = max_val - min_val

    print(f'#{t}', result)