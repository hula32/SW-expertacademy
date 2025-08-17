# 기준점 : 시작 포인트를 컴퓨터에게 전달
# 수정을 원하면 리스트, 수정할 필요가 없으면 문자열로 받기

T = int(input())

for t in range(1, T+1):
    N = int(input()) # 최대 20까지

    graph = [input() for _ in range(N)]
    answer = "NO" # 프래그로 활용

    for i in range(N):
        for j in range(N):

            if graph[i][j] == 'o': #나로부터 4칸만 확인하면 됨
                # 가로 검사
                if j+4 < N:
                    for k in range(1, 5): # for - else : for문에 한번도 안 걸렸을 때 else로 이동
                        if graph[i][j+k] != 'o':
                            break
                    else:
                        answer = 'YES'

                # 세로 검사
                if answer == 'NO':
                    if i+4 < N:
                        for k in range(1, 5): # for - else : for문에 한번도 안 걸렸을 때 else로 이동
                            if graph[i+k][j] != 'o':
                                break
                        else:
                            answer = 'YES'

                # 좌하단 # 행과 열 둘다 바뀜
                if answer == 'NO':
                    if i+4 < N and j-4 >= 0:
                        for k in range(1, 5): # for - else : for문에 한번도 안 걸렸을 때 else로 이동
                            if graph[i+k][j-k] != 'o':
                                break
                        else:
                            answer = 'YES'

                # 우하단
                if answer == 'NO':
                    if i+4 < N and j+4 >= 0:
                        for k in range(1, 5): # for - else : for문에 한번도 안 걸렸을 때 else로 이동
                            if graph[i+k][j+k] != 'o':
                                break
                        else:
                            answer = 'YES'
            if answer == 'YES':
                break
        if answer == 'YES':
                break
    print(f'#{t} {answer}')