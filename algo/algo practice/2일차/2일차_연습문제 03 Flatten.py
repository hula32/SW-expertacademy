for t in range(1, 11):
    dump = int(input()) # 834
    box_h = list(map(int, input().split())) # [42, 68, ...]

    for _ in range(dump):

        max_h = 0
        max_idx = -1
        min_h = 101
        min_idx = -1

        for idx, high in enumerate(box_h):
            if max_h < high:
                max_h = high
                max_idx = idx
            if min_h > high:
                min_h = high
                min_idx = idx
            
        box_h[max_idx] -= 1
        box_h[min_idx] += 1

        if dump == 0:
            break

        max_h = 0
        max_idx = -1
        min_h = 101
        min_idx = -1

        for idx, high in enumerate(box_h):
            if max_h < high:
                max_h = high
                max_idx = idx
            if min_h > high:
                min_h = high
                min_idx = idx

        result = max_h - min_h
    
    print(f'#{t} {result}')



    


