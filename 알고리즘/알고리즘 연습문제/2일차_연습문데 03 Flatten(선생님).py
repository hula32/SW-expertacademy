for t in range(1, 11):
    dump = int(input()) # 834
    box_h = list(map(int, input().split())) # 42 68 ...

    for _ in range(dump): # 주어진 횟수만큼 덤프를 한다.

        max_h = 0 # 최대 높이 찾기
        max_idx = -1 # 그때의 idx값 저장
        min_h = 101 # 최소 높이
        min_idx = -1 # 그때의 idex

        for idx, high in enumerate(box_h):
            if max_h < high:
                max_h = high
                max_idx = idx
            if min_h > high:
                min_h = high
                min_idx = idx

        box_h[max_idx] -= 1 # 최대 높이에서 -1
        box_h[min_idx] += 1 # 최소 높이에서 +1

        if min_h == max_h:
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

    box_score = max_h - min_h

    print(f'{t} {box_score}')


