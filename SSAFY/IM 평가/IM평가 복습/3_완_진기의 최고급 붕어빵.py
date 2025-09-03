T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split()) # 2명, 2초, 2개
    num = sorted(list(map(int, input().split()))) # 3 4

    result = 'Impossible'
    count = 0

    for r in range(1, num[-1]+1):
        if r % M == 0:
            count += K
        if num[0] == r:
            if count >= 1:
                result = 'Possible'
                count -= 1
                num.pop(0)
            else:
                result = 'Impossible'
                
    
    print(f'#{t} {result}')

    





