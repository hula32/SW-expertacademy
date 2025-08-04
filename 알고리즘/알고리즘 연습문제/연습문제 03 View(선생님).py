T = int(10)

for tc in range(1, T+1):

    N = int(input()) # 건물개수
    NH = list(map(int, input().split())) # 건물 높이

    view_sum = 0

    for idx, nh in enumerate(NH):
        if idx >= 2 and idx <= N-3:



            # 1.
            # max_val = NH[idx-2] # 두번째 전
            # if NH[idx-1] > max_val: # 직전 건물 높이
            #     max_val = NH[idx-1]
            # if NH[idx+1] > max_val: # 앞 건물
            #     max_val = NH[idx+1]
            # if NH[idx+2] > max_val:
            #     max_val = NH[idx+2]

            # 2.
            # max_val = max(NH[idx-1], NH[idx-2])
            # max_val = max(max_val, NH[idx+1])
            # max_val = max(max_val, NH[idx+2])

            # 3.
            max_val = max(NH[idx-2], NH[idx-1], NH[idx+1], NH[idx+2])

            # idx : 현재 건물의 인덱스
            # nh : 현재 건물의 높이

            curr_view = nh - max_val # 현재 건물의 조망권확보된 세대 수
            if curr_view > 0:
                view_sum += curr_view
    
    print(f"#{tc} {view_sum}")


# 조망권이 확보된 세대의 수



