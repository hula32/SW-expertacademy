T = int(input())

def recur(row, total):
    global min_val

    if row == N:
        # print(f"base, {row}, {total}")
        if min_val > total:
            min_val = total
        return  
    
    if min_val < total:
        return
    
    for col in range(N):
        if visited[col]:
            continue

        visited[col] = True
        recur(row + 1, total + arr[row][col])
        visited[col] = False

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_val = 99999
    recur(0, 0) # row, 합계
    print(f'#{t} {min_val}')