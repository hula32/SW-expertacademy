T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 방향 : 오른쪽, 아래, 왼쪽, 위쪽(시계방향)
    dx = [0, 1, 0, -1] # 행 이동 : 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0] # 열 이동
    
    direction = 0 # 초기 방향 : 오른쪽
    x, y = 0, 0 # 시작 좌표

    for num in range(1, N*N +1):
        arr[x][y] = num # 현재 위치에 숫자 채움

        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            direction = (direction + 1) % 4 # 방향 회전
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny # 다음 위치로 이동

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ") # print(*row)
        print() # 줄 바꿈 



    
