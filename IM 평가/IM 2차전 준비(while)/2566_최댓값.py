arr = [list(map(int, input().split())) for _ in range(9)]

max_val = 0
max_r, max_c = -1, -1
for r in range(9):
    for c in range(9):
        if max_val <= arr[r][c]:
            max_val = arr[r][c]
            max_r, max_c = r, c

print(max_val)
print(max_r+1, max_c+1)
