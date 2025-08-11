# T = int(input())

# for t in range(1, T+1):
#     N, K = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]


N, K = 5, 3
arr = [[0, 0, 1, 1, 1], 
       [1, 1, 1, 1, 0], 
       [0, 0, 1, 0, 0], 
       [0, 1, 1, 1, 1], 
       [1, 1, 1, 0, 1]]

result = 0

# 행 순회

for r in range(N):
    cnt = 0
    for c in range(N):
        a = arr[r][c] 
        '''
        0 0 1 1 1 
        1 1 1 1 0
        0 0 1 0 0
        0 1 1 1 1
        1 1 1 0 1
        '''
        if a == 1:
            cnt += 1
        if a == 0 or arr[r][N-1]:
            if cnt == K:
                print(r, c, cnt)
                result += 1
                cnt = 0
print(result)


                


        # if cnt == K:
        #     result += 1



# print(result)

# 열 순회
# cnt = 0
# for c in range(N):
#     for r in range(N):
    
#         a = arr[r][c]
#         if a == 1:
#             cnt += 1
#     if cnt == K:
#         result += 1

# print(result)
