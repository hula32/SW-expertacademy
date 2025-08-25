T = int(input())

for t in range(1, T+1):
    N, min_v, max_v = map(int, input().split())
    score = list(map(int, input().split()))

# N = 7
# min_v = 1
# max_v = 6
# score = [3, 3, 5, 2, 5, 1, 2]

    max_val = 0 # 5
    min_val = 101 # 1

    for sc in score:
        if max_val <= sc:
            max_val = sc
        if min_val >= sc:
            min_val = sc

    mid_val = round((max_val + min_val) / 2) #3
    print(mid_val)

    score2 = 0 # 3
    score1 = 0 # 1
    score0 = 0 # 1

    for sc in score:
        if sc == max_val:
            score2 += 1
        elif sc < mid_val:
            score0 += 1
        else :
            score1 += 1


    if min_v <= score0 <= max_v and min_v <= score1 <= max_v and min_v <= score2 <= max_v:
        max_std = max(score0, score1, score2)
        min_std = min(score0, score1, score2)
        result = max_std - min_std
    else:
        result = -1


    print(f'#{t} {result}')