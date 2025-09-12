arr = [
    [1, 2, 3, 4], #
    [2, 3, 4, 5], #
    [6, 4, 3, 2],
    [4, 4, 5, 5]
]

# 위 1차원 리스트(당근) 중에서
# 순증가하는 것의 개수는? 2

cnt = 0
for a in arr:
    result = True
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            result = False
            break

    if result:
        cnt += 1
print(cnt)


