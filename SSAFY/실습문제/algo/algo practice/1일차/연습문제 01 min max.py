
T = int(input())

for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    max_val = a[0]
    min_val = a[0]

    for num in a:
        if max_val < num:
            max_val = num
        if min_val > num:
            min_val = num

    result = max_val - min_val

    print(f'#{t} {result}')
            

