TC = int(input())
def shift_length(shift_num, i, j) :
    shift_num += 1
    # print(f'shift함수에 들어온 좌표 : ({i}, {j})')
    min_val = 9999999999
    nxt_r = nxt_c = 0   # 다음 재귀 함수에 넘겨줄 좌표

    # 상, 하, 좌, 우 값 확인
    for d in range(4) :
        nr = i + dr[d]
        nc = j + dc[d]
        
        # 경계조건 확인
        if 0 <= nr < N and 0 <= nc < N :
            # print(arr[nr][nc])

            # 상, 하, 좌, 우 중 가장 최솟값
            if arr[nr][nc] < min_val and arr[nr][nc] < cursor:
                min_val = arr[nr][nc]
                nxt_r = nr
                nxt_c = nc

    if min_val < arr[i][j] :
        # print('재귀함수 진입')
        shift_num = shift_length(shift_num, nxt_r, nxt_c)

    # print(shift_num)
    # print('return하기')
    return shift_num

for t in range(1, TC+1) :
    N = int(input())    # N : 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 델타 배열
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]

    shift_num = 0
    max_len = 0
    for i in range(N) :
        for j in range(N) :
            cursor = arr[i][j]  # 시작점
            # print('------시작점 :', cursor, '-------')
            shift_result = shift_length(shift_num, i, j)

            if max_len < shift_result :
                max_len = shift_result
    
    print(f'#{t} {max_len}')
            



"""
2
3
1 2 3
4 5 6
7 8 9
4
70 42 47 32
11 1 3 59
75 90 5 81
84 42 11 59
"""