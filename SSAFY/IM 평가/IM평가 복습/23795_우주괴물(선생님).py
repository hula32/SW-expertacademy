# 0 의 수를 세어준다
# 2의 위치를 찾는 것이 중요
# 이후 레이저를 쏴서 0을 소거

# 입력받고 있는 도중에 수행 가능한 경우
# 안되는 경우 : 미로찾기
# 반복하는 객체는 반복문 안에 두면 안됨. 중복될 가능성 있음.

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, T+1):
    N = int(input()) # 크기
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 # 안전 영역의 수

    r = c = -1
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                r = i
                c = j
            elif graph[i][j] == 0:
                answer += 1

    for dir in range(4): # 방향
        
        nr = r + dr[dir]
        nc = c + dc[dir]

        while 0 <= nr < N and 0<= nc < N:
            if graph[nr][nc] == 0:
                answer -= 1
            elif graph[nr][nr] == 1:
                break

            nr += dr[dir]
            nc += dc[dir]

    print(f'#{t} {answer}')



