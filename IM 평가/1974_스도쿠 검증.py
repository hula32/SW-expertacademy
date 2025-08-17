T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = "1"

    # 행 검사
    for r in range(9):
        num = set()
        for c in range(9):
            cnt = arr[r][c]
            num.add(cnt)

        if len(num) != 9:
            result = "0"
            break
    # 열 검사
    for c in range(9):
        num = set()
        for r in range(9):
            cnt = arr[r][c]
            num.add(cnt)
            
        if len(num) != 9:
            result = "0"
            break

    dr = [-1, 1, 0, 0]+[1, 1, -1, -1]
    dc = [0, 0, 1, -1]+[-1, 1, -1, 1]

    # 3*3 검사
    for r in [1, 4, 7]:
        for c in [1, 4, 7]:
            cnt = set()
            cnt.add(arr[r][c])
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < 9 and 0 <= nc < 9:
                    cnt.add(arr[nr][nc])
            if len(cnt) != 9:
                result = "0"
                break
                    


    print(f'#{t} {result}')