
T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    di = [-1, -1, 1, 1]
    dj = [1, -1, -1, 1]

    max_val = -1

    for r in range(N):
        for c in range(N):

            cnt = arr[r][c]

            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + dr[d] * m, c + dc[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]

            if max_val < cnt:
                max_val = cnt

            
            cnt = arr[r][c]

            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + di[d] * m, c + dj[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt += arr[nr][nc]

            if max_val < cnt:
                max_val = cnt

    print(f'#{t} {max_val}')

'''
# # 2
# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     cnt = 0

#     for i in range(N-1, 0, -1): # 4, 3, 2, 1
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 cnt += 1
#         print(*arr)
#     print(cnt)


# #3
# 1. A는 카운팅 정렬 
# : 중복이 많고, 값의 범위가 작을 때는 카운팅 정렬을 사용해야 한다.
# 값의 범위가 작고, 정수이며, 빈도 배열을 만들어 O(N+K) 시간 정렬도 가능하다.
# 중복이 많아도 빈도 계산만 하면 되서 효율적이고,

# 2. A는 선택 정렬
# : 추가 배열을 만들 수 없고, 값의 범위도 알 수 없을 때는 선택 정렬을 사용해야 한다.
# 제자리 정렬로 추가 메모리가 거의 필요하지 않고,
# 값 범위를 몰라도 비교 기반이므로 사용이 가능하다.
# 시간 복잡도는 항상 O(N^2)이지만 메모리 제약 상황에서는 현실적인 선택이다.

# 3. B는 버블 정렬
# 한 패스에서 거의 정렬된 경우, 시간 복잡도가 O(N) 이다.
# 선택 정렬은 항상 O(N^2)이라 비효율적이다.

# '''

# # 4




