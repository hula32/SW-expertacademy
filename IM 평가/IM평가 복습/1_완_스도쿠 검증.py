T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 행 검사
    for r in range(9):
        number = set()
        for c in range(9):
            number.add(arr[r][c])
        if len(number) != 9:
            result = 0
            break

    # 열 검사
    for c in range(9):
        number = set()
        for r in range(9):
            number.add(arr[r][c])
        if len(number) != 9:
            result = 0
            break
    
    # 3*3 검사
    dr = [-1,1,0,0]+[-1,-1,1,1]
    dc = [0,0,1,-1]+[1,-1,1,-1]

    for r in [1, 4, 7]:
        for c in [1, 4, 7]:
            number = set()
            number.add(arr[r][c])
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < 9 and 0 <= nc < 9:
                    number.add(arr[nr][nc])
            if len(number) < 9:
                result = 0
                break
    
    print(f'#{t} {result}')


