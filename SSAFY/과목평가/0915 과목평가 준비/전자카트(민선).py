# 조건 1 : 각 구역을 한번씩만 방문
# 조건 2 : 최소 배터리 사용량
# 조건 3 : 1번 사무실, 2번 ~ N번 관리구역 번호
# 조건 4 : 경사나 통행로에 따라 배터리 소비량이 다름
 
 
# T = int(input())
# # 배터리 소비량 계산하기
# # 1로 시작하는 조합 만들기
# def recur(cnt, start, total):
#     global min_val
#     if cnt == N-1:
#         min_val = min(min_val, total+arr[start][0])
#         return
    
#     if min_val <= total:
#         return
    
#     for i in range(1, N): # 1,2,3
#         if not visited[i]:
#             visited[i] = True
#             recur(cnt + 1, i, total + arr[start][i])
#             visited[i] = False

 
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
 
 
#     min_val = float("inf")
#     visited = [False] * N
#     recur(0, 0, 0) # 조합 개수, 시작점, 총계
 
#     print(f'#{t} {min_val}')



T = int(input())

def recur(cnt, start, total):
    global min_val
    if cnt == N-1:
        total += arr[start][0]
        min_val = min(min_val, total)
        return
    
    if min_val <= total:
        return
    
    for i in range(1, N): # 1, 2
        if visited[i]:
            continue

        visited[i] = True
        recur(cnt + 1, i, total + arr[start][i])
        visited[i] = False


for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_val = float("inf")
    visited = [False] * N

    recur(0, 0, 0) # cnt, start, total
    print(f'#{t} {min_val}')