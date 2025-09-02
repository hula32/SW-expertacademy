N = int(input())

arr = [[0] * 101 for _ in range(101)]

for n in range(N):
    A, B = map(int, input().split())

    for r in range(B, B+10):
        for c in range(A , A+10):
            arr[r][c] = 1
    

cnt = 0

for r in range(101):
    for c in range(100):
        if arr[r][c] != arr[r][c+1]:
            cnt += 1

for c in range(101):
    for r in range(100):
        if arr[r][c] != arr[r+1][c]:
            cnt += 1


print(cnt)

