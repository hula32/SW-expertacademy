def check(row):
    for prev_row in range(row):
        # 세로탐색
        if visited[row] == visited[prev_row]:
            return False
        
        if (visited[row] - visited[prev_row]) == (row - prev_row):
            return False
        
    return True

def recur(row):
    global answer

    if row == N:
        answer += 1
        return
    
    for col in range(N):
        visited[row] = col
        if not check(row):
            continue

        recur(row + 1)

N = 8
visited = [0] * N # row 인덱스에 col 인덱스 저장하는 배열
answer = 0

recur(0)
print(answer)




# def check(row, col):
#     # 같은 열에 놓은 적 있는가?
#     for i in range(row):
#         if visited[i][col]:
#             return False

#     # 좌상단 대각선
#     i, j = row - 1, col - 1
#     while i >= 0 and j >= 0:
#         if visited[i][j]:
#             return False
        
#         i -= 1
#         j -= 1

#     # 우상단 대각선
#     i, j = row - 1, col + 1
#     while i >= 0 and j < N:
#         if visited[i][j]:
#             return False
        
#         i -= 1
#         j += 1
    
#     return True


# def recur(row):
#     global answer

#     if row == N:
#         answer += 1
#         return
    
#     for col in range(N):

#         if check(row, col) is False:
#             continue

#         visited[row][col] = 1
#         recur(row + 1)
#         visited[row][col] = 0


# N = 8
# answer = 0
# visited = [[0] * N for _ in range(N)]

# recur(0)

# print(f'{N} {answer}')
