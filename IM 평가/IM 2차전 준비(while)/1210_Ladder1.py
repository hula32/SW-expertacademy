# for t in range(1):
#     input()
#     arr = [list(map(int, input().split())) for _ in range(100)]
arr = [[0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 0, 2]]

    
dr = [0, 0, 1]
dc = [-1, 1, 0]

for r in range(5):
    for c in range(5):
        if arr[r][c] == 2:
            start_r, start_c = r, c 

            print(start_r, start_c)

            # while r != 0: # r이 0이 될때까지
            #     for d in range(3):
            #         nr, nc = start_r + dr[d], start_c + dc[d]
            #         if 0 <= nr < 5 and 0 <= nc < 5:
            #             if arr[nr][nc] == 1:
            #                 cnt = arr[nr][nc]
            # print(nc)

            # if r == 0:
            #     print(c)
            #     break



            