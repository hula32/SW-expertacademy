T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    step = N // 2
    sums = 0

    for r in range(N):
        nums= arr[r][0+step:N-step]
        if r < mid:
            step -= 1
        if r >= mid:
            step += 1
        for n in nums:
            sums += n
    print(f'#{t} {sums}')


