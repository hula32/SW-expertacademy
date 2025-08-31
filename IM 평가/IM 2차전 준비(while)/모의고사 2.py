# i열 j행
# (i+j+1) -> k의 배수이면 현상태와 다른 상태로 변함
# 0(off) 1(on)
# 1(on)의 개수 구하기

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    arr = [[0] * N for _ in range(4)]

    i = 1

    while i <= K:
        for r in range(4):
            for c in range(N):
                # if i == 0:
                #     arr[r][c] = 1
                if (r + c + 1) % i == 0:
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    elif arr[r][c] == 1:
                        arr[r][c] = 0
        i += 1

    result = 0
    for r in range(4):
        for c in range(N):
            if arr[r][c] == 1:
                result += 1

    print(f'#{t} {result}')

