
# def search(A, B):
#     N = len(A)
#     M = len(B)

#     cnt = 0
#     i = 0
#     while i <= N - M:
#         for j in range(M):
#             if A[i+j] != B[j]:
#                 break
#         else:
#             cnt += 1
#             i += M
#             continue
#         i += 1

#     return cnt


# T = int(input())

# for t in range(1, T+1):
#     A, B = input().split() # banana / bana

#     cnt = search(A, B)
#     result = len(A) - (cnt * len(B)) + cnt

#     print(f'#{t} {result}')





def search(A, B):
    N = len(A)
    M = len(B)

    i = 0
    cnt = 0

    while i <= N-M:
        for j in range(M):
            if A[i+j] != B[j]:
                break
        else:
            cnt += 1
            i += M
            continue
        i += 1
    return cnt

T = int(input())

for t in range(1, T+1):
    A, B = input().split()

    cnt = search(A, B)
    result = len(A) - (cnt * len(B)) + cnt

    print(f'#{t} {result}')


    


    

