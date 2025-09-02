N = int(input()) # 색종이 개수

arr = [[0] * 100 for _ in range(100)]

for n in range(N):
    A, B = map(int, input().split())

    for r in range(B, B+10):
        for c in range(A, A+10):
            arr[r][c] = 1

cnt = 0

for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            cnt += 1

print(cnt)

