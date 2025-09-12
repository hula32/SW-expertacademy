T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_list = [[0] * (N + 1) for _ in range(N + 1)]
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            input_list[i][j] = board[i-1][j-1]

    isussed = [False] * (N + 1)
    isussed[1] = True
    min_value = -1

    def recur(num, path):
        global min_value
        if num == N - 1:
            result = input_list[1][path[0]] + input_list[path[-1]][1]
            for i in range(len(path) - 1):
                result += input_list[path[i]][path[i + 1]]
            if min_value == -1 or min_value > result:
                min_value = result
                
        for i in range(1, N + 1):
            if not isussed[i]:
                isussed[i] = True
                recur(num + 1, path + [i])
                isussed[i] = False

    recur(0, [])
    print(f"#{test_case} {min_value}")