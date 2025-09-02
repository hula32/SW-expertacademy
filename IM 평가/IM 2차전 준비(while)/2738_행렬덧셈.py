N, M = map(int, input().split())


arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

new_arr = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        new_arr[r][c] = arr1[r][c] + arr2[r][c]

for lit in new_arr:
    print(' '.join(map(str, lit)))

    