# T = int(input())

# for tc in range(1, T+1):
#     N = int(input()) # 4

#     pascal = []
#     for i in range(N): # 0,1,2,3
#         arr = [1] * (i+1)
#         for j in range(1, i):
#             arr[j] = pascal[i-1][j-1] + pascal[i-1][j]
#         pascal.append(arr)

#     print(f'#{tc}')
#     for p in pascal:
#         print(*p)


# T = int(input())

# for t in range(1, T+1):
#     N = int(input())

#     pascal = []
#     for i in range(N):
#         arr = [1] * (i+1)
#         for j in range(1, i):
#             arr[j] = pascal[i-1][i-j] + pascal[i-1][j]
#         pascal.append(arr)

#     print(f'#{t}')
#     for p in pascal:
#         print(*p)




T = int(input())

for t in range(1, T+1):
    N = int(input())

    pascal = []

    for i in range(N):
        arr = [1] * (i+1)
        for j in range(1, i):
            arr[j] = pascal[i-1][i-j] + pascal[i-1][j]
        pascal.append(arr)
    
    print(f'#{t}')
    for p in pascal:
        print(*p)








