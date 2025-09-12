# 조건 1 : 각 구역을 한번씩만 방문
# 조건 2 : 최소 배터리 사용량
# 조건 3 : 1번 사무실, 2번 ~ N번 관리구역 번호
# 조건 4 : 경사나 통행로에 따라 배터리 소비량이 다름
 
 
T = int(input())
# 배터리 소비량 계산하기
def arr_subset(path):
    result = 0
 
    for i in range(N):
        result += arr[path[i]][path[i+1]]
 
    return result
 
# 1로 시작하는 조합 만들기
def recur(cnt, start, total):
    global min_val
 
    if cnt == N:
        if path[0] == 0:
            # print(path + [0])
            '''
            [0, 1, 2, 0]
            [0, 2, 1, 0]
            '''
            min_val = min(arr_subset(path+[0]), min_val)
        return
     
    for i in range(N):
        if visited[i]:
            continue
 
        visited[i] = True
        recur(cnt+1, total + arr[])
        visited[i] = False
 
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
 
    min_val = float("inf")
    visited = [False] * N
    recur(0, 0, 0)
 
    print(f'#{t} {min_val}')