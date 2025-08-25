T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    row_sums = []
    col_sums = []

    for i in range(N): 
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        row_sums.append(row_sum)
        col_sums.append(col_sum)

    for i in range(N):
        for j in range(N):
            result = row_sums[i] + col_sums[j] - arr[i][j]

            if answer < result:
                answer = result


    print(f'#{t}', answer)



    
