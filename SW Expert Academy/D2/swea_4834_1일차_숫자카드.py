# 
T = int(input())

for t in range(1, T+1):
    N = int(input())
    number = list(map(int,input())) # [4, 9, 6, 7, 9]
    cnt = [0] * 10

    for num in number:
        cnt[num] += 1

    # print(cnt)
    
    max_idx = -1 # 9
    max_count = 0 # 2

    for idx, count in enumerate(cnt):
        if count == max_count:
            if max_idx < idx:
                max_idx = idx
        elif count > max_count:
            max_count = count
            max_idx = idx
        
        

    print(f'#{t} {max_idx} {max_count}')
        


        


        