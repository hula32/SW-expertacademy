T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split()) # 2명 2초 1개
    person_s = sorted(list(map(int, input().split()))) # 2 3


    result = 'Impossible'
    count = 0

    for second in range(1, person_s[-1]+1): # 1,2,3,4
        if second % M == 0:
            count += K
        if person_s[0] == second:
            if count >= 1:
                result = 'Possible'
                count -= 1
                person_s.pop(0)
            else:
                result = 'Impossible'
            
    print(f'#{t} {result}')





