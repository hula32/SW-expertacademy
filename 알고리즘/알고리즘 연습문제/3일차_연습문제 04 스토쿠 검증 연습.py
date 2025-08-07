T = 10

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    value = 1

    # 행 정렬
    for r in range(9):
        result = set()
        for c in range(9):
            result.add(arr[r][c])
        if len(result) != 9:
            value = 0
            break
        
    # 열 정렬
    if value == 1:
        for c in range(9):
            result = set()
            for r in range(9):
                result.add(arr[r][c])
            if len(result) != 9:
                value = 0
                break

    # 3*3
    dr = [-1, 1, 0, 0] + [-1, -1, 1, 1]
    dc = [0, 0, -1, 1] + [-1, 1, -1, 1]

    for r in [1, 4, 7]:
        for c in [1, 4, 7]:
            result = set()
            result.add(arr[r][c])
            for b in range(8):
                nr, nc = r + dr[b], c + dc[b]
                if 0 <= nr < 9 and 0 <= nc < 9:
                    result.add(arr[nr][nc])
            if len(result) != 9:
                value = 0
                break
            
    print(f'#{t} {value}')
