T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    mid = N//2
    step = N//2
    sums = 0

    for r in range(N): # 0,1,2,3,4
        numbers = arr[r][0+step:N-step]
        if r < mid:
            step -= 1
        if r >= mid:
            step += 1
        for nums in numbers:
            sums += nums

    print(f'#{t} {sums}')
    
    









