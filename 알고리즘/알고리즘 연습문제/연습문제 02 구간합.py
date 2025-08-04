T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_val = -9999999
    min_val = 9999999

    for a in range(N-M+1):
        number = sum(nums[a:a+M])
        if max_val < number:
            max_val = number
        if min_val > number:
            min_val = number

    result = max_val - min_val

    print(f'#{t} {result}')

