arr = [[7, 3, 6, 4, 2, 9, 5, 8, 1],
[5, 8, 9, 1, 6, 7, 3, 2, 4],
[2, 1, 4, 5, 8, 3, 6, 9, 7],
[8, 4, 7, 9, 3, 6, 1, 5, 2],
[1, 5, 3, 8, 4, 2, 9, 7, 6],
[9, 6, 2, 7, 5, 1, 8, 4, 3],
[4, 2, 1, 3, 9, 8, 7, 6, 5],
[3, 9, 5, 6, 7, 4, 2, 1, 8],
[6, 7, 8, 2, 1, 5, 4, 3, 9]]

for r in range(9):
    print(arr[r])

    cnt = [0] * 10

    for num in arr[r]:
        cnt[num] += 1

    print(cnt)

    is_ok = True
    for c in range(1, 10):
        if cnt[c] != 1:
            is_ok = False
            break

    if is_ok:
        print(1)
    else:
        print(0)

for c in range(9):
    print(f"{c} column")
    cnt = [0] * 10

    for r in range(9):
        cnt[arr[r][c]] += 1
    
    print(cnt)

    is_ok = True
    for c in range(1, 10):
        if cnt[c] != 1:
            is_ok = False
            break

    if is_ok:
        print(1)
    else:
        print(0)