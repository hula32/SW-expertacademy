T = int(input())

for t in range(1, T+1):
    N = int(input())

    dp = [0] * 301

    dp[10] = 1
    dp[20] = 3
    dp[30] = 5

    for i in range(40, N+1):
        dp[i] = dp[i-10] + dp[i-20] *2

    print(f'#{t} {dp[N]}')
