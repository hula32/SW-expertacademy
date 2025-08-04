T = int(input())

for t in range(1, T+1):
    N, M = input().split()

    num = int(M, 16)

    l = int(N) * 4

    print(f'#{t} {num:0{l}b}')