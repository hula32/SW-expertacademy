T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행의 개수
    rows = len(arr)

    # 열의 개수
    cols = len(arr[0])

    # 인덱스(r, c) 상하좌우(nr, nc)
    nr = [0, 1, 0, -1]
    nc = [1, 0, -1, 0]

    # 대각선(dr, dc)
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    max_val = 0

    for r in range(N):
        for c in range(N):
            # r, c를 중심으로
            s1 = arr[r][c] # 누적합
            s2 = arr[r][c]
            
            # 상하좌우
            for nr, nc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for p in range(1, M):
                    ni, nj = r+nr*p, c+nc*p
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]

            for dr, dc in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                for p in range(1, M):
                    di, dj = r+dr*p, c+dc*p
                    if 0 <= di < N and 0 <= dj < N:
                        s2 += arr[di][dj]

            if s1 > s2:
                if max_val < s1:
                    max_val = s1
            elif s1 < s2:
                if max_val < s2:
                    max_val = s2
            

    print(f'#{t} {max_val}')


# 선생님 파리퇴치3

# 4방 탐색 => 델타배열 만들기
# 상하좌우 델타배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 대각선 델타배열
dr2 = [1, 1, -1, -1]
dc2 = [1, -1, 1, -1]

T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # N : 배열의 크기
    # M : 스프레이의 세기

    # N x N 정사각 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 파리의 갯수 세기
    # - 모든 경우의 수를 다 세야 함
    # - (0,0) ~ (N-1, N-1)까지 N^2개의 칸을 모두 조사
    # - 4중 for문:
    #      - 2중 for문(2차원 배열 순회)
    #      - for문 : 상하좌우 또는 대각선 방향 순회(4번 반복, 델타배열 길이만큼)
    #      - for문 : 세기 M만큼 반복

    max_cnt = -1 # 최댓값 초기화(최솟값으로 초기화)

    # 2차원 배열 순회
    for r in range(N):
        for c in range(N):
            # (r, c)가 결정됨
            # 이 (r, c)를 중심으로 상하좌우, 또는 대각선을 순회

            ## 상하좌우로 보기
            cnt = arr[r][c] # 현재 중심점의 파리 갯수
            for d in range(4): # 델타배열 순회(방향 순회)
                for m in range(1, M): # 방향을 따라서 세기 만큼 순회
                    # d, m에 따라서 인접 칸의 좌표 만들기
                    nr = r + dr[d]*m
                    nc = c + dc[d]*m
                    if 0 <= nr < N and 0 <= nc < N: # 경계조건 체크 필수!!
                        cnt += arr[nr][nc] # 인접 칸의 파리 갯수를 더함
            max_cnt = max(max_cnt, cnt) # 최댓값 없데이트

            ## 대각선 방향으로 보기
            cnt = arr[r][c]  # 현재 중심점의 파리 갯수
            for d in range(4):  # 델타배열 순회(방향 순회)
                for m in range(1, M):  # 방향을 따라서 세기 만큼 순회
                    # d, m에 따라서 인접 칸의 좌표 만들기
                    nr = r + dr2[d] * m
                    nc = c + dc2[d] * m
                    if 0 <= nr < N and 0 <= nc < N:  # 경계조건 체크 필수!!
                        cnt += arr[nr][nc]  # 인접 칸의 파리 갯수를 더함
            max_cnt = max(max_cnt, cnt)  # 최댓값 없데이트

    print(f"#{tc} {max_cnt}")






