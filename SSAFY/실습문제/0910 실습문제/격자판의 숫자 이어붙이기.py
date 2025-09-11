T = int(input())

def recur(row, cnt):
    global answer

    if cnt == 7:
        answer += 1
        print(*path)
        return
    
    for col in range(4):
        path.append(arr[row][col])
        recur(row+1, cnt+1)
        recur(row-1, cnt+1)
        path.pop()

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    path = []
    answer = 0
    recur(0, 0)