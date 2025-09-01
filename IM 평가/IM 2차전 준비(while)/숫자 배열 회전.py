# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     new_arr_90 = [[0] * N for _ in range(N)]
#     for r in range(N): # 0,1,2
#         for c in range(N): # 0,1,2
#             new_arr_90[r][c] = arr[N-1-c][r]

#     new_arr_180 = [[0] * N for _ in range(N)]
#     for r in range(N): # 0,1,2
#         for c in range(N): # 0,1,2
#             new_arr_180[r][c] = new_arr_90[N-1-c][r]

#     new_arr_270 = [[0] * N for _ in range(N)]
#     for r in range(N): # 0,1,2
#         for c in range(N): # 0,1,2
#             new_arr_270[r][c] = new_arr_180[N-1-c][r]

#     print(f'#{t}')
#     for i in range(N):
#         print(''.join(map(str, new_arr_90[i])), end = ' ')
#         print(''.join(map(str, new_arr_180[i])), end = ' ')
#         print(''.join(map(str, new_arr_270[i])), end = ' ')
#         print()



T = int(input())

def new_90(arr):
    return list(map(list, zip(*arr[::-1])))

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    n_90 = new_90(arr)
    n_180 = new_90(n_90)
    n_270 = new_90(n_180)

    print(f'#{t}')
    for i in range(N):
        print(''.join(map(str, n_90[i])), end = ' ')
        print(''.join(map(str, n_180[i])), end = ' ')
        print(''.join(map(str, n_270[i])))