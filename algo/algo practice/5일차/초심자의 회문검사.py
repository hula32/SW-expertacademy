T = int(input())

for t in range(1, T+1):
    word = input().strip() # level

    N = len(word)
    M = N // 2

    l = 0
    r = N - 1

    is_pal = 1

    for idx in range(M):
        if word[l + idx] != word[r - idx]:
            is_pal = 0

    print(f'#{t} {is_pal}')
