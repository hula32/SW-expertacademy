T = int(input())

for t in range(1, T+1):
    N = int(input())
    datas = list(map(int, input()))
    
    max_val = -1
    cnt = 0

    for d in datas:
        if d == 0:
            cnt = 0
        elif d == 1:
            cnt += 1
        
        if max_val < cnt:
            max_val = cnt

    print(f'#{t} {max_val}')


            