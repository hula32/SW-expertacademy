T = int(input())

def check(row):
    for prev_row in range(row):
        # 세로 검사
        if visited[row] == visited[prev_row]:
            return False
        
        # 대각선 검사
        if abs(visited[row] - visited[prev_row]) == abs(row - prev_row):
            return False
        
    return True

def recur(row):
    global answer

    if row == N:
        answer += 1
        return
    
    for col in range(N):
        visited[row] = col
        if check(row):
            recur(row + 1)

        
        
for t in range(1, T+1):
    N = int(input()) # 퀸의 개수
    # M = 8 # 체스보드의 칸 수

    visited = [0] * N
    answer = 0
    recur(0)
    print(f'#{t} {answer}')