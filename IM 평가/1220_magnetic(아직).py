# T = 10

# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]

N = 10
arr = [[1, 0, 0, 0, 0, 0, 0, 0, 2, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
       [0, 0, 0, 2, 0, 0, 2, 0, 1, 2], 
       [0, 0, 0, 0, 2, 0, 2, 0, 0, 0], 
       [0, 0, 2, 0, 0, 0, 1, 1, 1, 0], 
       [1, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
result = 0

for c in range(N):
    one_cnt = 0
    two_cnt = 0
    for r in range(N):
        if arr[r][c] == 1:
            one_cnt += 1
        elif arr[r][c] == 2:
            two_cnt += 1
    if one_cnt >= 1 and two_cnt == 0:
        pass
    elif one_cnt == 0 and two_cnt >= 1:
        pass
    elif one_cnt == two_cnt:
        result += one_cnt
    elif one_cnt > two_cnt:
        result += two_cnt
    elif one_cnt < two_cnt:
        result += one_cnt
        
print(result)
# print(f'#{t} {result}')


    # N(1)
# N = 10
# arr = [[1, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 2, 0, 0, 0, 0, 1, 2], 
#         [0, 0, 0, 0, 2, 0, 2, 0, 0, 0], 
#         [0, 0, 2, 0, 0, 0, 1, 1, 1, 0], 
#         [1, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # 4
# # S(2)

