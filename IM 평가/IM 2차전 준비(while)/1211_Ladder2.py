# arr = [[1, 0, 1, 0, 1],
#        [1, 0, 1, 1, 1],
#        [1, 1, 1, 0, 1],
#        [1, 0, 1, 1, 1],
#        [1, 0, 1, 0, 1]]

for t in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    def cnt_val(r, c):
        cnt = 0

        while r < 99:
            if c-1 >= 0 and arr[r][c-1] == 1:
                while c-1 >= 0 and arr[r][c-1] == 1:
                    c -= 1
                    cnt += 1

            elif c+1 < 100 and arr[r][c+1] == 1:
                while c+1 < 100 and arr[r][c+1] == 1:
                    c += 1
                    cnt += 1

            r += 1
            cnt += 1

        return cnt


    start = []
    for c in range(100):
        if arr[0][c] == 1:
            start.append(c)

    min_val = 9999999
    min_c = -1

    for s in start:
        steps = cnt_val(0, s)

        if min_val > steps or (steps == min_val and s > min_c):
            min_val = steps
            min_c = s



    print(f'#{t} {min_c}')
# print(min_c)



