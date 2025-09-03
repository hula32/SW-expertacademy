T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(N, M)
    print(arr)

    break