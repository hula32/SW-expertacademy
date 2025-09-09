T = int(input())

for t in range(1, T+1):
    A, B, C = map(int, input().split())

    

    if A < 1 or B < 2 or C < 3:
        print(f'#{t} -1')
        continue
    
    cnt = 0

    if B >= C:
        cnt += B-C+1
        B = C-1
        
    if A >= B:
        cnt += A-B+1
        A = B-1
        
    print(f'#{t} {cnt}')