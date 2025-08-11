'''
T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행의 개수
    rows = len(arr)

    # 열의 개수
    cols = len(arr[0])

    # 부분배열의(파리채) 크기
    k = M
    l = M

    # 전체 탐색하면서 부분배열 추출
    # 범위 : 너무 끝까지 가면 k*l 크기를 뽑을 수 없기 때문에 -k, -l 하기

    
    total_list = []

    for r in range(rows - k + 1):
        for c in range(cols - l + 1):
            # 부분 배열을 만들기 위한 슬라이싱 사용
            # r: 행의 시작위치, c: 열의 시작위치
            # r부터 r+k까지의 행에서, 각 행마다 c부터 c+l까지 잘라냄
            sum_arr = [arr[x][c:c+l] for x in range(r, r+k)]

            # 부분배열의 합을 계산(2차원이니까 2번의 합계
            total = sum(sum(row) for row in sum_arr)
            total_list.append(total)

    # print(total_list)
    
    [25, 28, 30, 33, 41, 49, 44, 38, 26, 32, 47, 43, 28, 22, 35, 35]
    

    # 제일 높은 합계
    max_val = total_list[0]

    for i in total_list:
        if max_val < i:
            max_val = i


    print(f'#{t} {max_val}')

'''


# 선생님 파리 퇴치
T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    # 기준점(R, C)
    for R in range(N-M+1):
        for C in range(N-M+1):
            cnt = 0
            for r in range(M):
                for c in range(M):
                    cnt += arr[R+r][C+c]

            if cnt > max_cnt:
                max_cnt = cnt
                
    print(f'#{t} {max_cnt}')



    

            