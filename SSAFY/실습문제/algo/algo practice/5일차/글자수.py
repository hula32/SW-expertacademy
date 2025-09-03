T = int(input())

for t in range(1, T+1):
    N = input()
    M = input()

    max_val = 0

    for n in N:
        if n in M:
            num = M.count(n)
            if max_val < num:
                max_val = num
    print(f'#{t} {max_val}')
