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
    dr = [0, 1, 0, -1] + [1, 1, -1, -1]
    dc = [1, 0, -1, 0] + [1, -1, -1, 1]

    for r in range(2, 5, 8):
        for c in range(2, 5, 8):
            result = set()
            for b in range(8):
                nr, nc = r + dr[b], c + dc[b]
                result.add(arr[r][c])
                if 0 <= nr < 2 and 1 <= nc < 2:
                    pass
            if len(result) != 9:
                value = 0
    
    print(f'#{t} {value}')
