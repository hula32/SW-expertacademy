# for t in range(1):
#     input()
#     arr = [list(map(int, input().split())) for _ in range(100)]
arr = [[0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 0, 2]]

start_r, start_c = -1, -1
for r in range(5):
    for c in range(5):
        if arr[r][c] == 2:
            start_r, start_c = r, c 

r, c = start_r, start_c

while r != 0:
    if c-1 >= 0 and arr[r][c-1] == 1:
        while c-1 >= 0 and arr[r][c-1] == 1:
            c -= 1
    elif c+1 < 5 and arr[r][c+1] == 1:
        while c-1 < 5 and arr[r][c+1] == 1:
            c += 1
    
    r -= 1

print(c)





            