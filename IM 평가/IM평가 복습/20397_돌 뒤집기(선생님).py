T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split()) # 2 2
        i -=  1 # 인덱스 동기화 -> #  1

        for idx in range(1, j+1): # 1, 2
            if i- idx < 0 or i+idx >= N:
                break
            
            if stones[i-idx] == stones[i+idx]:
                stones[i-idx] = (stones[i-idx]+1)%2
                stones[i+idx] = (stones[i+idx]+1)%2

    print(f'{t}', *stones)

