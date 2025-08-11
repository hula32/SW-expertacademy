A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a = len(A) # 12

T = int(input())

for t in range(1, T+1):
    N, K = list(map(int, input()))

    for i in range(1<<a):
        for j in range(N):
            if i & (1<<j):
                print(A[j], end = ' ')

