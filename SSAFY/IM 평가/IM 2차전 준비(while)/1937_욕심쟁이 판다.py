# 판다가 있는 지역의 대나무 다 먹기
# 상하좌우 중 이동하는데, 현재 지역보다 대나무가 더 많아야해.
# 최대 많은 칸 이동 경로 찾기

N = int(input())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def is_max(r, c):

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[r][c] < arr[nr][nc]:
                return True
    return False


def find_min_neighbor(r, c):
    max_val = arr[r][c]
    max_r, max_c = -1, -1

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if max_val < arr[nr][nc]:
                max_val = arr[nr][nc]
                max_r, max_c = nr, nc

    return max_r, max_c

def simulation(r, c):

    cnt = 1

    while is_max(r, c):
        nr, nc = find_min_neighbor(r, c)
        r, c = nr, nc
        cnt += 1
    return cnt


arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0

for r in range(N):
    for c in range(N):
        cnt = simulation(r, c)

        if cnt > max_val:
            max_val = cnt

print(max_val)