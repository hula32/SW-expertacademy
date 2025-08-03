T = int(input())

for t in range(1, T+1):
    N = int(input())
    n_list = list(map(int,input().split()))

    max_val = -10000000
    min_val = 10000000

    for number in n_list:
        if max_val < number:
            max_val = number
        if min_val > number:
            min_val = number

    result = max_val - min_val

    print(f'#{t} {result}')
