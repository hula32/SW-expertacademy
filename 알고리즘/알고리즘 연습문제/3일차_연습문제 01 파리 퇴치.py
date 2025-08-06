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
            # i: 행의 시작위치, j: 열의 시작위치
            # i부터 i+k까지의 행에서, 각 행마다 j부터 j+l까지 잘라냄
            sum_arr = [arr[x][c:c+l] for x in range(r, r+k)]

            # 부분배열의 합을 계산(2차원이니까 2번의 합계
            total = sum(sum(row) for row in sum_arr)
            total_list.append(total)

    # print(total_list)
    '''
    [25, 28, 30, 33, 41, 49, 44, 38, 26, 32, 47, 43, 28, 22, 35, 35]
    '''

    # 제일 높은 합계
    max_val = total_list[0]

    for i in total_list:
        if max_val < i:
            max_val = i


    print(f'#{t} {max_val}')

    

            