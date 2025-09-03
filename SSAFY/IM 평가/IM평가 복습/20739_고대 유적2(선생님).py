T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
 
    for i in range(N):
        row_one_count = 0
        for j in range(M):
            if graph[i][j] == 1:
                row_one_count += 1     
            else:
                answer = max(answer, row_one_count)
                row_one_count = 0
        answer = max(answer, row_one_count)
 
    for i in range(M):
        col_one_count = 0
        for j in range(N):
            if graph[j][i] == 1:
                col_one_count += 1
            else:
                answer = max(answer, col_one_count)
                col_one_count = 0
        answer = max(answer, col_one_count)
 
    if answer < 2:
        answer = 0
 
    print(f'#{tc} {answer}')