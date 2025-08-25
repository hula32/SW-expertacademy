T = int(input())

for t in range(1, T+1):
    N = int(input()) # 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 # float('-inf') 가장 작은값

    row_sums = [] # 행의 값 / 4,5,4,4
    col_sums = [] # 열의 값 / 4,5,4,4

    for i in range(N): 
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        row_sums.append(row_sum)
        col_sums.append(col_sum)

    for i in range(N): # 4,5,4,4
        for j in range(N): # 4,5,4,4
            score = row_sums[i] + col_sums[j] - arr[i][j]
            
            answer = max(answer, score)
    print(f'#{t} {answer}')





