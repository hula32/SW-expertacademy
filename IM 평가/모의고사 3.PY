# N * N 배열
# 상, 하, 좌, 우 값 중 최솟값인 곳 -> 높은 곳에서 낮은 곳(경계 벗어나지 않음)
# 공이 가장 길게 굴러가는 루트의 최대 칸수 구하기.

# 1. 행 순회를 통해 상하좌우 검사
# 2. 상하좌우 값 중 본인보다 낮은 최솟값 찾기 
# 3. 만약 본인이 가장 낮은 값이면 break, cnt 도출
# 4. 본인보다 낮은 값이 있다면 이동 -> cnt += 1
# 5. 모든 행 순회를 검사한 후에 최대 cnt를 구하라.

# TC = int(input())

# for tc in range(1, TC+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

N = 3
arr = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# (r,c) 기준으로 해서 최소값 찾기
def search(r, c): 

    min_v = arr[r][c]
    min_r, min_c = r, c

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if min_v > arr[nr][nc]:
                min_v = arr[nr][nc]
                min_r, min_c = nr, nc 

    if min_r == r and min_c == c:
        return (-1, -1)
    else:
        return (min_r, min_c)

def work(r, c):
    min_val = arr[r][c]

    if min_val 


start_r, start_c = -1, -1
for r in range(N):
    for c in range(N):
        #  start_r, start_c = r, c # 기준점
        # (r, c) 부터 출발!
        
        


