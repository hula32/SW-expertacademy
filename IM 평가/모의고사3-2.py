"""
cnt = simulation(r, c) : (r, c)에서 공굴리기 해서 cnt만 세는 함수

is_min(r,c) : (r, c)가 5개 중에서 현재 최소값인지 아닌지만 확인

while not is_min(r, c): (r,c)가 최소값이 아니면 반복, 최소값이면 종료

nr, nc = find_min_neighbor(r, c): (r, c)를 기준으로 해서 4방향 이웃 중에서 최소값의 좌표를 반환

"""

TC = int(input())

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def is_min(r, c):
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] < arr[r][c]:
                return True
    return False

def find_min_neighbor(r, c):

    min_v = arr[r][c]
    min_r, min_c = -1, -1

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] < min_v:
                min_v = arr[nr][nc]
                min_r, min_c = nr, nc
    
    return min_r, min_c


def simulation(r, c):

    cnt = 1

    while is_min(r, c): # 제일 작은 값이 아니면
        nr, nc = find_min_neighbor(r, c)
        r, c = nr, nc
        cnt += 1
    
    return cnt


for t in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N):
        for c in range(N):
            cnt = simulation(r, c)

            if max_val < cnt:
                max_val = cnt

    print(f'#{t} {max_val}')