# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]

N = 5

arr = [[1, 4, 0, 5, 4], 
       [4, 4, 2, 5, 0], 
       [0, 2, 0, 3, 2], 
       [5, 1, 2, 0, 4], 
       [5, 2, 2, 1, 2]]

mid = N//2

step = 2

for r in range(N):
    print(arr[r][0+step:N-step])
    if r < mid:
        step -= 1
    if r >= mid:
        step += 1










# for r in range(N):
#     sum_val = 0
#     for c in range(N):
#         if r < N//2 and c < N // 2:
#             pass
#         elif r < N//2 and c > N // 2:
#             pass
#         elif r > N//2 and c < N // 2:
#             pass
#         elif r > N//2 and c > N // 2:
#             pass
#         else:
#             sum_val += arr[r][c]

#             print(arr[r][c], end = ' ')
#         print()
        

