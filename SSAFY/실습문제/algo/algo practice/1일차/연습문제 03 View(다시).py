
T = int(10)

for t in range(1, T+1):
    N = int(input())
    NH = list(map(int, input().split()))
    
    view_sum = 0

    for idx, nh in enumerate(NH):
        if idx >= 2 and idx <= N-3:
            
            max_val = NH[idx-2]
            
            if max_val < NH[idx-1]:
                max_val = NH[idx-1]
            if max_val < NH[idx+1]:
                max_val = NH[idx+1]
            if max_val < NH[idx+2]:
                max_val = NH[idx+2]

            NH_view = nh - max_val
            if NH_view > 0:
                view_sum += NH_view


    print(f'#{t} {view_sum}')