# 버블정렬
T = int(input())

for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))



#     # for i in range(N-1, 0, -1): # 4, 3, 2, 1
#     #     for j in range(i):
#     #         if a[j] > a[j+1]:
#     #             a[j], a[j+1] = a[j+1], a[j]

#     # print(f'#{t}', *a)

# # 카운팅 정렬

# # N = 7
# # a = [1, 4, 7, 8, 0, 8, 9]

#     max_val = 0

#     for m in a:
#         if max_val < m:
#             max_val = m

#     cnt = [0] * (max_val+1)
#     temp = [0] * N


#     for i in range(len(a)):
#         cnt[a[i]] += 1

#     for i in range(1, max_val+1):
#         cnt[i] += cnt[i-1]

#     for i in range(N-1, -1, -1):
#         cnt[a[i]] -= 1
#         temp[cnt[a[i]]] = a[i]

#     print(f'#{t}', *temp)

# 선택정렬

    for i in range(N-1): # 0,1,2,3
        min_val = i
        for j in range(i+1, N): # 1,2,3,4
            if a[min_val] > a[j]: # 1,4,7,8 > 4,7,8,0
                min_val = j # 1,2,3,4
        a[i], a[min_val] = a[min_val], a[i]

    print(f'#{t}', *a)















