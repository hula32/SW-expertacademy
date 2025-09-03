# 4행 n열 크기 LED
# 1(ON) 0(OFF)
# i+j+1 = K배수이면 다른 상태로 변한다.

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    arr = [[0] * N for _ in range(4)]

    '''
    [[0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]]

    [['', '', '', '', ''], 
    ['', '', '', '', ''], 
    ['', '', '', '', ''], 
    ['', '', '', '', '']]
    '''

    print(arr)

    # i = 1
    # cnt = 0
    # while i <= K:
    #     for r in range(4):
    #         for c in range(N):
    #             if (r+c+1) % i == 0:
    #                 if arr[r][c] == 0:
    #                     arr[r][c] = 1
    #                 else:
    #                     arr[r][c] = 0

    #     i += 1
    
    # for r in range(4):
    #     for c in range(N):
    #         if arr[r][c] == 1:
    #             cnt += 1

    # print(f'#{t} {cnt}')
